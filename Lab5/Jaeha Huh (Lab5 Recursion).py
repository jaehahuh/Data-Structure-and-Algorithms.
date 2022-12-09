def binary_search(lst, val, low,high):
    mid = (low + high)//2
    if val == lst[mid]:
        return mid
    elif val < lst[mid]:
        return binary_search(lst,val,low, mid-1)
    else:
        return binary_search(lst,val, mid+1, high)






def nested_list_sum(lst):
    total = 0
    for elem in lst:
        if isinstance(elem, list):
            total += nested_list_sum(elem)
        else:
            total += elem
    return total







def selection_sort(lst):
    for start_num in range (len(lst)):
        min_index = start_num
        for check_num in range (start_num+1,len(lst)):
            if lst[min_index] > lst[check_num]:
                min_index = check_num          
        lst[start_num], lst[min_index] = lst[min_index], lst[start_num]
    return lst









def find_min(lst,low,high):
    if low==high:
        return low
    if lst[low] < lst[find_min(lst,low+1,high)]:
        return low
    else:
        return find_min(lst, low+1, high)
    
def selection_sort_recursive(lst, low, high):
    if low == high:
        return lst
    min_val = find_min(lst,low,high)
    if low != min_val:
        lst[low], lst[min_val] = lst[min_val], lst[low]
    return selection_sort_recursive(lst, low+1, high)









def partition(lst,start,end):
    pivot = lst[start]
    i = start
    for j in range (start+1,end+1):
        if lst[j] <= pivot:
            i = i + 1
            lst[i], lst[j] = lst[j],lst[i]
    lst[start], lst[i] = lst[i], lst[start]
    return i

def quicksort(lst, start, end):
    if start < end:
        pivot = partition(lst,start,end)
        quicksort(lst, start, pivot-1)
        quicksort(lst, pivot+1, end)
        
    return lst





#Test codes
def main():
    #binary search
    lst = [11,12,13,14,15,16,17,18]
    val = 14
    low = 0
    high = len(lst)-1
    print(binary_search(lst, val, low,high))

    #nested list sum
    print(nested_list_sum([1,[2,[3],[4,5]],[6,7]]))

    #selection sort
    print(selection_sort([5,8,3,2,1,3,4,5,7]))

    #selection sort(recursive) 
    lst2 = [5,8,3,21,11,2,3,7,5]
    print(selection_sort_recursive(lst2, 0, len(lst2)-1))

    #quick sort
    lst3 = [42, 81, 17, 77, 68, 22, 55,10,90]
    print(quicksort(lst3,0,len(lst3)-1))



main()
