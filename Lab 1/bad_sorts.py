"""
This file corresponds to the first graded lab of 2XC3.
Feel free to modify and/or add functions to this file.
"""
import random
import time
import matplotlib.pyplot as plt


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
    start_time = time.time()
    sort_function(list)
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

        #Running Insertion Sort
        print("INSERTION SORT TEST")
        a=measure_time(insertion_sort,list1)
        b=measure_time(insertion_sort,list2)
        c=measure_time(insertion_sort,list3)
        d=measure_time(insertion_sort,list4)

        y1= [a,b,c,d]
        # plotting the points 
        plt.plot(x, y1, label = "Insertion Sort")

        #Running Selection Sort
        print("SELECTION SORT TEST")
        e=measure_time(selection_sort,list1)
        f=measure_time(selection_sort,list2)
        g=measure_time(selection_sort,list3)
        h=measure_time(selection_sort,list4)

        y2= [e,f,g,h]
        # plotting the points 
        plt.plot(x, y2, label = "Selection Sort")
        
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
                #if max_index == last_unsorted_index:
                #    max_index = min_index
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
            #print(max_index)
            return max_index
        
        list1 = create_random_list(x[0],maxVal) #List Length is 5, maximum value in list is 100
        list2 = create_random_list(x[1],maxVal)
        list3 = create_random_list(x[2],maxVal)
        list4 = create_random_list(x[3],maxVal)
        
        #my_list = [25, 64, 12, 22, 11]
        #selection_sort2(list1)
        
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


run_experiment1(False)
run_experiment2(True)