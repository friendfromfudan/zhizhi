from collections import  Counter
import jieba

def ordered_count(s):
    counts=([(k,v) for k,v in Counter(s).items()])
    return sorted(counts,key=lambda x:x[1],reverse=True)

s='adfaassgda'

print(ordered_count(s))


def Name(name):
    abbrs=map(lambda name:name[0].upper(),name.split())
    return '.'.join(abbrs)

assert Name('Harry Poot')=="H.P","wrong"