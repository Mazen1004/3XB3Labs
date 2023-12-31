"""
This file corresponds to the first graded lab of 2XC3.
Feel free to modify and/or add functions to this file.
"""
import random
import time
import matplotlib.pyplot as plt
import numpy as np

# Create a random list length "length" containing whole numbers between 0 and max_value inclusive
def create_random_list(length, max_value):
    print("test")
    return [random.randint(0, max_value) for _ in range(length)]


# Creates a near sorted list by creating a random list, sorting it, then doing a random number of swaps
def create_near_sorted_list(length, max_value, swaps):
    L = create_random_list(length, max_value)
    L.sort()
    for _ in range(swaps):
        r1 = random.randint(0, length - 1)
        r2 = random.randint(0, length - 1)
        swap(L, r1, r2)
    return L


# I have created this function to make the sorting algorithm code read easier
def swap(L, i, j):
    L[i], L[j] = L[j], L[i]


# ******************* Insertion sort code *******************

# This is the traditional implementation of Insertion Sort.
def insertion_sort(L):
  
    for i in range(1, len(L)):
        insert(L, i)


def insert(L, i):
    while i > 0:
        if L[i] < L[i-1]:
            swap(L, i-1, i)
            i -= 1
        else:
            return


# ******************* Bubble sort code *******************

# Traditional Bubble sort
def bubble_sort(L):
    for i in range(len(L)):
        for j in range(len(L) - 1):
            if L[j] > L[j+1]:
                swap(L, j, j+1)


# ******************* Selection sort code *******************

# Traditional Selection sort
def selection_sort(L):
    for i in range(len(L)):
        min_index = find_min_index(L, i)
        swap(L, i, min_index)


def find_min_index(L, n):
    min_index = n
    for i in range(n+1, len(L)):
        if L[i] < L[min_index]:
            min_index = i
    return min_index

#function to measure time taken for algorithm to run
def measure_time(sort_function,list):
    copy_list = list.copy()
    start_time = time.time()
    sort_function(copy_list)
    end_time = time.time()
    execution_time = end_time - start_time
    
    print(execution_time)
    return execution_time


# ******************* Experiment 1 *******************

def run_experiment1(run):
    if run:
        #Creating Lists of Different Lengths
        x = [5,50,500,5000] #array of the list lengths
        maxVal = 100 #max value of list length

        list1 = create_random_list(x[0],maxVal) #List Length is 5, maximum value in list is 100
        list2 = create_random_list(x[1],maxVal)
        list3 = create_random_list(x[2],maxVal)
        list4 = create_random_list(x[3],maxVal)

        #Running Selection Sort
        print("SELECTION SORT TEST")
        e=measure_time(selection_sort,list1)
        f=measure_time(selection_sort,list2)
        g=measure_time(selection_sort,list3)
        h=measure_time(selection_sort,list4)

        y2= [e,f,g,h]
        # plotting the points 
        plt.plot(x, y2, label = "Selection Sort")
        
        
        #Running Insertion Sort
        print("INSERTION SORT TEST")
        a=measure_time(insertion_sort,list1)
        b=measure_time(insertion_sort,list2)
        c=measure_time(insertion_sort,list3)
        d=measure_time(insertion_sort,list4)

        y1= [a,b,c,d]
        # plotting the points 
        plt.plot(x, y1, label = "Insertion Sort")

        
        #Running Bubble Sort
        print("BUBBLE SORT TEST")
        i=measure_time(bubble_sort,list1)
        j=measure_time(bubble_sort,list2)
        k=measure_time(bubble_sort,list3)
        l=measure_time(bubble_sort,list4)

        y3= [i,j,k,l]
        # plotting the points 
        plt.plot(x, y3, label = "Bubble Sort")

        # naming the x axis
        plt.xlabel('List Length')
        # naming the y axis
        plt.ylabel('Time(s)')
        
        # giving a title to my graph
        plt.title('Experiment 1 Graph')

        # show a legend on the plot
        plt.legend()
        
        # function to show the plot
        plt.show()


# ******************* Experiment 2 *******************

