import random

my_list = [11, 25, 12, 29, 64]


def create_random_list(length, max_value):
    print("test")
    return [random.randint(0, max_value) for _ in range(length)]

def find_max_index(L, n , upper_limit):
            max_index = n
            for i in range(n+1, min(upper_limit+1, len(L))):
                if L[i] > L[max_index]:
                    max_index = i
            print(max_index)
            return max_index
#find_max_index(my_list,0,3)

def swap(L, i, j):
    L[i], L[j] = L[j], L[i]

def bubble_sort(L):
    for i in range(len(L)):
        for j in range(len(L) - 1):
            if L[j] > L[j+1]:
                swap(L, j, j+1)
    

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
            
         


L = create_random_list(10, 25)
print("Original List:", L)
dualPivQuickSort(L,0,len(L) - 1)
print("Sorted List:", L)
