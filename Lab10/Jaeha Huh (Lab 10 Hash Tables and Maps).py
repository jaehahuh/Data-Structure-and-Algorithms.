#Problem 2
'''
Worst case running time is Θ(n * m) when two lists don't have a intersection.
However, if two lists have a intersection, then running time is Θ(n + m)
Thus, the function should run in Θ(n) average time.
'''
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
      
#Problem 3
def mode_of_list(lst):
    d = {}
    for num in lst:
        if not num in d:
            d[num]=1
        else:
            d[num]+=1
    for key,value in d.items():
        if value == max(d.values()):
            return key

        
#Problem 4
def two_sum(lst, target):
    d = {item: key for key, item in enumerate(lst)}

    for key, item in enumerate(lst):
        remain = target - item
        if remain in d:
            return (key, d[remain])

    return (None,None)



#Problem 5
def is_anagram(str1, str2):
    if len(str1) != len(str2):
        return False
    str1 = sorted(str1)
    str2 = sorted(str2)
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            return False
    return True

#sorted function runtime (O(N*log N))


#Test codes
def main():
    #Problem 2
    print("problem 2:")
    lst1 = [5,6,1,10]
    lst2 = [8,1,9,5,3,8]
    print(list_intersection(lst1,lst2))

    #Problem 3
    print("problem 3:")
    lst = [1,3,2,1,2,1]
    print  (mode_of_list(lst))

    #Problem 4
    print("problem 4:")
    print (two_sum([-5, 2, 8, -3, 7, 1], -1))
    
    #Problem 5
    print("problem 5:")
    str1 = "enraged"
    str2 = "angered"
    print(is_anagram(str1, str2))

main()
