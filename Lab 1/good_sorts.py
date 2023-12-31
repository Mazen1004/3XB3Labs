"""
This file corresponds to the first graded lab of 2XC3.
Feel free to modify and/or add functions to this file.

In contains traditional implementations for:
1) Quick sort
2) Merge sort
3) Heap sort

Author: Vincent Maccio
"""
import random
import time
import matplotlib.pyplot as plt
import numpy as np
import sys 

sys.setrecursionlimit(1000000)

def swap(L, i, j):
    L[i], L[j] = L[j], L[i]


def create_random_list(length, max_value):
    print("test")
    return [random.randint(0, max_value) for _ in range(length)]

def create_near_sorted_list(length, max_value, swaps):
    L = create_random_list(length, max_value)
    L.sort()
    for _ in range(swaps):
        r1 = random.randint(0, length - 1)
        r2 = random.randint(0, length - 1)
        swap(L, r1, r2)
    return L

#function to measure time taken for algorithm to run
def measure_time(sort_function,list):
    copy_list = list.copy()
    start_time = time.time()
    sort_function(copy_list)
    end_time = time.time()
    execution_time = end_time - start_time
    
    print(execution_time)
    return execution_time


# ************ Quick Sort ************
def quicksort(L):
    copy = quicksort_copy(L)
    for i in range(len(L)):
        L[i] = copy[i]


def quicksort_copy(L):
    if len(L) < 2:
        return L
    pivot = L[0]
    left, right = [], []
    for num in L[1:]:
        if num < pivot:
            left.append(num)
        else:
            right.append(num)
    return quicksort_copy(left) + [pivot] + quicksort_copy(right)

# *************************************



#=================== dual piv quicksort ====================

def dualPivQuickSort(arr, low, high):
      
    if low < high:
          
    
        lp, rp = partition(arr, low, high)
        
        # recursively sort left arr
        dualPivQuickSort(arr, low, lp - 1)
    
        #middle
        dualPivQuickSort(arr, lp + 1, rp - 1)
        
        #right
        dualPivQuickSort(arr, rp + 1, high)
          
def partition(arr, low, high):
    

    #going to choose first element and last element as left and right pivots
    #left pivot must always be smaller than right pivot
    if arr[low] > arr[high]:
        arr[low], arr[high] = arr[high], arr[low]
          
    # p is the left pivot, and q is the right pivot.
    newLeftPiv = low + 1
    leftStarting = low + 1
    newRightPiv = high - 1 
    leftPivot  = arr[low]
    rightPivot = arr[high]
      
    while leftStarting <= newRightPiv:
          
        # If elements are less than the left pivot
        if arr[leftStarting] <leftPivot:
            arr[leftStarting], arr[newLeftPiv] = arr[newLeftPiv], arr[leftStarting]
            newLeftPiv += 1
              
        # If elements are greater than or equal 
        # to the right pivot
        elif arr[leftStarting] >= rightPivot:
            while arr[newRightPiv] > rightPivot and leftStarting < newRightPiv:
                newRightPiv -= 1
                  
            arr[leftStarting], arr[newRightPiv] = arr[newRightPiv], arr[leftStarting]
            newRightPiv -= 1
              
            if arr[leftStarting] < leftPivot:
                arr[leftStarting], arr[newLeftPiv] = arr[newLeftPiv], arr[leftStarting]
                newLeftPiv += 1
                  
        leftStarting += 1
          
    newLeftPiv -= 1
    newRightPiv += 1
      
    # Bring pivots to their appropriate positions.
    arr[low], arr[newLeftPiv] = arr[newLeftPiv], arr[low]
    arr[high], arr[newRightPiv] = arr[newRightPiv], arr[high]
      
    # Returning the indices of the pivots
    return newLeftPiv, newRightPiv
            

# ************ Merge Sort *************

def mergesort(L):
    if len(L) <= 1:
        return
    mid = len(L) // 2
    left, right = L[:mid], L[mid:]

    mergesort(left)
    mergesort(right)
    temp = merge(left, right)

    for i in range(len(temp)):
        L[i] = temp[i]


def merge(left, right):
    L = []
    i = j = 0

    while i < len(left) or j < len(right):
        if i >= len(left):
            L.append(right[j])
            j += 1
        elif j >= len(right):
            L.append(left[i])
            i += 1
        else:
            if left[i] <= right[j]:
                L.append(left[i])
                i += 1
            else:
                L.append(right[j])
                j += 1
    return L

