
import json

import networkx as nx
import matplotlib.pyplot as plt

# Opening JSON file
f = open('gen8vgc2022-0.json')

# returns JSON object as
# a dictionary
data = json.load(f)

g = nx.DiGraph()
pdata=data["data"]
labeldict={}
nodelist=[]
nodesizes=[]
THRESHOLD=0.05

for i in pdata:
    if pdata[i]["usage"] <= THRESHOLD:

        g.add_node(i)
        labeldict[i]=i[0:]
        for teammate in pdata[i]["Teammates"]:
            #print( pdata[i]["Teammates"][teammate]/pdata[i]["Raw count"])
            if pdata[i]["Teammates"][teammate]/pdata[i]["Raw count"]>=0.03:
                if (pdata.get(teammate) is None):
                    continue
                if pdata[teammate]["usage"]>=THRESHOLD :


                    #print(teammate,pdata[teammate]["usage"])
                    g.add_edge(i,teammate,weight=format(pdata[i]["Teammates"][teammate]/pdata[i]["Raw count"],".3f"))
pos=nx.spring_layout(g)
weights=nx.get_edge_attributes(g,"weight")

edgecolors=[]

for i in weights:
    if(float(weights[i]))>=0.5:
        edgecolors.append("red")
    elif(float(weights[i]))>=0.4:
        edgecolors.append("green")
    elif (float(weights[i])) >= 0.3:
        edgecolors.append("blue")
    elif (float(weights[i])) >= 0.2:
        edgecolors.append("yellow")
    elif (float(weights[i])) >= 0.1:
        edgecolors.append("cyan")
    else:
        edgecolors.append("black")



for i in pos:
    nodesizes.append(((pdata[i]["usage"]*100)**0.8)*100)



edgelabels = nx.get_edge_attributes(g,'weight')
plt.figure(figsize=(12,12))
nx.draw(g,labels=labeldict,node_size=nodesizes,pos=pos ,font_size=18,edge_color=edgecolors,with_labels=True,connectionstyle='arc3, rad = 0.1')
#nx.draw_networkx_edge_labels(g,pos=pos,edge_labels=edgelabels)
plt.show()




plt.savefig("safe.png")