from graph import Graph
from testing import *
# from exp1 import createRandomGraph
import random
import matplotlib.pyplot as plt


def isConnected(graph):
    visited = set()

    def dfs(node):
        visited.add(node)
        for neighbor in graph.adjacent_nodes(node):
            if neighbor not in visited:
                dfs(neighbor)
    
     # Get the first node in the adjacency list
    startNode = next(iter(graph.adj))

    dfs(startNode)
    
    # check if there is a path from the start node to every other node in the graph
    return len(visited) == graph.number_of_nodes()


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

numEdges = [100, 150, 200, 250, 300, 350, 400]



def exp2():
    numGraphs = 100
    connectedCounts = []

    for numEdge in numEdges:
        connectCount = 0
        
        for i in range(numGraphs):
            graph = createRandomGraph(100, numEdge)
            
            if(isConnected(graph)):
                connectCount += 1

        connectedCounts.append(connectCount)
    


    
    print(connectedCounts)
    return connectedCounts




connectedCounts = exp2()
plt.plot(numEdges,connectedCounts)
plt.xlabel("number of Edges")
plt.ylabel("Connected Graph Probability (%)")
plt.title("Edges vs Connected Probability (%)")
plt.show()
