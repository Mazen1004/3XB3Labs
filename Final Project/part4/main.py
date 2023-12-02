from graph import WeightedGraph, HeuristicGraph
from short_path_finder import ShortPathFinder
from spalgorithm import Dijkstra, Bellman_Ford, A_Star

# Example usage:
if __name__ == "__main__":
    graph = HeuristicGraph()
    # Populate the graph with nodes and edges

    path_finder = ShortPathFinder()
    path_finder.set_graph(graph)
    
    # Choose the algorithm
    algorithm = Dijkstra()  # or Bellman_Ford(), A_Star()
    path_finder.set_algorithm(algorithm)
    
    # Calculate the shortest path
    source = 0  # starting node
    dest = 5  # ending node
    path_cost = path_finder.calc_short_path(source, dest)
    print("The cost of the shortest path is: {path_cost}")