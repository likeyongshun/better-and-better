import os
import sys
import json

wenjian1 = sys.argv[1]
wenjian2 = sys.argv[2]
wenjian3 = sys.argv[3]

def need_concat(wenjian1, wenjian2):
    with open(wenjian1)as f:
        w1 = json.load(f)
    with open(wenjian2)as f:
        w2 = json.load(f)
    return w1, w2

w3 = []
w3.extend([need_concat(wenjian1, wenjian2)[0],
          need_concat(wenjian1, wenjian2)[1]])
print(w3)
temp = []
for i in w3:
    if not i in temp:
        temp.append(i)
# # temp=list(set(w3))
# # temp.sort(key=w3.index)
# # print(temp)

def concat(wenjian3, name):
    path = wenjian3+os.sep+name
    with open(path, 'w')as f:
        temp2 = ''.join(str(temp))
        return json.dumps(f.write(temp2), indent=4, check_circular=False)

if not os.path.exists(wenjian3):
    os.makedirs(wenjian3)
need_concat(wenjian1, wenjian2)
name = 'ys.json'
concat(wenjian3, name)