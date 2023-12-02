import heapq
from graph import Graph
import min_heap2
class SPAlgorithm:
    def calc_sp(self, graph: Graph, source: int, dest: int):
        pass

class Dijkstra(SPAlgorithm):
    def calc_sp(self, graph: Graph, source: int, dest: int) -> float:
        pred = {}  # Predecessor dictionary
        dist = {}  # Distance dictionary
        Q = min_heap2.MinHeap([])
        nodes = list(graph.adj.keys())

        # Initialize priority queue/heap and distances
        for node in nodes:
            Q.insert(min_heap2.Element(node, float("inf")))
            dist[node] = float("inf")
        Q.decrease_key(source, 0)

        # Main loop of the algorithm
        while not Q.is_empty():
            current_element = Q.extract_min()
            current_node = current_element.value
            dist[current_node] = current_element.key
            # Looping through all the neighbors of extracted element
            for neighbour in graph.adj[current_node]:
                if dist[current_node] + graph.w(current_node, neighbour) < dist[neighbour]:
                    Q.decrease_key(neighbour, dist[current_node] + graph.w(current_node, neighbour))
                    dist[neighbour] = dist[current_node] + graph.w(current_node, neighbour)
                    pred[neighbour] = current_node

        # Reconstruct the shortest path from source to destination
        path = []
        current = dest
        while current != source:
            path.append(current)
            current = pred[current]
        path.append(source)
        path.reverse()  # Reverse the path to start from the source

        return dist[dest], path  # Return the distance and the path


class Bellman_Ford(SPAlgorithm):
    def calc_sp(self, graph: Graph, source: int, dest: int) -> float:
        # Implement Bellman-Ford algorithm here
        pred = {}  # Predecessor dictionary
        dist = {}  # Distance dictionary
        nodes = list(graph.adj.keys())

        # Initialize distances
        for node in nodes:
            dist[node] = float("inf")
        dist[source] = 0

        # Relax edges repeatedly
        for _ in range(graph.number_of_nodes()):
            for node in nodes:
                for neighbour in graph.adj[node]:
                    if dist[neighbour] > dist[node] + graph.w(node, neighbour):
                        dist[neighbour] = dist[node] + graph.w(node, neighbour)
                        pred[neighbour] = node

        # Reconstruct the shortest path from source to destination
        path = []
        current = dest
        while current != source:
            path.append(current)
            current = pred.get(current, None)
            if current is None:  # No path found
                return float("inf"), []
        path.append(source)
        path.reverse()  # Reverse to get the path from source to destination

        return dist[dest], path  # Return the distance and the path


class A_Star(SPAlgorithm):
    def calc_sp(self, graph: Graph, source: int, dest: int) -> float:
        
        # Implement A* algorithm here
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
        
        heuristic = graph.get_heuristic()
        return a_star(graph, source, dest, heuristic)     