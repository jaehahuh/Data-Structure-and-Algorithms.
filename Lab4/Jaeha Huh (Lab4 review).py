import random

#  T(n) = Θ(n^2)  
'''
def random_str(n):  
    letters = "abcdefghijklmnopqrstuvwxyz"
    s = ""
    for i in range(1,n+1):
        curr = random.choice(letters)
        s = s + curr + ' '
    return s
'''


# T(n) = Θ(2n) = Θ(n)    
def random_str(n):  
    letters = "abcdefghijklmnopqrstuvwxyz"
    lst = []
    for i in range(1,n+1):  #Θ(n)
        curr = random.choice(letters)
        lst.append(curr)  #Θ(1) Amortized
    s = ' '.join(lst) #Θ(n)
    return s  





def powers(base,n):
    if n == 0:
        yield 1
    else :
        for i in range (1, n+1):
            yield base ** i







def is_palindrome (input_str, low, high):
 
    if high <= low :
        return True
    if input_str[low] != input_str[high-1]:
        return False
    return is_palindrome(input_str,low+1,high-1)






def partition(lst):
    pivot = lst[0]
    i = 0
    for j in range (1,len(lst)):
        if lst[j] <= pivot:
            i = i + 1
            lst[i], lst[j] = lst[j],lst[i]
    lst[0], lst[i] = lst[i], lst[0]
    return lst

   



def main():
    print(random_str(10))

    for val in powers(3, 5):
        print(val, end=' ')
 
    
    print()
    
    s = 'racecar'
    print(is_palindrome(s, 0, len(s)))
    

    lst = [42, 81, 17, 77, 68, 22, 55,10,90]
    print(partition(lst))

   
main()



