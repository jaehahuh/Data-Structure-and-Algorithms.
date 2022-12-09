def two_sum(lst, target):
    d = {item: key for key, item in enumerate(lst)}

    for key, item in enumerate(lst):
        remain = target - item
        if remain in d:
            return (key, d[remain])

    return (None,None)

print (two_sum([-5, 2, 8, -3, 7, 1], -1))



