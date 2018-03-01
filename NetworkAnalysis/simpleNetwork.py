import networkx as nx

#Create an empty undirected graph

G = nx.Graph()

#Directed graphs

G = nx.DiGraph()

#Convert digraph to undirected graph

F = nx.Graph(G)

#Multigraphs - parallel edges  ALice classmate of bob but also his friend

G = nx.MultiDiGraph()

# Sample network of foods

G = nx.Graph([("A", "eggs"),])
G.add_node("spinach")
G.add_node("Hg") # mistake node
G.add_nodes_from(["foaltes", 'asparagus',"liver"])
G.add_edge("spinach", "folates") # Add one edge, both ends exist
G.add_edge("spinach", "heating oil") # Add one edge by mistake
G.add_edge("liver", "Se") # Add one edge , one end does not exist
G.add_edges_from([("folates", "liver"), ("folates", 'asparagus')])


# remove some nodes

G.remove_node("Hg")
G.remove_nodes_from(["Hg",]) # safe to remove a missing node using a list
G.remove_edge("spinach", "heating oil")
G.remove_edges_from([("spinach", "heating oil"),])
G.remove_node("heating oil")

print(G.node)

print(G.edges)

print(G.nodes(data=True))

print(G.edges(data=True))