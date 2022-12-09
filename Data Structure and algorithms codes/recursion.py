# Counting Up
def count_up1(start, end):
    if (start == end):
        print(end)
    else:
        print(start)
        count_up1(start + 1, end)

def count_up2(start, end):
    if (start == end):
        print(end)
    else:
        count_up2(start, end - 1)
        print(end)

def count_up3(start, end):
    if (start == end):
        print(end)
    else:
        mid = (start + end) // 2
        count_up3(start, mid)
        count_up3(mid+1, end)


# Counting Down
def count_down(start, end):
    if (start == end):
        print(end)
    else:
        print(end)
        count_down(start + 1, end)

        
# Counting Up and Down
def count_up_and_down(start, end):
    if (start == end):
        print(end)
    else:
        print(start)
        count_up_and_down(start + 1, end)
        print(start)


# Factorial
def factorial(n):
    if(n == 1):
        return 1
    else:
        rest_fact = factorial(n-1)
        return rest_fact * n


# Computing powers (x^n)
def power1(x, n):
    if(n == 1):
        return x
    else:
        rest = power1(x, n-1)
        return x*rest

def power2(x, n): 
    if (n == 1):
        return x
    else:
        part1 = power2(x, n//2)
        part2 = power2(x, n//2)
        if (n % 2 == 0):
            return part1 * part2
        else: # n is odd
            return x * part1 * part2

def power3(x, n):
    if (n == 1):
        return x
    else:
        part = power3(x, n//2)
        if (n % 2 == 0):
            return part * part
        else: # n is odd
            return x * part * part