# *************************************

# ************* Heap Sort *************

def heapsort(L):
    heap = Heap(L)
    for _ in range(len(L)):
        heap.extract_max()

class Heap:
    length = 0
    data = []

    def __init__(self, L):
        self.data = L
        self.length = len(L)
        self.build_heap()

    def build_heap(self):
        for i in range(self.length // 2 - 1, -1, -1):
            self.heapify(i)

    def heapify(self, i):
        largest_known = i
        if self.left(i) < self.length and self.data[self.left(i)] > self.data[i]:
            largest_known = self.left(i)
        if self.right(i) < self.length and self.data[self.right(i)] > self.data[largest_known]:
            largest_known = self.right(i)
        if largest_known != i:
            self.data[i], self.data[largest_known] = self.data[largest_known], self.data[i]
            self.heapify(largest_known)

    def insert(self, value):
        if len(self.data) == self.length:
            self.data.append(value)
        else:
            self.data[self.length] = value
        self.length += 1
        self.bubble_up(self.length - 1)

    def insert_values(self, L):
        for num in L:
            self.insert(num)

    def bubble_up(self, i):
        while i > 0 and self.data[i] > self.data[self.parent(i)]:
            self.data[i], self.data[self.parent(i)] = self.data[self.parent(i)], self.data[i]
            i = self.parent(i)

    def extract_max(self):
        self.data[0], self.data[self.length - 1] = self.data[self.length - 1], self.data[0]
        max_value = self.data[self.length - 1]
        self.length -= 1
        self.heapify(0)
        return max_value

    def left(self, i):
        return 2 * (i + 1) - 1

    def right(self, i):
        return 2 * (i + 1)

    def parent(self, i):
        return (i + 1) // 2 - 1

    def __str__(self):
        height = math.ceil(math.log(self.length + 1, 2))
        whitespace = 2 ** height
        s = ""
        for i in range(height):
            for j in range(2 ** i - 1, min(2 ** (i + 1) - 1, self.length)):
                s += " " * whitespace
                s += str(self.data[j]) + " "
            s += "\n"
            whitespace = whitespace // 2
        return s

# *************************************

def runTimeTimer(sortingAlgo,nearSortList):
    
    copyNearSort = nearSortList.copy()
    start_time = time.time()
    
    # Call the sorting algorithm on the nearSortList
    sortingAlgo(copyNearSort)

    # Record the end time
    end_time = time.time()

    # Calculate the runtime
    runtime = end_time - start_time

    # Return the sorted list and the runtime
    print(runtime)
    return runtime

def experiment4(run):
    if run:
        listLength = [10,100,1000,10000]

        quickSortOutput = []
        mergeSortOutput = []
        heapSortOutput = []

        for length in listLength:

            nearSortList = create_random_list(length, 1000)  # Adjust the parameters as needed
            quick_sort_runtime = runTimeTimer(quicksort, nearSortList)
            merge_sort_runtime = runTimeTimer(mergesort, nearSortList)
            heap_sort_runtime = runTimeTimer(heapsort, nearSortList)

            quickSortOutput.append(quick_sort_runtime)
            mergeSortOutput.append(merge_sort_runtime)
            heapSortOutput.append(heap_sort_runtime)


        plt.plot(listLength,quickSortOutput,label = "Quick Sort")
        plt.plot(listLength,mergeSortOutput,label = "Merge Sort")
        plt.plot(listLength,heapSortOutput,label = "Heap Sort")

        # plt.yticks(np.arange(min(heapSortOutput), max(heapSortOutput)+1, 0.25))

        plt.xlabel('List Length')
        # naming the y axis
        plt.ylabel('Time(s)')
        
        # giving a title to my graph
        plt.title('Variable List Length and Constant Swaps Experiment')

        # show a legend on the plot
        plt.legend()
        
        # function to show the plot
        plt.show()


def experiment5(run):

    if run:
        numSwaps = [100000,10000,1000,100]

        quickSortOutput = []
        mergeSortOutput = []
        heapSortOutput = []

        for swaps in numSwaps:
            nearSortList = create_near_sorted_list(100000,100000,swaps)

            quick_sort_runtime = runTimeTimer(quicksort, nearSortList)
            merge_sort_runtime = runTimeTimer(mergesort, nearSortList)
            heap_sort_runtime = runTimeTimer(heapsort, nearSortList)

            quickSortOutput.append(quick_sort_runtime)
            mergeSortOutput.append(merge_sort_runtime)
            heapSortOutput.append(heap_sort_runtime)

        plt.plot(numSwaps,quickSortOutput,label = "Quick Sort")
        plt.plot(numSwaps,mergeSortOutput,label = "Merge Sort")
        plt.plot(numSwaps,heapSortOutput,label = "Heap Sort")

        plt.yticks(np.arange(min(mergeSortOutput), max(quickSortOutput)+1, 1))

        plt.xlabel('Number of Swaps')
        # naming the y axis
        plt.ylabel('Time(s)')
        
        # giving a title to my graph
        plt.title('Variable Swaps and Constant List Length')

        # show a legend on the plot
        plt.legend()
        
        # function to show the plot
        plt.show()


def dualPivRunTimeCalculator(arr,length):
    copy = arr.copy()
    start_time = time.time()
    
    # Call the sorting algorithm on the nearSortList
    dualPivQuickSort(copy,0,length)

    # Record the end time
    end_time = time.time()

    # Calculate the runtime
    runtime = end_time - start_time

    # Return the sorted list and the runtime
    print(runtime)
    return runtime


def experiment6(run):
    if run:
        listLength = [100,1000,10000,100000]

        

        quickSortOutput = []
        dualQuickSortOutput = []

        for lengths in listLength:
            randomList=  create_random_list(lengths,100000)
        
            quick_sort_runtime = runTimeTimer(quicksort, randomList)
            dualPivQuickSortRuntime = dualPivRunTimeCalculator(randomList,len(randomList)-1)

            quickSortOutput.append(quick_sort_runtime)
            dualQuickSortOutput.append(dualPivQuickSortRuntime)

        plt.plot(listLength,quickSortOutput,label = "Quick Sort")
        plt.plot(listLength,dualQuickSortOutput,label = "Dual Pivot Quick Sort")
        

        #plt.yticks(np.arange(min(quickSortOutput), max(dualQuickSortOutput)+1, 0.025))

        plt.xlabel('List Length')
        # naming the y axis
        plt.ylabel('Time(s)')
        
        # giving a title to my graph
        plt.title('Quick Sort vs Dual Pivot Quick Sort')

        # show a legend on the plot
        plt.legend()
        
        # function to show the plot
        plt.show()





def experiment7(run):
    def bottom_up_mergesort(arr):
        n = len(arr)
        width = 1

        while width < n:
            for i in range(0, n, 2 * width):
                left = arr[i:i + width]
                right = arr[i + width:i + 2 * width]
                merged = merge(left, right)
                arr[i:i + 2 * width] = merged

            width *= 2
            
    if run:
        #Creating Lists of Different Lengths
        x = [10,100,1000,10000] #array of the list lengths
        maxVal = 100 #max value of list length

        list1 = create_random_list(x[0],maxVal) 
        list2 = create_random_list(x[1],maxVal)
        list3 = create_random_list(x[2],maxVal)
        list4 = create_random_list(x[3],maxVal)
        
        
        
        print("MERGE SORT TEST")
        e=measure_time(mergesort,list1)
        f=measure_time(mergesort,list2)
        g=measure_time(mergesort,list3)
        h=measure_time(mergesort,list4)
        
        y2= [e,f,g,h]
        
        plt.plot(x, y2, label = "Merge Sort")
        
        print("INSERTION SORT TEST")
        a=measure_time(bottom_up_mergesort,list1)
        b=measure_time(bottom_up_mergesort,list2)
        c=measure_time(bottom_up_mergesort,list3)
        d=measure_time(bottom_up_mergesort,list4)

        y1= [a,b,c,d]
        # plotting the points 
        plt.plot(x, y1, label = "Bottom Up Merge Sort")
        
        # naming the x axis
        plt.xlabel('List Length')
        # naming the y axis
        plt.ylabel('Time(s)')
        
        # giving a title to my graph
        plt.title('Experiment 7 Graph')

        # show a legend on the plot
        plt.legend()
        
        # function to show the plot
        plt.show()
# ============

experiment4(False)
experiment5(False)
experiment6(False)
experiment7(False)
