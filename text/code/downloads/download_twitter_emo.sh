tgt_dir=${1:-$(pwd)/../../data/raw/twitter}

mkdir -p $tgt_dir
tgt_dir=$(readlink -f $tgt_dir)
echo $tgt_dir


twitter()
{
    src_url="https://raw.githubusercontent.com/cardiffnlp/tweeteval/main/datasets/emotion"
    for file in "mapping.txt" "train_labels.txt" "train_text.txt" "test_labels.txt" "test_text.txt" "val_labels.txt" "val_text.txt";
    do
        wget -O "$tgt_dir/$file" "$src_url/$file" 
    done
}

twitter