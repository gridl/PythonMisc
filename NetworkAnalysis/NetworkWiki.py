
from operator import itemgetter
import networkx as nx
import wikipedia

SEED = "Black Metal".title()

# STOPS = ("International Standard Serial Number","International Standard Book Number",         "National Diet Library ", "International Stnadard Name Identifier")

STOPS = "Adrenalize"
# Create empty directed graph

todo_lst = [(0,SEED)] # The seed is in the layer 0
todo_set = set(SEED) # iThe seed itself
done_set = set() # Nothing is done yet

F= nx.DiGraph()
layer,page = todo_lst[0]

print(layer)
print(page)

while layer <2:
    del todo_lst[0]
    done_set.add(page)
    print(layer,page)

    try:
        wiki = wikipedia.page(page)
    except:
        layer,page = todo_lst[0]
        print("Could not load", page)
        continue

    for link in wiki.links:
        link = link.title()
        if link not in STOPS and not link.startswith("List of"):
            if link not in todo_set and link not in done_set:
                todo_lst.append((layer +1, link))
                todo_set.add(link)
            F.add_edge(page,link)

    layer,page = todo_lst[0]

