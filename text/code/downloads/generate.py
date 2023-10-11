from pathlib import Path

from tqdm import tqdm, trange
from math import ceil
from transformers import AutoModelForCausalLM, AutoTokenizer

from utils import root

num_samples = 150000
prefix_len = 20


out_dir = root / 'data/texts'
Path(out_dir).mkdir(exist_ok=True)

device = 'cuda'
transformer = 'gpt2'
model = AutoModelForCausalLM.from_pretrained(transformer).to(device)
tokenizer = AutoTokenizer.from_pretrained(transformer)
tokenizer.pad_token = tokenizer.eos_token

i = 1
prefixes = []
with open(Path(out_dir) / 'corpus.txt', 'r') as f:
    for line in f:
        prefixes.append(line.strip()[:prefix_len])
        if i >= num_samples:
            break
        i += 1

def save_res(res, first:bool):
    with open(Path(out_dir) / 'generation.txt', 'w' if first else 'a') as f:
        for line in res:
            f.write(f'{line}\n')


def get_batch(prefixes, beg_id, bsz):
    len_list=len(prefixes)
    end_id = beg_id + bsz
    if end_id > len_list:
        end_id = len_list
    
    return prefixes[beg_id:end_id]


res = []

# save every several pfxes
save_interval = 20
first = True
counter = 0
total = 0
batch_size = 50
len_pfxes = len(prefixes)
batches = ceil(len_pfxes/batch_size)


for idx in trange(0, len_pfxes, batch_size, total=batches):
    has_text=False
    prefix = get_batch(prefixes, idx, batch_size)
    tokens = tokenizer(prefix, return_tensors='pt', padding=True).to(device)
    text = model.generate(**tokens, do_sample=True, top_p=0.9, max_length=80,
                          pad_token_id=tokenizer.pad_token_id)
    
    texts = tokenizer.batch_decode(text)
    for text in texts:
        text = '.'.join(text.split('.')[1:]).strip()
        text = text.replace('<|endoftext|>', '')
        text = text.replace('\n', ' ')
        if text:
            res.append(text)
            has_text=True
    
    counter += int(has_text)
    
    if counter % save_interval == 0 or idx+batch_size>=len_pfxes:
        save_res(res, first=first)
        first=False
        total += len(res)
        # empty res list after one save
        res=[]

print(f"{total} lines in total")
