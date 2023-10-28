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

def approxExperiment1():
    numEdges = [1,5,10,20,25]
    mvcCount = 0
    mvcArray = []
    approx1Count = 0
    approx1Array = []
    approx2Count = 0
    approx2Array = []
    approx3Count = 0
    approx3Array = []
    #Generating 1000 graphs so 200 graphs for each num of edges (Nodes is constant at 8)
    for num in numEdges:
        for _ in range(200):
            graph = createRandomGraph(8, num)
            
            mvcCount = mvcCount + len(MVC(graph))      
            
            approx1Count = approx1Count + len(approx1(graph))
            
            approx2Count = approx2Count + len(approx2(graph))
            
            approx3Count = approx3Count + len(approx3(graph))
            
        #After 200 graphs generated for each m edges we append them to their corresponding array
        mvcArray.append(mvcCount)
        #Calculating performance by dividing each approx by mvc
        performance1Calc= approx1Count/mvcCount
        performance2Calc=approx2Count/mvcCount
        performance3Calc=approx3Count/mvcCount
        approx1Array.append(performance1Calc)
        approx2Array.append(performance2Calc)
        approx3Array.append(performance3Calc)    
                   
    plt.plot(numEdges, approx1Array, label = "Approx1")
    plt.plot(numEdges, approx2Array, label = "Approx2")
    plt.plot(numEdges, approx3Array, label = "Approx3")
    
    # naming the x axis
    plt.xlabel('Number of Edges (m)')
    # naming the y axis
    plt.ylabel('Expected Performance')
    
    # giving a title to my graph
    plt.title('Performance of Vertex Cover Approximations when Increasing Edges')

    # show a legend on the plot
    plt.legend()
    
    # function to show the plot
    plt.show()
    
def approxExperiment2():
    numNodes = [6,8,10,12,14]
    mvcCount = 0
    mvcArray = []
    approx1Count = 0
    approx1Array = []
    approx2Count = 0
    approx2Array = []
    approx3Count = 0
    approx3Array = []
    #Generating 1000 graphs so 200 graphs for each num of nodes (Edges is constant at 4)
    for num in numNodes:
        for _ in range(200):
            graph = createRandomGraph(num, 4)
            
            mvcCount = mvcCount + len(MVC(graph))      
            
            approx1Count = approx1Count + len(approx1(graph))
            
            approx2Count = approx2Count + len(approx2(graph))
            
            approx3Count = approx3Count + len(approx3(graph))
            
        #After 200 graphs generated for each m edges we append them to their corresponding array
        mvcArray.append(mvcCount)
        #Calculating performance by dividing each approx by mvc
        performance1Calc= approx1Count/mvcCount
        performance2Calc=approx2Count/mvcCount
        performance3Calc=approx3Count/mvcCount
        approx1Array.append(performance1Calc)
        approx2Array.append(performance2Calc)
        approx3Array.append(performance3Calc)  
                   
    plt.plot(numNodes, approx1Array, label = "Approx1")
    plt.plot(numNodes, approx2Array, label = "Approx2")
    plt.plot(numNodes, approx3Array, label = "Approx3")
    
    # naming the x axis
    plt.xlabel('Number of Edges (m)')
    # naming the y axis
    plt.ylabel('Expected Performance')
    
    # giving a title to my graph
    plt.title('Performance of Vertex Cover Approximations when Increasing Nodes')

    # show a legend on the plot
    plt.legend()
    
    # function to show the plot
    plt.show()
    
def approxExperiment3(): 
    numNodes = [0, 1, 2, 3, 4]
    possibleEdges = []
    
    worstCaseSize = -1
    worstCaseGraph = None
    
    #Creating all possible edges
    for i, node1 in enumerate(numNodes):
        for node2 in numNodes[i+1:]:
            possibleEdges.append((node1, node2))
    
    #Creating all the possible graphs
    for edges in range(2**len(possibleEdges)):
        graph = Graph(5)
        for i, edge in enumerate(possibleEdges):
            if (edges > i) & 1:
                graph.add_edge(edge[0], edge[1])
        minCover = len(approx1(graph))
        #Finding worst case graph
        if minCover > worstCaseSize:
            worstCaseGraph = graph
            worstCaseSize = minCover
            
    print("Worst Case Graph: ")
    print("Nodes -> Edges")
    for node, neighbors in worstCaseGraph.adj.items():
        print(node, "----->", neighbors)
    
    
#----- Experiment Runner ------#    
approxExperiment1()    
approxExperiment2()
approxExperiment3()    