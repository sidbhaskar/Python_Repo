def swap (lst , a , b) :
    lst[a] , lst[b] = lst[b] , lst[a]
    return lst

lst = [10,200,30,40,50]
print(swap(lst, 2 ,3 ))

lst.sort()
print(lst,lst[-2])