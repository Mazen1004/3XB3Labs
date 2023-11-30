L = [2, 4, 6, 7, 10, 14]
m = 2

def bsp_value(L, m):
    #Check if m is equal to or greater than the length of L
    if m >= len(L):
        return "Invalid m input, m must be less than list length" 

    #Base case used in recursion when m is 0, calculate the minimum distance between remaining stations
    if m == 0:
        min_distance = float('inf')
        for i in range(1, len(L)):
            min_distance = min(min_distance, L[i] - L[i-1])
        return min_distance

    #Recursive case: try removing each station and find the maximum of the minimum distances
    max_min_distance = float('-inf')
    for i in range(len(L)):
        #Creating new list with length value
        new_L = L[:i] + L[i+1:] 
        #Recursion call 
        current_distance = bsp_value(new_L, m - 1)
        print("current distance is: ", current_distance)
        #Checking if new Max Min Distance is found
        max_min_distance = max(max_min_distance, current_distance)

    return max_min_distance

def bsp_value_solution(L, m):
    #Check if m is equal to or greater than the length of L
    if m >= len(L):
        return "Invalid m input, m must be less than list length" 
    #Base case used in recursion when m is 0, calculate the minimum distance between remaining stations
    if m == 0:
        min_distance = float('inf')
        for i in range(1, len(L)):
            min_distance = min(min_distance, L[i] - L[i-1])
        return min_distance, L

    max_min_distance = float('-inf')
    #Array to store best combination of numbers
    best_combination = []

    #Recursive case: Try removing each station and find the best combination
    for i in range(len(L)):
        new_L = L[:i] + L[i+1:]  # Create a new list without the chosen station
        current_distance, current_combination = bsp_value_solution(new_L, m - 1)

        # Update the best combination if this one is better
        if current_distance > max_min_distance:
            max_min_distance = current_distance
            best_combination = current_combination

    return max_min_distance, best_combination

#print(bsp_value(L,2))
#print(bsp_value_solution(L,2))