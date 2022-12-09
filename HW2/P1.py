import time # For the SimpleTimer class
import random

### BEGIN POVIDED CODE

class SimpleTimer:
    def __init__(self):
        self.start = time.time()

    def elapsed(self):
        return time.time() - self.start

    def reset(self):
        self.start = time.time()

'''
Cubic running time algorithm for maximum contiguous subsequence sum
start_seq and end_seq are the starting and ending indices of the subsequence
Running time: O(n^3)
'''
def max_subsequence_sum1(lst):
    max_sum = 0
    start_seq = None
    end_seq = None
    for curr_start in range(len(lst)):
        for curr_end in range(curr_start, len(lst)):
            curr_sum = 0
            for i in range(curr_start, curr_end+1):
                curr_sum += lst[i]
            if curr_sum > max_sum:
                max_sum = curr_sum
                start_seq = curr_start
                end_seq = curr_end
    return max_sum, start_seq, end_seq

'''
Quadratic running time algorithm for maximum contiguous subsequence sum
start_seq and end_seq are the starting and ending indices of the subsequence
Running time: O(n^2)
'''
def max_subsequence_sum2(lst):
    max_sum = 0
    start_seq = None
    end_seq = None
    for curr_start in range(len(lst)):
        curr_sum = 0
        for curr_end in range(curr_start, len(lst)):
            curr_sum += lst[curr_end]
            if curr_sum > max_sum:
                max_sum = curr_sum
                start_seq = curr_start
                end_seq = curr_end
    return max_sum, start_seq, end_seq

'''
Linear running time algorithm for maximum contiguous subsequence sum
start_seq and end_seq are the starting and ending indices of the subsequence
Running time: O(n)
'''
def max_subsequence_sum3(lst):
    max_sum = 0
    start_seq = None
    end_seq = None

    curr_start = 0
    curr_sum = 0
    for curr_end in range(len(lst)):
        curr_sum += lst[curr_end]
        if curr_sum > max_sum:
            max_sum = curr_sum
            start_seq = curr_start
            end_seq = curr_end
        elif curr_sum < 0:
            curr_start = curr_end + 1
            curr_sum = 0
    return max_sum, start_seq, end_seq

### END PROVIDED CODE



n = int(input("Please type number(n) to make list of n random integers: "))
lst = (random.sample(range(-10000,10000),n))

#max_subsequence_sum1
my_timer = SimpleTimer()
max_sum,start,end = max_subsequence_sum1(lst)
runtime_sum1 = my_timer.elapsed()
print(runtime_sum1)


#max_subsequence_sum2
my_timer.reset()
max_sum,start,end = max_subsequence_sum2(lst)
runtime_sum2 = my_timer.elapsed()
print(runtime_sum2)


#max_subsequence_sum3
my_timer.reset()
max_sum,start,end = max_subsequence_sum3(lst)
runtime_sum3 = my_timer.elapsed()
print(runtime_sum3)



#check max_subsequence_sum2 and max_subsequence_sum3's average running time
#if running time is 0.
'''
total_runtime_sum2=0
total_runtime_sum3=0

for i in range (1,1001):
    my_timer.reset()
    max_sum,start,end = max_subsequence_sum2(lst)
    runtime_sum2 = my_timer.elapsed()
    total_runtime_sum2 += runtime_sum2
print(total_runtime_sum2/1000)

for i in range (1,1001):
    my_timer.reset()
    max_sum,start,end = max_subsequence_sum3(lst)
    runtime_sum3 = my_timer.elapsed()
    total_runtime_sum3 += runtime_sum3
print(total_runtime_sum3/1000)
'''
