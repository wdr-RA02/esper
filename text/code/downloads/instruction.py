'''
https://github.com/mahnazkoupaee/WikiHow-Dataset
'''
import json
import csv
from pathlib import Path

import gdown
from tqdm import tqdm

from utils import root


_DATA_URL = "https://public.boxcloud.com/d/1/b1!_3cQ2QwKJtNXCEadwVoqkI6Yw8ShCpukwIX0no1ORDo0vSrz_0cnNqjRMORXNNOLd6gkEHisvPszOVXL3cJwR9M54nZo7q9DV06PfXBJ8CFwENEh0cTk7c1ZrI6R_41H1_cTecdwj2MlEf7Uvp7KkRn_WzgPBBEPPbham_9eWFQH_LhW-Bo_EpDobe0srGeFXO-4edfLoeHwl_5FMma1HEs2u9jJ3vo6Yz7li8GF0x-aYUuLUvQ-bdrApK1yH3De-TAOCtKX1_MWZwTTvu5MxSSiGa2aW282AOUmg7AgG4CCb6IcCEFX_OHILLXfGGKShw68A628tWm1Qb17-IZ3SqHgFwVLrEV-zGfy9lZ36WgdO_G9lWYtGE7DPHAdrxJnvj96o-Oi1LA0Ymj9K-t-fAb0RwyBhT7AkDoJJJkL7srI3oLBRawcnNA4XeoDDxp8CF0F7lXBcpfNftGjwqV-1NCERmjHx8-FCJHbZnCoxcuWBxbcF36qrm7NsDYPjuCsUKVBjOgnUpJQ0vpVBwAL4HoHtzRS1lR8HOlxgLnbtm1m2d8FBx3xX3zsc21oJRITnkMvyhIyYMo04fvPTRgpO0vovvfipNYVLuPXkV5IepsZKwsHeF5eE0HF50nB8dauTbu2Xq09iAaCtBn4-FjorGN1mgaCp7CEDq81KIMeNOqHAwwJ5_1VZ6E9awXXMNU6kjcCITAHTMU9BxGLNnzEbdzrz8-v-_EBF0Zb4k4D_Ay0GNVSJT1QF27_vlBQXMYf-bBJPxuB4ieW2tX8z1J20-B2Ee_iGwZi6l24DzqOIttjO7IL_g1C6B5D_SJpLCdh7naHmoVcScQTTm57372aiBrlYtl3rcFuN0anQafugnWUMmwEE5lZUVYzFfqixKmH4PKywkgZmvEsa3VFinRLyNbTTWASCJLWUPkIV55G6wmmKu2Fxotvd2lD3Inos9a3Yc75dKISatqm0jVGnXZ0AxtY-PxPc2zs_EylmQL6IvEhlaL2DB2o_WbWPj_woPrBaQ-ZlFIciuggKs7iJr7fAH_pUoeeC8x2V6kHauy09PMjji7jEH1cUifocJitPQFURdAQHbderP9ra8Grd_zIheIvo-cGkd0GiAaRaGbuQNTJByHiaq9d_ai9N-taSS3FJr9K6JlxVYHjiPwiX9Pz6b2IHfpWCOsewZDRHKSPsxRwiMoVRQrTG-Ub9wvh-RW3nfKRq5fEjYkCjGlHOuBoomxWC1RHQJWBem0PRZHkkw../download"


data_dir = root / 'data/raw/instruction'
out_dir = root / 'data/texts'
data_dir.mkdir(exist_ok=True)
Path(out_dir).mkdir(exist_ok=True)

data_path = data_dir / 'wikihowAll.csv'

if not data_path.is_file():
    gdown.download(_DATA_URL, str(data_path), quiet=False)

data = []
with open(data_path) as f:
    reader = csv.reader(f)
    for row in tqdm(reader):
        txt = row[0].strip()
        txt = '.'.join(txt.split('.,'))
        data.append(txt.replace('\n', ' '))

print(f"{len(data)} lines in total")
with open(Path(out_dir) / 'instruction.txt', 'w') as f:
    for line in data:
        f.write(f'{line}\n')
