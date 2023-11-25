from pstats import Stats
#from scipy.stats import linregress
import time
import min_heap2
import random
import matplotlib.pyplot as plt
import numpy as np

class DirectedWeightedGraph:

    def __init__(self):
        self.adj = {}
        self.weights = {}

    def are_connected(self, node1, node2):
        for neighbour in self.adj[node1]:
            if neighbour == node2:
                return True
        return False

    def adjacent_nodes(self, node):
        return self.adj[node]

    def add_node(self, node):
        self.adj[node] = []

    def add_edge(self, node1, node2, weight):
        if node2 not in self.adj[node1]:
            self.adj[node1].append(node2)
        self.weights[(node1, node2)] = weight

    def w(self, node1, node2):
        if self.are_connected(node1, node2):
            return self.weights[(node1, node2)]

    def number_of_nodes(self):
        return len(self.adj)


def dijkstra(G, source):
    pred = {} #Predecessor dictionary. Isn't returned, but here for your understanding
    dist = {} #Distance dictionary
    Q = min_heap2.MinHeap([])
    nodes = list(G.adj.keys())

    #Initialize priority queue/heap and distances
    for node in nodes:
        Q.insert(min_heap2.Element(node, float("inf")))
        dist[node] = float("inf")
    Q.decrease_key(source, 0)

    #Meat of the algorithm
    while not Q.is_empty():
        current_element = Q.extract_min()
        current_node = current_element.value
        dist[current_node] = current_element.key
        #Looping through all the neighbors of extracted element
        for neighbour in G.adj[current_node]:
            #If calculated distance is less than current distance stored for adjacent vertex from source code
            if dist[current_node] + G.w(current_node, neighbour) < dist[neighbour]:
                #Decrease value in min heap to new updated distance
                Q.decrease_key(neighbour, dist[current_node] + G.w(current_node, neighbour))
                #Update distance and pred tables
                dist[neighbour] = dist[current_node] + G.w(current_node, neighbour)
                pred[neighbour] = current_node
    return dist


def bellman_ford(G, source):
    pred = {} #Predecessor dictionary. Isn't returned, but here for your understanding
    dist = {} #Distance dictionary
    nodes = list(G.adj.keys())

    #Initialize distances
    for node in nodes:
        dist[node] = float("inf")
    dist[source] = 0

    #Meat of the algorithm
    for _ in range(G.number_of_nodes()):
        for node in nodes:
            for neighbour in G.adj[node]:
                if dist[neighbour] > dist[node] + G.w(node, neighbour):
                    dist[neighbour] = dist[node] + G.w(node, neighbour)
                    pred[neighbour] = node
    return dist


def total_dist(dist):
    total = 0
    for key in dist.keys():
        total += dist[key]
    return total

def create_random_complete_graph(n,upper):
    G = DirectedWeightedGraph()
    for i in range(n):
        G.add_node(i)
    for i in range(n):
        for j in range(n):
            if i != j:
                G.add_edge(i,j,random.randint(1,upper))
    return G


#Assumes G represents its nodes as integers 0,1,...,(n-1)
def mystery(G):
    n = G.number_of_nodes()
    d = init_d(G)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if d[i][j] > d[i][k] + d[k][j]: 
                    d[i][j] = d[i][k] + d[k][j]
    return d

