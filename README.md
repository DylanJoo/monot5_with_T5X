# Training monot5 with T5X

Followed the work of monot5 [Document Ranking with a Pretrained Sequence-to-Sequence Model](https://aclanthology.org/2020.findings-emnlp.63/).
But change the T5 framework from T5 to T5X, which is the latest (and will update) framework from Google.


1. Download train triple from MS MARCO

2. Convert tsv to monot5
```
Input: Query :<q> Document: <d> Relevant:
Output: true/false
```