def run_experiment2(run):
    if run:
        def insertion_sort2(L):
            for i in range(1, len(L)):
                insert(L, i)


        def insert(L, i):
            current_element = L[i]
            j=i-1
            while j >= 0 and L[j] > current_element:
                L[j+1] = L[j]
                j = j-1
                
            L[j+1] = current_element
            
        #Creating Lists of Different Lengths
        x = [5,50,500,5000] #array of the list lengths
        maxVal = 100 #max value of list length

        list1 = create_random_list(x[0],maxVal) #List Length is 5, maximum value in list is 100
        list2 = create_random_list(x[1],maxVal)
        list3 = create_random_list(x[2],maxVal)
        list4 = create_random_list(x[3],maxVal)

        #Running Insertion Sort
        print("INSERTION SORT TEST")
        a=measure_time(insertion_sort,list1)
        b=measure_time(insertion_sort,list2)
        c=measure_time(insertion_sort,list3)
        d=measure_time(insertion_sort,list4)

        y1= [a,b,c,d]
        # plotting the points 
        plt.plot(x, y1, label = "Insertion Sort")
        
        print("INSERTION SORT 2 TEST")
        e=measure_time(insertion_sort2,list1)
        f=measure_time(insertion_sort2,list2)
        g=measure_time(insertion_sort2,list3)
        h=measure_time(insertion_sort2,list4)
        
        y2= [e,f,g,h]
        # plotting the points 
        plt.plot(x, y2, label = "Insertion Sort 2")
        
        # naming the x axis
        plt.xlabel('List Length')
        # naming the y axis
        plt.ylabel('Time(s)')
        
        # giving a title to my graph
        plt.title('Experiment 2 Graph')

        # show a legend on the plot
        plt.legend()
        
        # function to show the plot
        plt.show()
        
        def selection_sort2(L):
            last_unsorted_index = len(L)-1
            n = len(L)
            for i in range(n // 2):
                #print("Loop:")
                #print(i)
                min_index = find_min_index(L, i)
                
                swap(L, i, min_index)
                #print(L)
              
                last_unsorted_index = len(L) - i - 1
                max_index = find_max_index(L, i, last_unsorted_index)
                swap(L, last_unsorted_index, max_index)
                #print(L)
            #print(L)
          
 
        def find_min_index(L, n):
            min_index = n
            for i in range(n+1, len(L)):
                if L[i] < L[min_index]:
                    min_index = i
            return min_index
        def find_max_index(L, n , upper_limit):
            max_index = n
            for i in range(n+1, min(upper_limit+1, len(L))):
                if L[i] > L[max_index]:
                    max_index = i
            return max_index
        
        list1 = create_random_list(x[0],maxVal) #List Length is 5, maximum value in list is 100
        list2 = create_random_list(x[1],maxVal)
        list3 = create_random_list(x[2],maxVal)
        list4 = create_random_list(x[3],maxVal)
        
        
        #Running Selection Sort
        print("SELECTION SORT TEST")
        a=measure_time(selection_sort,list1)
        b=measure_time(selection_sort,list2)
        c=measure_time(selection_sort,list3)
        d=measure_time(selection_sort,list4)

        y1= [a,b,c,d]
        # plotting the points 
        plt.plot(x, y1, label = "Selection Sort")
        
        print("SELECTION SORT 2 TEST")
        e=measure_time(selection_sort2,list1)
        f=measure_time(selection_sort2,list2)
        g=measure_time(selection_sort2,list3)
        h=measure_time(selection_sort2,list4)
        
        y2= [e,f,g,h]
        # plotting the points 
        plt.plot(x, y2, label = "Selection Sort 2")
        
        # naming the x axis
        plt.xlabel('List Length')
        # naming the y axis
        plt.ylabel('Time(s)')
        
        # giving a title to my graph
        plt.title('Experiment 2 Graph')

        # show a legend on the plot
        plt.legend()
        
        # function to show the plot
        plt.show()
        
        def bubble_sort2(L):   
            for i in range(len(L)):
                for j in range(len(L) - 1, i, -1):
                    if L[j] < L[j - 1]:
                    # If the current element is smaller than the previous element,
                    # shift the previous element up
                        L[j], L[j - 1] = L[j - 1], L[j]
                        swapped = True
            return L
        
        list1 = create_random_list(x[0],maxVal) #List Length is 5, maximum value in list is 100
        list2 = create_random_list(x[1],maxVal)
        list3 = create_random_list(x[2],maxVal)
        list4 = create_random_list(x[3],maxVal)
        
        
        #Running Selection Sort
        print("BUBBLE SORT TEST")
        a=measure_time(bubble_sort,list1)
        b=measure_time(bubble_sort,list2)
        c=measure_time(bubble_sort,list3)
        d=measure_time(bubble_sort,list4)

        y1= [a,b,c,d]
        # plotting the points 
        plt.plot(x, y1, label = "Bubble Sort")
        
        print("BUBBLE SORT 2 TEST")
        e=measure_time(bubble_sort2,list1)
        f=measure_time(bubble_sort2,list2)
        g=measure_time(bubble_sort2,list3)
        h=measure_time(bubble_sort2,list4)
        
        y2= [e,f,g,h]
        # plotting the points 
        plt.plot(x, y2, label = "Bubble Sort 2")
        
        # naming the x axis
        plt.xlabel('List Length')
        # naming the y axis
        plt.ylabel('Time(s)')
        
        # giving a title to my graph
        plt.title('Experiment 2 Graph')

        # show a legend on the plot
        plt.legend()
        
        # function to show the plot
        plt.show()



# Experiment 3
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


def experiment3(run):
    #theoretically: swaps = n * log(n)/2

    if run:

        #constant swaps, list length increasing
        listLength = [10,100,1000,10000]

        constswaps = []
        constswaps.append(create_near_sorted_list(listLength[0],100,10))
        constswaps.append(create_near_sorted_list(listLength[1],100,10))
        constswaps.append(create_near_sorted_list(listLength[2],100,10))
        constswaps.append(create_near_sorted_list(listLength[3],100,10))

        insertionSortOutput = []
        bubbleSortOutput = []
        selectionSortOutput = []

        print("Variable List Length Tests")
        for testList in constswaps:
            print("Insertion Sort Test: ")
            insertionSortOutput.append(runTimeTimer(insertion_sort,testList)) 

            print("Bubble Sort Test: ")

            bubbleSortOutput.append(runTimeTimer(bubble_sort,testList))

            print("Selection Sort Test: ")
            selectionSortOutput.append(runTimeTimer(selection_sort,testList))
        
        #constant list size, increasing swap size
        listSwaps = [10,100,1000,10000]

        constList = []
        constList.append(create_near_sorted_list(10000,10000,listSwaps[0]))
        constList.append(create_near_sorted_list(10000,10000,listSwaps[1]))
        constList.append(create_near_sorted_list(10000,10000,listSwaps[2]))
        constList.append(create_near_sorted_list(10000,10000,listSwaps[3]))
        
        insertionSortOutput2 = []
        bubbleSortOutput2 = []
        selectionSortOutput2 = []

        print("Variable Swaps Tests")

        for testList in constList:
            print("Insertion Sort Test: ")
            insertionSortOutput2.append(runTimeTimer(insertion_sort,testList)) 

            print("Bubble Sort Test: ")
            bubbleSortOutput2.append(runTimeTimer(bubble_sort,testList))

            print("Selection Sort Test: ")
            selectionSortOutput2.append(runTimeTimer(selection_sort,testList))


        #Constant Swap size Plot
        plt.plot(listLength,insertionSortOutput,label = "Insertion Sort")
        plt.plot(listLength,bubbleSortOutput,label = "Bubble Sort")
        plt.plot(listLength,selectionSortOutput,label = "Selection Sort")

        # plt.yticks(np.arange(min(bubbleSortOutput), max(bubbleSortOutput)+1, 0.25))

        plt.xlabel('List Length')
        # naming the y axis
        plt.ylabel('Time(s)')
        
        # giving a title to my graph
        plt.title('Variable List Length and Constant Swaps Experiment')

        # show a legend on the plot
        plt.legend()
        
        # function to show the plot
        plt.show()


        #Constant List Length Plot
        plt.plot(listSwaps,insertionSortOutput2,label = "Insertion Sort")
        plt.plot(listSwaps,bubbleSortOutput2,label = "Bubble Sort")
        plt.plot(listSwaps,selectionSortOutput2,label = "Selection Sort")

        #plt.yticks(np.arange(0, max(bubbleSortOutput)+1, 1))

        plt.xlabel('Number of Swaps')
        # naming the y axis
        plt.ylabel('Time(s)')
        
        # giving a title to my graph
        plt.title('Variable Swaps and Constant List Length Experiment')

        # show a legend on the plot
        plt.legend()
        
        # function to show the plot
        plt.show()
        
def run_experiment8(run):
    #copying
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
    
    if run:
        #Creating Lists of Different Lengths
        x = [10,25,40,55] #array of the list lengths
        maxVal = 100 #max value of list length

        list1 = create_random_list(x[0],maxVal) #List Length is 5, maximum value in list is 100
        #list1=[1,2,4,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35]
        #list1 = [[5, 2, 8, 1, 9]]
        list2 = create_random_list(x[1],maxVal)
        list3 = create_random_list(x[2],maxVal)
        list4 = create_random_list(x[3],maxVal)

       
        
        print("MERGE SORT TEST")
        e=measure_time(mergesort,list1)
        f=measure_time(mergesort,list2)
        g=measure_time(mergesort,list3)
        h=measure_time(mergesort,list4)
        
        y2= [e,f,g,h]
        # plotting the points 
        plt.plot(x, y2, label = "Merge Sort")
        
        
        print("QUICK SORT TEST")
        i=measure_time(quicksort,list1)
        j=measure_time(quicksort,list2)
        k=measure_time(quicksort,list3)
        l=measure_time(quicksort,list4)
        
        y3= [i,j,k,l]
        # plotting the points 
        plt.plot(x, y3, label = "Quick Sort")
        
         #Running Insertion Sort
         
        print("INSERTION SORT TEST")
        a=measure_time(insertion_sort,list1)
        b=measure_time(insertion_sort,list2)
        c=measure_time(insertion_sort,list3)
        d=measure_time(insertion_sort,list4)

        y1= [a,b,c,d]
        # plotting the points 
        plt.plot(x, y1, label = "Insertion Sort")
        
        # naming the x axis
        plt.xlabel('List Length')
        # naming the y axis
        plt.ylabel('Time(s)')
        
        # giving a title to my graph
        plt.title('Experiment 2 Graph')

        # show a legend on the plot
        plt.legend()
        
        # function to show the plot
        plt.show()
        
        

# ******************* Run the Experiment *******************

run_experiment1(False)
run_experiment2(False)
experiment3(False)
run_experiment8(False)