def init_d(G):
    n = G.number_of_nodes()
    d = [[float("inf") for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            if G.are_connected(i, j):
                d[i][j] = G.w(i, j)
        d[i][i] = 0
    return d

#Functions needed to create random graphs
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

    graph = DirectedWeightedGraph()
    
    # Adding nodes to the graph
    for node in range(i):
        graph.add_node(node)

    edge_count = 0

    while edge_count < j:
        node1 = random.choice(range(i))
        node2 = random.choice(range(i))

        # Skip if the same edge or duplicate edge is found
        if node1 == node2 or graph.are_connected(node1, node2):
            continue  
        
        graph.add_edge(node1, node2, random.randint(1, 10))
        edge_count += 1

    return graph

#Shortest Path Approximations

def dijkstra_approx(G, source, k):
    pred = {} #Predecessor dictionary. Isn't returned, but here for your understanding
    dist = {} #Distance dictionary
    relaxCount = {} #Relaxation count for each node
    Q = min_heap2.MinHeap([])
    nodes = list(G.adj.keys())

    #Initialize priority queue/heap and distances
    for node in nodes:
        Q.insert(min_heap2.Element(node, float("inf")))
        dist[node] = float("inf")
        relaxCount[node] = 0
    Q.decrease_key(source, 0)

    #Meat of the algorithm
    while not Q.is_empty():
        current_element = Q.extract_min()
        current_node = current_element.value
        dist[current_node] = current_element.key
        #Looping through all the neighbors of extracted element
        for neighbour in G.adj[current_node]:
            #Count for max relaxations
            #If calculated distance is less than current distance stored for adjacent vertex from source code
            if dist[current_node] + G.w(current_node, neighbour) < dist[neighbour] and relaxCount[neighbour] < k:
                relaxCount[neighbour] +=1
                #Decrease value in min heap to new updated distance
                Q.decrease_key(neighbour, dist[current_node] + G.w(current_node, neighbour))
                #Update distance and pred tables
                dist[neighbour] = dist[current_node] + G.w(current_node, neighbour)
                pred[neighbour] = current_node
    return dist

def bellman_ford_approx(G, source, k):
    pred = {} #Predecessor dictionary. Isn't returned, but here for your understanding
    dist = {} #Distance dictionary
    relaxCount = {} #Relaxation count for each node
    nodes = list(G.adj.keys())

    #Initialize distances
    for node in nodes:
        dist[node] = float("inf")
        relaxCount[node] = 0
    dist[source] = 0

    #Meat of the algorithm
    for _ in range(G.number_of_nodes()):
        for node in nodes:
            for neighbour in G.adj[node]:
                if dist[neighbour] > dist[node] + G.w(node, neighbour) and relaxCount[neighbour] < k:
                    relaxCount[neighbour] +=1
                    dist[neighbour] = dist[node] + G.w(node, neighbour)
                    pred[neighbour] = node
    return dist


def experiment_suite1():
    #Loop to generate a graphs that get more dense with time
    #After each graph is generated it is run through each of the 4 algorithms
    #Time duration plotted vs number of edges
    #n(n-1)/2  
    max_number_of_edges = 200
    number_of_nodes = 20
    min_number_of_edges = int(number_of_nodes-1)
    print(min_number_of_edges)
    max_number_of_edges = int((number_of_nodes*(number_of_nodes-1))/2)
    print(max_number_of_edges)
    max_relax_count = 1
    number_of_nodes_array = []
    dijkstra_approx_array = []
    dijkstra_array = []
    bellman_ford_array = []
    bellman_ford_approx_array = []
    for number_of_edges in range(min_number_of_edges, max_number_of_edges+1):
        number_of_nodes_array.append(number_of_edges)
        Graph = createRandomGraph(number_of_nodes, number_of_edges)
        #Distance for Dijkstra
        dijkstra_array.append(total_dist(dijkstra(Graph,0)))
        #Distance for Dijkstra Approx
        dijkstra_approx_array.append(total_dist(dijkstra_approx(Graph,0,max_relax_count)))
        #Distance for Bellman Ford
        bellman_ford_array.append(total_dist(bellman_ford(Graph,0)))
        #Distance for Bellman Ford Approx
        bellman_ford_approx_array.append(total_dist(bellman_ford_approx(Graph,0,max_relax_count)))
        
    #Creating Result Graph
    print(number_of_nodes_array, dijkstra_array)
    plt.plot(number_of_nodes_array, dijkstra_array, label = "Dijkstra")
    plt.plot(number_of_nodes_array, dijkstra_approx_array, label = "Dijkstra Approx")
    plt.plot(number_of_nodes_array, bellman_ford_array, label = "Bellman Ford")
    plt.plot(number_of_nodes_array, bellman_ford_approx_array, label = "Bellman Ford Approx")
    plt.xlabel('Number of Edges')
    plt.ylabel('Total Distance')
    plt.title('Analysis on Dense vs Sparse Graphs')
    plt.legend()
    plt.show()
    
def experiment_suite2():
    #Create a complete graph of size 50
    #Run the Graph through each of the 4 Algorithms
    #In each loop the value of k (relaxation limit is adjusted) until max_k is reached
    #Result of total distance is plotted against number values of k
    number_of_nodes = 50
    max_k = 15
    k_array = []
    dijkstra_approx_array = []
    dijkstra_array = []
    bellman_ford_array = []
    bellman_ford_approx_array = []
    Graph =  create_random_complete_graph(number_of_nodes, 10)
    for k in range(2,max_k+1):
        k_array.append(k)
        #Distance for Dijkstra
        dijkstra_array.append(total_dist(dijkstra(Graph,0)))
        #Distance for Dijkstra Approx
        dijkstra_approx_array.append(total_dist(dijkstra_approx(Graph,0,k)))
        #Distance for Bellman Ford
        bellman_ford_array.append(total_dist(bellman_ford(Graph,0)))
        #Distance for Bellman Ford Approx
        bellman_ford_approx_array.append(total_dist(bellman_ford_approx(Graph,0,k)))
    #Creating Result Graph 1
    plt.plot(k_array, bellman_ford_array, label = "Bellman Ford")
    plt.plot(k_array, bellman_ford_approx_array, label = "Bellman Ford Approx")
    plt.xlabel('Max K(Relaxations) amount')
    plt.ylabel('Total Distance of Shortest Path Calculated')
    plt.title('Performance of Approx Algorithms with Changing Max Relexations')
    plt.legend()
    plt.show()
    #Creating Result Graph 2
    plt.plot(k_array, dijkstra_array, label = "Dijkstra")
    plt.plot(k_array, dijkstra_approx_array, label = "Dijkstra Approx")
    plt.xlabel('Max K(Relaxations) amount')
    plt.ylabel('Total Distance of Shortest Path Calculated')
    plt.title('Performance of Approx Algorithms with Changing Max Relexations')
    plt.legend()
    plt.show()

def experiment_suite3():
    #Experiment Summary:
    #Loop to generate a graphs that increase in size upto max_number_of_nodes
    #After each graph is generated it is run through each of the 4 algorithms
    #Total Distance vs number of nodes plotted
    max_number_of_nodes = 50
    max_relax_count = 1
    number_of_nodes_array = []
    dijkstra_approx_array = []
    dijkstra_array = []
    bellman_ford_array = []
    bellman_ford_approx_array = []
    for number_of_nodes in range(1,max_number_of_nodes+1):
        number_of_nodes_array.append(number_of_nodes)
        Graph = create_random_complete_graph(number_of_nodes, 10)
        #Distance for Dijkstra
        dijkstra_array.append(total_dist(dijkstra(Graph,0)))
        #Distance for Dijkstra Approx
        dijkstra_approx_array.append(total_dist(dijkstra_approx(Graph,0,max_relax_count)))
        #Distance for Bellman Ford
        bellman_ford_array.append(total_dist(bellman_ford(Graph,0)))
        #Distance for Bellman Ford Approx
        bellman_ford_approx_array.append(total_dist(bellman_ford_approx(Graph,0,max_relax_count)))
        
    #Creating Result Graph 1
    plt.plot(number_of_nodes_array, dijkstra_array, label = "Dijkstra")
    plt.plot(number_of_nodes_array, dijkstra_approx_array, label = "Dijkstra Approx")
    plt.xlabel('Number of Nodes')
    plt.ylabel('Total Distance of Shortest Path Calculated')
    plt.title('Analysis of the Algorithm Performance with Graph Size')
    plt.legend()
    plt.show()
    #Creating Result Graph 2
    plt.plot(number_of_nodes_array, bellman_ford_array, label = "Bellman Ford")
    plt.plot(number_of_nodes_array, bellman_ford_approx_array, label = "Bellman Ford Approx")
    plt.xlabel('Number of Nodes')
    plt.ylabel('Total Distance of Shortest Path Calculated')
    plt.title('Analysis of the Algorithm Performance with Graph Size')
    plt.legend()
    plt.show()
    
def mystery_algorithm_experiment():
    max_number_of_nodes = 50
    number_of_nodes_array = []
    mystery_array = []
    for number_of_nodes in range(1,max_number_of_nodes+1):
        number_of_nodes_array.append(number_of_nodes)
        Graph = create_random_complete_graph(number_of_nodes, 10)
        #Time for Mystery Algorithm
        start_time1 = time.time()
        mystery(Graph)
        end_time1 = time.time() 
        mystery_array.append(end_time1-start_time1)
        
    #Creating Result Graph
    log_x = np.log(number_of_nodes_array)
    log_y = np.log(mystery_array)
    slope =(log_x/log_y)
    #slope = Stats.linregress(log_x, log_y)
    #slope, intercept, r_value, p_value, std_err = linregress(log_x, log_y)
    print("SLOPE IS: ", slope)
    plt.loglog(number_of_nodes_array, mystery_array, label = "Mystery Algorithm")
    plt.xlabel('Number of Nodes')
    plt.ylabel('Time(s) Performance')
    plt.title('Logarithmic Performance of Mystery Algorithm')
    plt.legend()
    plt.show()
 
#------------------------------------------------------------EXPERIMENT RUNNER------------------------------------------------------------#       
print("EXPERIMENT RUNNER: ")
experiment_suite1()
#experiment_suite2()
#experiment_suite3()
#mystery_algorithm_experiment()