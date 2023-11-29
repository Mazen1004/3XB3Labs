import timeit
from final_project_part2 import a_star 
import csv
from final_project_part1 import DirectedWeightedGraph
import numpy
import time

import matplotlib.pyplot as plt
from final_project_part1 import dijkstra as dijkAlgo
#the edge weights are the times found in london_connections
#the heuristic weight is the euclidean distance calculated from longitude and latitude found in london_stations





def readStationfile(file_path):
    data = {}
    with open(file_path, 'r') as csvfile:
        # Create a CSV reader object
        csv_reader = csv.DictReader(csvfile)
        
        
        # Iterate over each row in the CSV file
        #idCount = 1
        for row in csv_reader:
            data[int(row["id"])] = row

    return data

def readConnectionFile(file_path):
    data = {}


    #store 2d array as value with connections being first element, 2nd element is the time array, key is station id, 
    with open(file_path, 'r') as csvfile:

        csv_reader = csv.DictReader(csvfile)

        for row in csv_reader:
            if int(row["station1"]) in data.keys():
               connectionArr = data[int(row['station1'])][0]
               timeArr = data[int(row['station1'])][1]

               connectionArr.append(int(row['station2']))
               timeArr.append(int(row["time"]))

            else:
               data.update({int(row["station1"]):[[int(row["station2"])],[int(row["time"])]]})
        
    return data



londonStationHash = readStationfile("../Final Project/part3/london_stations.csv")
londonConnHash = readConnectionFile("../Final Project/part3/london_connections.csv")
#print(londonStationHash[11])

#use pythagorean theorem to solve distance between end node and every other node
def heurisiticWeighting(end,londonStatHash): #will create a dictionary that stores the distance of every node from the end node, note start is not the source node it is the node that we want the euclidean distance from the end node
    heuristic = {}

    #print(f"calculating euclidiean distance from {end} to every other node")

    #takes in target station, calculates euclidean distance between sink and every other station
    lat1 = float(londonStatHash[end]["latitude"])
    lon1 = float(londonStatHash[end]["longitude"])

    for station in londonStatHash.keys():
        
        lat2 = float(londonStatHash[station]["latitude"])
        lon2 = float(londonStatHash[station]["longitude"])

        distance = numpy.arccos(numpy.sin(lat1)*numpy.sin(lat2)+numpy.cos(lat1)*numpy.cos(lat2)*numpy.cos(lon2-lon1))*6371

        #approximate distance
        heuristic[station] = numpy.floor(distance) #rounded distance down

    return heuristic 

#h = heurisiticWeighting(278,londonStationHash)

#print(londonConnHash[96])

#something wrong with graph
#make it bidirectional, connections are bidirectional (undirected)
def createLondonStationGraph(londonStatHash,londonConnHash):
    stationGraph = DirectedWeightedGraph()
    
    for key in londonStatHash.keys():
        stationGraph.add_node(key)
        
    for station in stationGraph.adj.keys():
        if station in londonConnHash.keys():
            for i in range(len(londonConnHash[station][0])):
                stationGraph.add_edge(station,londonConnHash[station][0][i],londonConnHash[station][1][i])
                stationGraph.add_edge(londonConnHash[station][0][i],station,londonConnHash[station][1][i])


    
    return stationGraph

stationGraph = createLondonStationGraph(londonStationHash,londonConnHash)
print(stationGraph.adj[11])
#print(stationGraph.adj[26])

def callAstar(G,s,d,londonStationHash):
    
    h = heurisiticWeighting(d,londonStationHash)
    
    start_time1 = timeit.default_timer()
    pred,path = a_star(G,s,d,h)
    end_time1 = timeit.default_timer() 

    execution_time = end_time1 - start_time1
    
    #print(pred)
    #print(path)

    return execution_time

callAstar(stationGraph,1,200,londonStationHash)

def callDjikstra(G,s):
    
    startTime = timeit.default_timer()
    dist = dijkAlgo(G,s)
    endTime = timeit.default_timer()

    execution_time = endTime - startTime

    return execution_time


#print("A:", callAstar(stationGraph,11,278,londonStationHash))
#print("D:", callDjikstra(stationGraph,1))


#do another test without dividing
#make graph be the sum of time for each station APSP problem using both Djikstra and A* vs number of trials
def experiment2Suite(londonStationGraph,londonStatHash):
    
    Aexecutiontimes = []
    DexecutionTimes = []
    orderedStations = list(londonStatHash.keys())
    orderedStations.sort()


    for station1 in orderedStations:
        a_starExeTime = 0

        print(station1)

        aruns = 0
        for station2 in orderedStations:
            if station1 != station2:
                runTime = callAstar(londonStationGraph,station1,station2,londonStatHash)
                aruns += 1
                a_starExeTime += runTime

        #average time it takes to get a shortest path because we are doing trials over times run (effectively)
        #A star executiom time is probably greater because it iterates through pred dictionary and forms a path
        Aexecutiontimes.append(a_starExeTime/aruns)
        
        print(f"APSP A* execution time beginning at {station1} is: {a_starExeTime/(len(londonStatHash)*(len(londonStatHash) - 1))}")

        #djiksta is getting shortest path globally, A* getting 1 shortest path, but the time it takes A* to get a single shortest path, is smaller than the time it takes to run Djikstra normally
        #but because we are getting every pairs shortest path, djikstra is faster, but if we try to get the
        #djikstra ends up being faster but because we run A* (N*N-1) times 
        
        #Djikstra gets every shortest path from source node, but A* only gets 1 shortest path to some other node, so we have to do every pair from source to destination to get all pairs from source node
        #the fair test, how long it takes to get all pairs from node 1 but if we are interested in only getting the average time to create a path from node 1, then we should do all  pairs from node 1/source node divided by the number of possible pairs to get the average amount of time it takes to get all shortest paths from the source node to every other node
        dRunTime = callDjikstra(londonStationGraph,station1)
        DexecutionTimes.append(dRunTime)

        print(f"APSP Djikstra Execution time beginning at {station1} is: {dRunTime}")


    plt.plot(orderedStations,Aexecutiontimes,label="AStar")
    plt.plot(orderedStations,DexecutionTimes,label="Djikstra")

    plt.xlabel('Station ID')
    plt.ylabel('Runtime')
    plt.title("A* vs Djikstra Runtimes All Pair Shortest Path")

    plt.legend()
    plt.show()


#print(callAstar(stationGraph,26,260,londonStationHash))

experiment2Suite(stationGraph,londonStationHash)