#!/usr/bin/env python
import random,re

white=[]
for q in open('./card-white.txt', 'rb'):
    white.append(q)
black=[]
for r in open('./card-black.txt', 'rb'):
    black.append(r)

blank=re.compile(r"( +)?(\b|[^_])_+(\b|[^_])( +)?")
rpl=lambda _:" %s " % random.choice(white).strip()
for _ in range(10):
    print(re.sub(blank,rpl,random.choice(black)).strip().replace(' .','.'))
