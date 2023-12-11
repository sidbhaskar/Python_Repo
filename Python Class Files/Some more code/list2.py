list1 = [1, 2, 3]
list2 = [3, 1, 4]

o=[]

for i in list1 :
    for j in list2 :
        if i != j:
            o.append((i,j))
print(o)