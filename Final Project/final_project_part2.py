 
import heapq


def a_star(G, s, d, h):
   
    pred = {}
    dist = {}
    

    #heap storing the first node with a distance of 0
    priorityQueue = [(0,s)]
    heapq.heapify(priorityQueue)
    
    nodes = list(G.adj.keys())

    for node in nodes:
        dist[node] = float("inf")
    
    dist[s] = 0

    while len(priorityQueue) > 0:
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






