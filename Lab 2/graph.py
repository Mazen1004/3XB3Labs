from collections import deque
import random

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
    nodes = [i for i in range(G.number_of_nodes())]
    subsets = power_set(nodes)
    min_cover = nodes
    for subset in subsets:
        if is_vertex_cover(G, subset):
            if len(subset) < len(min_cover):
                min_cover = subset
    return min_cover




# ============== Max Independent Set =====================

def createRandomGraph(i,j):

    # if the number of edges is greater than the number of possible node connections (without duplicates) then we cannot create a list without duplicate edges
    if j > (i * (i - 1)) // 2:
        raise ValueError("Too many edges for the given number of nodes")

    graph = Graph(i)

    # generates a list of i nodes
    nodes = list(range(i))
    edge_count = 0

    while edge_count < j:
        node1 = random.choice(nodes)
        node2 = random.choice(nodes)

        # Skip if the same edge or duplicate edge is found
        if node1 == node2 or graph.are_connected(node1, node2):
            continue  
        
        graph.add_edge(node1, node2)
        edge_count += 1

    return graph


def isIndependentSet(G,S):
    for start in range(len(S)):
        for end in range(start+1,len(S)):
            if G.are_connected(S[start],S[end]):
                return False
    return True

# similar to MVC
def MIS(G):

    nodes = [i for i in range(G.number_of_nodes())]
    subSets = power_set(nodes)
    maxIndependentSet = []

    for subset in subSets: 
        # skip checking the subset if its length is less than the maxIndependentSet
        if len(subset) < len(maxIndependentSet):
                continue
        if(isIndependentSet(G,subset)):

            if len(subset) > len(maxIndependentSet):
                    maxIndependentSet = subset

    
    return maxIndependentSet


def MISvsMVC():
    numGraphs = 5

    for i in range(numGraphs):
        graph = createRandomGraph(20,40)

        minVertexCover = MVC(graph)
        maxIndependentSet = MIS(graph)

        print("Min Vertex Cover: ",minVertexCover)
        print("Max Independent Set: ",maxIndependentSet)

        sum = len(minVertexCover) + len(maxIndependentSet)
        print("Number of nodes in graph ",graph.number_of_nodes()," Sum of length of MVC and MIS ",sum)


MISvsMVC()        





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
Graph1.add_edge(4,5) #This lines creates a cycle in graph
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
        # print(values)
        # print(G.adj.items())
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
    

# Part 2 #

#------------------------- Approximations --------------------------#

def approx1_helper(G_copy, C):
    #Max Degree Count
    max_degree_count = -1
    #Highest degree vertex v
    v = None
    #Loops through adjacent list and finds highest degree vertex
    for node, adjacent_nodes in G_copy.adj.items():
        adjacent_count = len(adjacent_nodes)
        if adjacent_count > max_degree_count:
            v = node
            max_degree_count = adjacent_count
            #Set to store adjacency nodes/edges that will be deleted from copy_graph
            adjacent_set = set(adjacent_nodes)
            print("test 1",adjacent_set)
    G_copy.adj.pop(v)
    #Adds highest degree vertex to Vertex Cover Set C        
    C.add(v)
    print(C)

    #Removing all adjacent nodes from copy graph
    for adjacent_node in adjacent_set:
        print("test 2", adjacent_node)
        #Checks to see if node not already popped
        if adjacent_node in G_copy.adj:
            G_copy.adj.pop(adjacent_node)
        
    print(G_copy.adj)
    
def approx1(G):
    #Copy input graph
    G_copy = G
    #Initalize Set C
    C= set()
    print(G_copy.adj)
    
    while not is_vertex_cover(G_copy, C):
        approx1_helper(G_copy, C)
    return C


def approx2_helper(G_copy, C):
    #Get random vertex v
    while True:
        v = random.choice(list(G_copy.adj.keys()))
        print(v)
        if v not in C:
            break
        
    #add v to Vertex Cover Set C
    C.add(v)
    

def approx2(G):  
    #Copy input graph
    G_copy = G
    #Initalize Set C
    C= set()
    
    while not is_vertex_cover(G_copy, C):
        approx2_helper(G_copy, C)
    return C     

def approx3_helper(G_copy, C):  
    #Generate random edge pair (u,v)
    u = random.choice(list(G_copy.adj.keys()))
    print("val 1", u)
    adjacent_nodes = G_copy.adj[u]
    v = random.choice(adjacent_nodes)
    print("val 2", v)

    C.add(u)
    C.add(v)
    print(C)
    
    #Removing nodes/edges incident to u or v from G_copy
    adjacent_set = set()
    values = G_copy.adj[u]
    for value in values:
        adjacent_set.add(value)
        
    values2 = G_copy.adj[v]     
    for value in values2:
        adjacent_set.add(value)
    print("test 101", adjacent_set)    
    G_copy.adj.pop(u)
    G_copy.adj.pop(v)
    
     #Removing all adjacent nodes from copy graph
    for adjacent_node in adjacent_set:
        print("test 2", adjacent_node)
        #Checks to see if node not already popped
        if adjacent_node in G_copy.adj:
            G_copy.adj.pop(adjacent_node)
    

def approx3(G):  
    #Copy input graph
    G_copy = G
    #Initalize Set C
    C= set()
    print(G.adj)
    while not is_vertex_cover(G_copy, C):
        approx3_helper(G_copy, C)
    return C  

   
print("nelp",approx3(Graph1))