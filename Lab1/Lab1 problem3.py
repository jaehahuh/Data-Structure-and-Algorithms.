'''
def mergeArray (lst1, lst2):
    sortedList = lst1 + lst2
    temp = int()
    for i in range (len(sortedList)):
        for j in range (len(sortedList)):
            if sortedList[i] < sortedList[j]:
                temp = sortedList[i]
                sortedList[i] = sortedList[j]
                sortedList[j] = temp
    return sortedList


print (mergeArray ([1,3,5,6], [1,2,3,4,7]))
'''
        



def merge (lst1, lst2):
        result = []
        ind1 = 0
        ind2 = 0
        while ind1 < len(lst1) and ind2 < len(lst2):
            if lst1[ind1] <= lst2[ind2]:
                result.append(lst1[ind1])
                ind1 += 1
            else:
                result.append(lst2[ind2])
                ind2 += 1
                
        while ind1 < len(lst1):
            result.append (lst1[ind1])
            ind1 += 1
            
        while ind2 < len(lst2):
            result.append (lst1[ind2])
            ind2 += 1
            
        return result


print (merge ([1,3,5,8,9], [1,2,3,4,7]))
