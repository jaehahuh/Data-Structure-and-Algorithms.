
lst = [1,3,5,7,9]
targetNum = 5


def searchArray(lst, targetNum):
    if targetNum < lst[0] or targetNum  > lst[-1]:
        return -1
    for ind in range(len(lst)):
        if lst[ind] == targetNum:
            return ind
    return -1

print(searchArray(lst,targetNum))




lst2 = [1,3,5,7,9]
targetNum2 = 1

def searchArray2(lst, targetNum):
    start = 0
    end = len(lst)
  
    while start < end:
        mid = (start + end) // 2
        if targetNum == lst[mid]:
            return mid
        elif targetNum < lst[mid]:
            end = mid
        else:
            start = mid + 1
    return mid

        



print(searchArray2(lst2,targetNum2))
