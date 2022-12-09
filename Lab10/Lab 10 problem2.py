# Worst case running time is Θ(n * m) when two lists don't have a intersection.
# However, if two lists have a intersection, then running time is Θ(n + m)
# Thus, the function should run in Θ(n) average time.
def list_intersection(lst1, lst2):
    lst3 = []
    d1 = {}
    d2 = {}
    for item1 in lst1:
        d1[item1] = 1 
    for item2 in lst2:
        d2[item2] = 2
    for key, value in d2.items():
        if key in d1:
            lst3.append(key)
    return lst3
      
    

lst1 = [5,6,1,10]
lst2 = [8,1,9,5,3,8]

print(list_intersection(lst1,lst2))

'''
 
'''
