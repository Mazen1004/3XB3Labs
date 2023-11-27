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


def createLondonStationGraph(londonStatHash,londonConnHash):
    stationGraph = DirectedWeightedGraph()
    
    for key in londonStatHash.keys():
        stationGraph.add_node(key)
        
    for station in stationGraph.adj.keys():
        if station in londonConnHash.keys():
            for i in range(len(londonConnHash[station][0])):
                stationGraph.add_edge(station,londonConnHash[station][0][i],londonConnHash[station][1][i])
            


    
    return stationGraph

stationGraph = createLondonStationGraph(londonStationHash,londonConnHash)

print(stationGraph.adj[26])

def callAstar(G,s,d,londonStationHash):
    
    h = heurisiticWeighting(d,londonStationHash)
    
    start_time1 = time.time()
    pred,path = a_star(G,s,d,h)
    end_time1 = time.time() 

    execution_time = end_time1 - start_time1
    
    print(pred)
    print(path)

    return execution_time

def callDjikstra(G,s):
    
    startTime = time.time()
    dist = dijkAlgo(G,s)
    endTime = time.time()

    execution_time = endTime - startTime

    return execution_time


# print(callAstar(stationGraph,11,278,londonStationHash))
# print(callDjikstra(stationGraph,11))




def experiment2Suite(londonStationGraph,londonStatHash):
    
    Aexecutiontimes = []
    DexecutionTimes = []
    orderedStations = list(londonStatHash.keys())
    orderedStations.sort()


    for station1 in orderedStations:
        a_starExeTime = 0

        print(station1)

        for station2 in orderedStations:
            if station1 != station2:
                runTime = callAstar(londonStationGraph,station1,station2,londonStatHash)
                a_starExeTime += runTime
        
        #A star executiom time is probably greater because it iterates through pred dictionary and forms a path
        Aexecutiontimes.append(a_starExeTime)
        
        print(f"APSP A* execution time beginning at {station1} is: {a_starExeTime}")


        dRunTime = callDjikstra(londonStationGraph,station1)
        DexecutionTimes.append(dRunTime)

        print(f"APSP Djikstra Execution time beginning at {station1} is: {dRunTime}")


    plt.plot(londonStatHash.keys(),Aexecutiontimes,label="AStar")
    plt.plot(londonStatHash.keys(),DexecutionTimes,label="Djikstra")

    plt.xlabel('Station ID')
    plt.ylabel('Runtime')
    plt.title("A* vs Djikstra Runtimes All Pair Shortest Path")

    plt.legend()
    plt.show()


#print(callAstar(stationGraph,26,260,londonStationHash))

#experiment2Suite(stationGraph,londonStationHash)