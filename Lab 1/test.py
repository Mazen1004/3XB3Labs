my_list = [11, 25, 12, 29, 64]
print(len(my_list))
print(my_list[1])

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
    
                
my_list1 = [11, 25, 12, 29, 64]

bubble_sort(my_list1)

print(my_list1)