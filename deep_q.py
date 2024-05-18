import matplotlib.pylab as plt
import networkx as nx
import numpy as np
import pandas as pd
import random
#edges=[(0,4,0.0),(4,0,0.0),(3,0,0),(0,3,10),(1,2,0.0),(2,1,0.0),(1,4,0.0),(4,1,0.0),(1,8,0.0),(8,1,0.0),(1,9,0.0),(9,1,0.0),(2,3,0),(3,2,10),(2,6,0.0),(6,2,0.0),
#       (1,5,0.0),(5,1,0.0),(5,2,0),(2,5,10),(5,6,0.0),(6,5,0.0),(8,7,0),(7,8,10),(7,5,0),(5,7,10),(8,9,0.0),(9,8,0.0),(8,10,0.0),(10,8,0.0),(9,10,0.0),(10,9,0.0)]
edges=[(0,4,20),(4,1,20),(2,1,0),(2,6,0),(5,6,0),(5,1,0),(1,8,0),(1,9,20),(0,3,10),(3,2,10),(2,5,10),(7,8,10),(5,7,10),(10,8,0),(9,10,0)]

G=nx.Graph()

G.add_weighted_edges_from(edges)
pos=nx.spring_layout(G)
nx.draw_networkx_edges(G,pos)
nx.draw_networkx_nodes(G,pos)
# draw edge labels
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
# draw node labels
node_labels = {node: node for node in G.nodes()}
nx.draw_networkx_labels(G, pos, labels=node_labels)
#nx.draw_networkx_labels(G,pos)
plt.show()
#print(G)
R=np.matrix(np.zeros(shape=(11,11)))

Q=np.matrix(np.zeros(shape=(11,11)))
#print(Q)
Q-=100

print(Q)
for node in G.nodes:
    for x in G[node]:
        #print(G[node][x]["weight"])
        #R[node,x]=G[node][x]["weight"]
        R[x,node]=G[x][node]["weight"]
        #Q[node,x]=G[node][x]["weight"]
        #Q[x,node]=G[x][node]["weight"]
for x in G[10]:
    R[x,10]=100       
#pd.DataFrame(R)
#pd.DataFrame(Q)
print(R)
###############################
def next_number(start,er):
    random_value=random.uniform(0,1)
    if random_value < er :
        sample=G[start]
    else:
        sample=np.where(Q[start,]==np.max(Q[start,]))[1]
    next_node=int(np.random.choice(sample))
    print(f"random_value:{random_value}")
    print(er)
    print(Q[start])
    print(sample)
    print(next_node)
    
    return next_node
################################
def updateQ(node1,node2,lr,discount):
    max_index=np.where(Q[node2,]==np.max(Q[node2,]))[1]
    if max_index.shape[0] >1 :
        max_index=int(np.random.choice(max_index,size=1))
    else:
        max_index=int(max_index)
    max_value=Q[node2,max_index]
    Q[node1,node2]=int((1-lr)*Q[node1,node2]+lr*(R[node1,node2]+discount*max_value))
################################
def learn (er,lr,discount):
    for i in range(500):
        start=np.random.randint(0,11)
        next_node=next_number(start,er)
        updateQ(start,next_node,lr,discount)
#################################
learn(0.3,0.8,0.8)
#print(pd.DataFrame(Q))
#################################
def shortest_path(begin,end):
    path=[begin]
    next_node=np.argmax(Q[begin,])
    path.append(next_node)
    while next_node != end:
        next_node=np.argmax(Q[next_node,])
        path.append(next_node)
    return path
###############################
print(shortest_path(0,10))
print(Q)









