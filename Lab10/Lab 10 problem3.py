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



lst = [1,3,2,1,2,1]
print  (mode_of_list(lst))

