from ast import List, Tuple
from itertools import chain, combinations
import random


def random_set_generator(set_length, max_weight, max_profit):
    items = []
    for _ in range(set_length):
        weight = random.randint(1, max_weight)
        value = random.randint(1, max_profit)
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
    return

def ks_bottom_up(items, capacity):
    return

def ks_top_down(items, capacity):
    return

items = random_set_generator(5,50,5)

print(ks_brute_force(items,100))
