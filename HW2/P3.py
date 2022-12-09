def permutations(lst, low, high):
    result = []
    if low == high:
        return [[lst[low]]]
    
    for perm_lst in permutations(lst, low+1, high):
        for elem in range(len(perm_lst) + 1):
            perm = perm_lst[:]
            perm.insert(elem, lst[low])
            result.append(perm)
    return result

