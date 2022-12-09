def threeSum(lst, targetSum):
    for i in lst:
        for j in lst:
            for k in lst:
                if i + j + k == targetSum:
                    return i, j, k

print(threeSum([1,2,4,6,9], 5))




#uneffiecient









#A = []
#num = int(input("Make a array with numbers if you want to stop then type number 0: "))
#while (num != 0):
    #A.append(num)
    #num = int(input("Make a array with numbers if you want to stop then type number 0: "))

#S = int(input("Type the sum")) 

#def func (A, S)
    #for i in range (len(A)):
        
