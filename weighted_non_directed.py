import json

import networkx as nx
import matplotlib.pyplot as plt

# Opening JSON file
f = open('gen8vgc2022-0.json')

# returns JSON object as
# a dictionary
data = json.load(f)
pdata = data["data"]

g = nx.Graph()
labeldict = {}
nodelist = []
nodesizes = []
USAGE_THRESHOLD = 0.162
PARTNER_THRESHOLD = 0.162
SINGLE_MON = ""



