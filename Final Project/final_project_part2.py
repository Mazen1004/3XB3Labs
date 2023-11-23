 
import heapq
import min_heap

def a_star(G, s, d, h):
   
    pred = {}
    dist = {}
    

    #heap storing the first node with a distance of 0
    priorityQueue = [(0,s)]

    nodes = list(G.adj.keys())

    for node in nodes:
        dist[node] = float("inf")
    
    

    while priorityQueue:
        currentVal, currentNode = heapq.heappop(priorityQueue)

        if currentNode == d:
            path = [] #stores path from start to end 

            while currentNode in pred:
                path.insert(0,currentNode) #insert at start of list (basically appending to the start of the list)
                currentNode = pred[currentNode] #current node is equal to the predecessor of the itself
            
            path.insert(0,s)
            
            return pred,path

        for neighbour in G.adjacent_nodes(currentNode):
            distance = dist[currentNode] + G.w(currentNode,neighbour)

            if distance < dist[neighbour]:

                dist[neighbour] = distance

                combinedWeight = distance + h[neighbour]

                #insert with given priority into priority queue based on heuristic and distance from start

                heapq.heappush(priorityQueue,(combinedWeight,neighbour))

                pred[neighbour] = currentNode
    
    #no path exists between start and end node

    return None, None

            


def dijkstra(G, source):
    pred = {} #Predecessor dictionary. Isn't returned, but here for your understanding
    dist = {} #Distance dictionary
    Q = min_heap.MinHeap([])
    nodes = list(G.adj.keys())

    #Initialize priority queue/heap and distances
    for node in nodes:
        Q.insert(min_heap.Element(node, float("inf")))
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
