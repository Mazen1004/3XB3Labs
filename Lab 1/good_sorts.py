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

def create_random_list(length, max_value):
    print("test")
    return [random.randint(0, max_value) for _ in range(length)]

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

        plt.yticks(np.arange(min(heapSortOutput), max(heapSortOutput)+1, 0.25))

        plt.xlabel('List Length')
        # naming the y axis
        plt.ylabel('Time(s)')
        
        # giving a title to my graph
        plt.title('Variable List Length and Constant Swaps Experiment')

        # show a legend on the plot
        plt.legend()
        
        # function to show the plot
        plt.show()


# ============

experiment4(True)