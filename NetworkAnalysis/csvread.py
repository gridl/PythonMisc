import networkx as nx
import matplotlib.pyplot as plt
#import dzcnapy_plotlib as dzcnapy
import csv

with open("nutrients.csv") as infile:
    csv_reader = csv.reader(infile)
    G = nx.Graph(csv_reader)
print(G.nodes())

# find self loops

loops = G.selfloop_edges()
G.remove_edges_from(loops)
print(loops)

# Relabel nodes

mapping = {node: node.title() for node in G if isinstance(node,str)}
nx.relabel_nodes(G,mapping,copy=False)
print(G.nodes())


print(G["Zn"])