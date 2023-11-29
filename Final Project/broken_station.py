L = [2, 4, 6, 7, 10, 14]
m = 2

def distance(L,n,m):
    if L[n] > L[m]:
        return L[n] - L[m]
    else:
        return L[m] - L[n]

def bsp_value(L, m):
    #Creating array to define
    bsp = []
    for _ in range(len(L)):
        bsp.append([float('inf')] * (m + 1))
        
    #Initializing First Row
    print(len(bsp))
    for i in range(1,len(bsp)):
        print("test loop")
        print(i)
        bsp[i][0] = distance(L,i,i-1)
        
    print(bsp)
    for row in bsp:
        print(' '.join(map(str, row)))
        
def bsp_value1(L, m):
    """
    Calculate the maximum value possible of the closest two numbers in L, after removing m numbers.
    """
    n = len(L)  # Number of stations
    DP = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    
    # Initialize the distances between adjacent stations
    distances = [L[i] - L[i - 1] for i in range(1, n)]
    
    # Base case initialization
    for i in range(1, n + 1):
        DP[i][0] = min(DP[i - 1][0], distances[i - 2] if i > 1 else float('inf'))
    
    # Fill the DP table using the recurrence relation
    for i in range(2, n + 1):
        for j in range(1, min(i, m + 1)):
            # Case 1: Keep the ith station, which does not change the minimum distance
            keep_station = DP[i - 1][j]
            # Case 2: Remove the ith station, which could potentially increase the minimum distance
            # We look at the gap that would be created by removing the current station.
            remove_station = DP[i - 2][j - 1]
            if i > 2 and j < i - 1:
                remove_station = max(remove_station, distances[i - 2])
            DP[i][j] = min(keep_station, remove_station)
    
    # Find the maximum minimum distance after m removals
    max_min_dist = 0
    for i in range(1, n + 1):
        max_min_dist = max(max_min_dist, DP[i][m])
    
    return max_min_dist

def bsp_value2(L, m):
    # Check if m is equal to or greater than the length of L
    if m >= len(L):
        return float('-inf')  # No valid minimum distance in this case

    # Base case: when m is 0, calculate the minimum distance between remaining stations
    if m == 0:
        min_distance = float('inf')
        for i in range(1, len(L)):
            min_distance = min(min_distance, L[i] - L[i-1])
        return min_distance

    # Recursive case: try removing each station and find the maximum of the minimum distances
    max_min_distance = float('-inf')
    for i in range(len(L)):
        new_L = L[:i] + L[i+1:]  # Create a new list without the chosen station
        current_distance = bsp_value2(new_L, m - 1)
        max_min_distance = max(max_min_distance, current_distance)

    return max_min_distance

def bsp_value_solution(L, m):
    # Base case: If no more stations are to be removed, return the current list and min distance
    if m == 0:
        if len(L) < 2:
            return float('-inf'), []  # Return negative infinity and empty list if not enough stations
        min_distance = float('inf')
        for i in range(1, len(L)):
            min_distance = min(min_distance, L[i] - L[i-1])
        return min_distance, L

    max_min_distance = float('-inf')
    best_combination = []

    # Try removing each station and find the best combination
    for i in range(len(L)):
        new_L = L[:i] + L[i+1:]  # Create a new list without the chosen station
        current_distance, current_combination = bsp_value_solution(new_L, m - 1)

        # Update the best combination if this one is better
        if current_distance > max_min_distance:
            max_min_distance = current_distance
            best_combination = current_combination

    return max_min_distance, best_combination

#print(bsp_value2(L,2))
print(bsp_value_solution(L,2))