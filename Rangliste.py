# Opening JSON file
import json

f = open('gen8vgc2022-0.json')

# returns JSON object as
# a dictionary
data = json.load(f)
pdata = data["data"]

a=sorted(pdata, key=lambda x: (pdata[x]['usage']))

a.reverse()

for i in range(10):
    print(i+1,a[i],pdata[a[i]]["usage"])
