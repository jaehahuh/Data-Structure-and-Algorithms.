def harmonic(n):
    total = 0
    for i in range (1,n+1):
        total += 1/i
    return total



def harmonicV2(n):
    total = [1/i for i in range (1,n+1) ]
    return sum (total)




