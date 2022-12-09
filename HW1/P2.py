import math

def find_primes (n):
    prime_lst = []
    for i in range (1, n+1):
        if is_prime(i):
            prime_lst.append(i)
    return prime_lst

def is_prime(n):
    if n == 1:
        return False
    for k in range (2, int(math.sqrt(n) + 1)):
        if n % k == 0:
            return False
    return True
       
        



def prime_seive(n):
    prime_num = [True for i in range(n+1)]
    check_num = 2
    prime_lst =[]
    while (check_num*check_num <= n):
        if (prime_num[check_num] == True):
            for i in range(check_num*check_num, n+1, check_num):
                prime_num[i] = False
        check_num+= 1

    for check_num in range(2,n+1):
        if prime_num[check_num]:
            prime_lst.append(check_num)
    return prime_lst




    
