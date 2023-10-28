from graph import Graph,has_cycle
from testing import *
import random
import matplotlib.pyplot as plt


def createRandomGraph(i,j):

    # if the number of edges is greater than the number of possible node connections (without duplicates) then we cannot create a list without duplicate edges
    # n Choose 2 max possible connections
    if j > (i * (i - 1)) // 2:
        raise ValueError("Too many edges for the given number of nodes")

    graph = Graph(i)

    # generates a list of i nodes
    nodes = list(range(i))
    edge_count = 0

    while edge_count < j:
        node1 = random.choice(nodes)
        node2 = random.choice(nodes)

        # Skip current iteration if the same edge or duplicate edge is found
        if node1 == node2 or graph.are_connected(node1, node2):
            continue  
        
        graph.add_edge(node1, node2)
        edge_count += 1

    return graph




# number of each graph
#numEdges = [500,1000,1500,2000,2500]

numEdges = [25,50,75,100,125,150,175,200]
def experiment1():
    
    numGraphs = 100
    cycleCounts = []

    for numEdge in numEdges:
        cycleCount = 0 


        for i in range(numGraphs):
            graph = createRandomGraph(100, numEdge)
            
            if(has_cycle(graph)):
                cycleCount += 1

        cycleCounts.append(cycleCount)
    
    print(cycleCounts)
    return cycleCounts 


cycleCounts = experiment1()

plt.plot(numEdges,cycleCounts)
plt.xlabel("number of Edges")
plt.ylabel("Cycle Probability (%)")
plt.title("Edges vs Cycle Probability (%)")
plt.show()




