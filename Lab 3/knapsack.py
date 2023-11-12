from ast import List, Tuple
from itertools import chain, combinations
import random
import time
import matplotlib.pyplot as plt


def random_set_generator(set_length, min_weight, max_weight, min_profit, max_profit):
    items = []
    for _ in range(set_length):
        weight = random.randint(min_weight, max_weight)
        value = random.randint(min_profit, max_profit)
        items.append((weight, value))
        
    return items

    
def ks_brute_force(items, capacity):
    max_profit = 0
    print(items)
    #Generating all possible subsets
    powerset = list(chain.from_iterable(combinations(items, r) for r in range(1,len(items)+1)))
    #looping through subsets to find max profit while meeting capacity
    for subset in powerset:
        print(subset)
        weight = 0
        profit = 0
        for item in subset:
            weight += item[0]
            profit += item[1]
        #Conditions to be met as new max profit
        if weight <= capacity and profit > max_profit:
            max_profit = profit
        
    return max_profit

def ks_rec(items, capacity):
    if len(items) == 0 or capacity == 0:
        # base case, no more items to consider or no capacity left
        return 0

    # If the item is greater than max capacity, keep calulating without item
    if capacity < items[0][0]:
        return ks_rec(items[1:], capacity)
    else:
        profit1 = ks_rec(items[1:], capacity)
        profit2 = items[0][1] + ks_rec(items[1:], capacity - items[0][0]) 
        return max(profit1,profit2)
            
def ks_bottom_up1(items, capacity):
    #Creating array to define
    memo = []
    for _ in range(len(items)):
        memo.append([None] * (capacity + 1))
    
    

def ks_bottom_up(item_list, max_weight):
    print(item_list)
    N = len(item_list)
    memo = [[0 for _ in range(max_weight + 1)] for _ in range(N + 1)]
    print(memo)

    for i in range(1, N + 1):
        wi, vi = item_list[i - 1]
        for j in range(1, max_weight + 1):
            # take
            op1 = 0
            if j - wi >= 0:
                op1 = memo[i - 1][j - wi] + vi

            # don't take
            op2 = memo[i - 1][j]

            memo[i][j] = max(op1, op2)
    print(memo)
    return memo[N][max_weight]

def ks_top_down(items, capacity):
    #Creating array to define
    memo = []
    for _ in range(len(items)+1):
        memo.append([None] * (capacity + 1))
        
    #Initialize First Row and Column to 0
    for i in range(len(items)+1):
        memo[i][0] = 0
    for j in range(capacity + 1):
        memo[0][j] = 0
        
    def ks_top_down_recursive(i,j):
        nonlocal items, capacity, memo
        #Base Case for the recursion
        if i<=0 or j<=0:
            return 0
        
        # If the solution is already calculated return it from array memory
        if memo[i][j] != None:
            return memo[i][j]
        
       
        # If the item is greater than max capacity
        if j < items[i][0]:
            memo[i][j] = ks_top_down_recursive(i - 1, j)
        else:
            profit1 = ks_top_down_recursive(i - 1, j)
            profit2 = items[i][1] + ks_top_down_recursive(i - 1, j - items[i][0]) 
            memo[i][j] = max(profit1,profit2)
        #print("test")
        #print(memo)
        #print("break")
        #for row in memo: 
        #    print(row)
            
        return memo[i][j]

    #print("final")
    #for row in memo: 
    #    print(row)    
    return ks_top_down_recursive(len(items) - 1, capacity)


    
#items1 = random_set_generator(5,50,5)
#print(items)

items = [(1,1),(3,4),(4,5),(5,7)]
#print(ks_brute_force(items,7))
#print(ks_bottom_up(items,7))
#print(ks_top_down(items, 7))
#print(ks_rec(items, 7))

def exp1():
    list_size_array = []
    ks_brute_force_array = []
    ks_rec_array = []
    for list_size in range(15):
        list_size_array.append(list_size)
        items_list = random_set_generator(list_size, 50, 75, 1000, 2000)
        #Time for Brute Force
        start_time1 = time.time()
        ks_brute_force(items_list,200)
        end_time1 = time.time()
        execution_time_brute_force = end_time1 - start_time1
        ks_brute_force_array.append(execution_time_brute_force)
        #Time for Recursion
        start_time2 = time.time()
        ks_rec(items_list,200)
        end_time2 = time.time()
        execution_time_rec = end_time2 - start_time2
        ks_rec_array.append(execution_time_rec)
    print("List size ", list_size_array)
    print("Brute Force ", ks_brute_force_array)
    print("Recursion ", ks_rec_array)
    
    #Creating Result Graph
    plt.plot(list_size_array, ks_brute_force_array, label = "Knapsack Brute Force")
    plt.plot(list_size_array, ks_rec_array, label = "Knapsack Recursion")
    plt.xlabel('List Length')
    plt.ylabel('Time(s) Performance')
    plt.title('Experiment 1 Graph')
    plt.legend()
    plt.show()
    
exp1()