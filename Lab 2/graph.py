from collections import deque

#Undirected graph using an adjacency list
class Graph:

    def __init__(self, n):
        self.adj = {}
        for i in range(n):
            self.adj[i] = []

    def are_connected(self, node1, node2):
        return node2 in self.adj[node1]

    def adjacent_nodes(self, node):
        return self.adj[node]

    def add_node(self):
        self.adj[len(self.adj)] = []

    def add_edge(self, node1, node2):
        if node1 not in self.adj[node2]:
            self.adj[node1].append(node2)
            self.adj[node2].append(node1)

    def number_of_nodes(self):
        return len(self.adj)


#Breadth First Search
def BFS(G, node1, node2):
    Q = deque([node1])
    marked = {node1 : True}
    for node in G.adj:
        if node != node1:
            marked[node] = False
    while len(Q) != 0:
        current_node = Q.popleft()
        for node in G.adj[current_node]:
            if node == node2:
                return True
            if not marked[node]:
                Q.append(node)
                marked[node] = True
    return False


#Depth First Search
def DFS(G, node1, node2):
    S = [node1]
    marked = {}
    for node in G.adj:
        marked[node] = False
    while len(S) != 0:
        current_node = S.pop()
        if not marked[current_node]:
            marked[current_node] = True
            for node in G.adj[current_node]:
                if node == node2:
                    return True
                S.append(node)
    return False


#Use the methods below to determine minimum Vertex Covers
def add_to_each(sets, element):
    copy = sets.copy()
    for set in copy:
        set.append(element)
    return copy

def power_set(set):
    if set == []:
        return [[]]
    return power_set(set[1:]) + add_to_each(power_set(set[1:]), set[0])

def is_vertex_cover(G, C):
    for start in G.adj:
        for end in G.adj[start]:
            if not(start in C or end in C):
                return False
    return True

def MVC(G):
    nodes = [i for i in range(G.get_size())]
    subsets = power_set(nodes)
    min_cover = nodes
    for subset in subsets:
        if is_vertex_cover(G, subset):
            if len(subset) < len(min_cover):
                min_cover = subset
    return min_cover


#------------------------ PART 1 -------------------------#

"""
            0
          / /              
         1  2
           /
          3
         /
        4           5(not connected)
"""
print("CREATING GRAPH")
Graph1=Graph(6)
Graph1.add_edge(0,1)
Graph1.add_edge(0,2)
Graph1.add_edge(2,3)
Graph1.add_edge(3,4)
Graph1.add_edge(1,3) #This lines creates a cycle in graph
Graph1.are_connected(1,2)
print(Graph1.number_of_nodes()) 

def BFS2(G, node1, node2):
    Q = deque([(node1, [node1])])  # Queue now stores tuples (node, path)
    marked = {node1: True}

    while Q:
        current_node, path = Q.popleft()

        if current_node == node2:
            # We found node2, return the path taken
            return path

        for neighbor in G.adj[current_node]:
            if not marked.get(neighbor, False):
                marked[neighbor] = True
                new_path = path + [neighbor]  # Create a new path by appending the neighbor
                Q.append((neighbor, new_path))

    return []  # Return an empty list if no path is found

def DFS2(G, node1, node2):
    S = [(node1, [node1])]  # Stack stores tuples (node, path)
    marked = {node1: True}

    while S:
        current_node, path = S.pop()

        if current_node == node2:
            # We found node2, return the path taken
            return path

        for neighbor in G.adj[current_node]:
            if not marked.get(neighbor, False):
                marked[neighbor] = True
                new_path = path + [neighbor]  # Create a new path by appending the neighbor
                S.append((neighbor, new_path))

    return []  # Return an empty list if no path is found

def BFS3(G, startNode):
    Q = deque([startNode])
    path_dictionary = {}
    while len(Q) != 0:
        #print("Queue is:" ,Q)
        current_node = Q.popleft()
        for node in G.adj[current_node]:
            #Check if node is not starting node and not already in dictionary
            if node != startNode and node not in path_dictionary: 
                path_dictionary[node] = current_node
                #print(path_dictionary)
                Q.append(node)
                
    return path_dictionary       


def DFS3(G, startNode):
    S = [startNode]
    path_dictionary = {}
    marked = {}
    for node in G.adj:
        marked[node] = False
    while len(S) != 0:
        #print("Stack is:", S)
        current_node = S.pop()
        #print("Exploring: ", current_node)
        if not marked[current_node]:
            marked[current_node] = True
            for node in G.adj[current_node]:
                if node != startNode and node not in path_dictionary:
                    path_dictionary[node] = current_node
                    #print(path_dictionary)
                S.append(node)
                
    return path_dictionary

#For this function, inefficient to use BFS or DFS code
def is_connected(G):
    #Loop through each item in dictionary e.g (0,[1,2])
    for values in G.adj.items(): 
        print(values)
        print(G.adj.items())
        if not values:
            return False
    return True

def has_cycle(G):
    #Get starting node for DFS search
    startNode = list(G.adj.keys())[0]
    #path dictionary has parent nodes of each node
    path_dictionary = DFS3(G,startNode)
    
    #Loop through path dictionary
    for node, parent in path_dictionary.items():       
        #if parent value is smaller than node, this mean there should only be one value
        #smaller than node if there is no cycles
        if parent < node:
            node_adjacency = G.adj[node]
            #print("node_adj",node_adjacency)
            count = 0
            for node in node_adjacency:
                if node <= parent:  
                    count += 1
            if count > 1:
                #means there is more than one parent (cycle)
                return True
            #print("Test",node_adjacency)
        #if parent value is greater than node, this mean there should only be one value
        #greater than node if there is no cycles
        if parent > node:
            node_adjacency = G.adj[node]
            count = 0
            for node in node_adjacency:
                if node >= parent:
                    count += 1
            if count > 1:
                #means there is more than one parent (cycle)
                return True
    #print(G.adj)            
    return False
    

print(has_cycle(Graph1))
