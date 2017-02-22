# breadthfirst is the shortest segment
# dijkstras algorithm path with smallest total weight

graph = {}

graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2

#nodes and neighbors to the graph
graph["a"] = {}
graph["a"]["fin"] = 1

graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5
graph["fin"] = {}

infinity = float("inf")
# costs table
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity


#hashtable
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None

processed = []

def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

node = find_lowest_cost_node(costs) # find lowest cost node that you have not processed yet
while node is not None: # until processing all the nodes
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys(): # go through all the neighbors of this node
        new_cost = cost + neighbors[n] # if its cheaper to get to this  neighbor
        if costs[n] > new_cost: # by going through this node
            costs[n] = new_cost # update the cost for this node
            parents[n] = node # this node becomes the new parent for tis neighbor
    processed.append(node) # mark the node as processed
    node = find_lowest_cost_node(costs) # find the next node to process and stop


