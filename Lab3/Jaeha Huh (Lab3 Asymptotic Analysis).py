def first1(lst):
    left = 0
    right = len(lst) - 1
    found = False
    ind = None
    while ((found == False) and (left <= right)):
        mid = (left + right) // 2
        if (lst[mid] == 1 and lst[mid - 1] == 0):
            ind = mid
            found = True
        elif (lst[mid] == 1 and lst[mid - 1] == 1):
            right = mid - 1
        else:
            left = mid + 1
    return ind





def e_approxmation(n):
    total = 1
    num = 1
    for i in range (1,n+1):
        num *= i
        total += 1/num
    return total





def two_sum(sorted_lst, target):
    left = 0
    right = len(sorted_lst)-1
    while left < right:
        if sorted_lst [left] + sorted_lst[right] == target:
            return (left,right)
        elif sorted_lst[left] + sorted_lst[right] < target:
            left += 1
        elif sorted_lst[left] + sorted_lst[right] > target:
            right -= 1





def split_neg_pos(lst):
    left = 0
    right = len(lst)-1
    while left < right:
        if lst[left] > 0 and lst[right] < 0:
            lst[left], lst[right] = lst[right], lst[left]
            left += 1
            right -= 1
        elif lst[left] < 0 and lst[right] < 0:
            left += 1
        elif lst[left] > 0 and lst[right] > 0:
            right -= 1
        else:
            left += 1
            right -= 1
    return lst





def move_zeros(lst):
    index1 = 0
    index2 = 0
    while index1 < len(lst):
        if lst[index1] != 0:
            if index2 != index1:
                lst[index2] = lst[index1]
                lst[index1] = 0
            index2 += 1
        index1 += 1
    return lst





def find_min(lst):
    if len(lst) == 1:
            return lst[0]
    else:
        if find_min(lst[1:]) < lst[0]:
            lst[0] = find_min(lst[1:])
        return lst[0]





def main():
    print (first1([0,0,0,0,1,1]))
    print (e_approxmation(5))
    sorted_lst = [-3,-2,0,5,7]
    target = 2
    print (two_sum(sorted_lst, target))
    print (split_neg_pos([-7,5,-3,4,2]))
    print (move_zeros([1,0,2,0,0,3,4]))
    my_lst = [5,-1,9,6,0]
    print (find_min(my_lst))


main()
