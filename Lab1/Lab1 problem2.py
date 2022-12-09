def subArraySum(lst, targetSum):
    for start in range (len(lst)):
        for stop in range (start + 1, len(lst)+1):
            currSum = 0
            for num in lst [start : stop]:
                currSum += num
            if currSum == targetSum:
                return lst[start : stop]
        


print(subArraySum([3,1,7,-2,4], 6))
