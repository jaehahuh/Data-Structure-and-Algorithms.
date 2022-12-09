def flatten_nested_list(lst,low,high):
    result = []
    while low <=  high:
        if isinstance(lst[low], list):
            result.extend(flatten_nested_list(lst[low], 0, len(lst[low])-1))
            low+=1
        else:
            result.append(lst[low])
            low+=1
    return result
    

