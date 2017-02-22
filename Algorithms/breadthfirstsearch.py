# is there a path from node A to node B?
# what is the shortest path from node A to node B?
# directed graph = one way

from collections import deque
graph = {}
graph["you"] = ["axe", "box","cox"]
graph["box"] = ["an","pa"]
graph["axe"] = ["pa"]
graph["cox"] = ["to", "jom"]
graph["an"] = []
graph["pa"] = []
graph["to"] = []
graph["jom"] = []




def person_is_seller(name):
    return name[-1] == 'm'

def search(name):
    search_queue = deque() # creates a new queue
    search_queue += graph[name]# adds all neighbors to the search queue
    searched = []
    print(search_queue)

    while search_queue:#while queue is not empty
        person = search_queue.popleft()
        print(person)
        if not person in searched:
            if person_is_seller(person):
                print(person + " is a mange seller!")
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False

search("you")