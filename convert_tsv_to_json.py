import argparse
from tqdm import tqdm
import json

def tsv_to_triplet_jsonl(args):

    with open(args.output, 'w') as fout, \
         open(args.input, 'r') as fin:
        for line in tqdm(fin):
            q, d1, d0 = line.strip().split('\t')
            fout.write(json.dumps({
                "query": q.replace("\n", ""), 
                "positive": d1.replace("\n", ""),  
                "negative": d0.replace("\n", ""),  
            }, ensure_ascii=False)+'\n')
    fout.close()
    
    return 0

def tsv_to_double_jsonl(args):
    with open("triples.train.small.tsv", 'r') as f, \
         open('marco_psg.train.doubles.jsonl', 'w') as fout:
        for line in tqdm(f):
            q, d1, d0 = line.strip().split('\t')
            fout.write(json.dumps({
                "query": q.replace("\n", ""), 
                "passage": d1.replace("\n", ""),  
                "relevant": 'true'
            }, ensure_ascii=False)+'\n')
            fout.write(json.dumps({
                "query": q.replace("\n", ""), 
                "passage": d0.replace("\n", ""),  
                "relevant": 'false'
            }, ensure_ascii=False)+'\n')
    return 0

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=str)
    parser.add_argument("--output", type=str)
    parser.add_argument("--triplet", action='store_true', default=False)
    args = parser.parse_args()

    if args.triplet:
        tsv_to_triplet_jsonl(args)
