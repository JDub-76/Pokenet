import json

import networkx as nx
import matplotlib.pyplot as plt

# Opening JSON file
f = open('gen8vgc2022-0.json')

# returns JSON object as
# a dictionary
data = json.load(f)

g = nx.DiGraph()
pdata = data["data"]
USAGE_THRESHOLD = 0.1
PARTNER_THRESHOLD = 0.1

for i in pdata:
    if pdata[i]["usage"] >= USAGE_THRESHOLD:
        g.add_node(i)
        for teammate in pdata[i]["Teammates"]:
            pass
