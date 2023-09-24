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
find_max_index(my_list,0,3)