#!/usr/bin/env python
import urllib,random,re

white=[]
for q in urllib.urlopen('https://raw.githubusercontent.com/johnko/devops-against-humanity/master/card-white.txt'):
    white.append(q)
black=[]
for r in urllib.urlopen('https://raw.githubusercontent.com/johnko/devops-against-humanity/master/card-black.txt'):
    black.append(r)

blank=re.compile(r"( +)?(\b|[^_])_+(\b|[^_])( +)?")
rpl=lambda _:" %s " % random.choice(white).strip()
for _ in range(10):
    print(re.sub(blank,rpl,random.choice(black)).strip().replace(' .','.'))
