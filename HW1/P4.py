import ctypes

def make_array(n):
    return (n * ctypes.py_object)()

class MyList:
    def __init__(self):
        # Initialize an empty array
        self.data = make_array(1)
        self.capacity = 1
        self.n = 0

    def __len__(self):
        return self.n

    def append(self, val):
        # append: O(1) amortized 
        if self.n == self.capacity:
            self.resize(self.capacity * 2)
        self.data[self.n] = val
        self.n += 1

    def resize(self, new_capacity):
        # resize: O(n), where n is number of elements in list
        new_data = make_array(new_capacity)
        for i in range(self.n):
            new_data[i] = self.data[i]
        self.data = new_data
        self.capacity = new_capacity

    def __getitem__(self, ind):
        # Runinng time O(1)
        if not (0 <= ind <= self.n-1):
            raise IndexError(str(ind) + " is out of range")
        return self.data[ind]

    def __setitem__(self, ind, value):
        # Running time O(1)
        if not (0 <= ind <= self.n-1):
            raise IndexError(str(ind) + " is out of range")
        self.data[ind] = value

    def extend(self, other):
        # extend: O(k) amortized, where k is number of elements in other
        for elem in other:
            self.append(elem)

    def __iter__(self):
        for i in range(self.n):
            yield self.data[i]

    def pop(self) :
        #O(1) amortized 
        if self.n == 0:
            raise IndexError("Can't pop() from an empty list")
        if self.n == self.capacity // 4:   
            self.resize(self.capacity // 2)
        val = self.data[self.n-1]
        self.n  -= 1
        return val

    

    def __repr__(self):
        mylst = "["
        for elem in range (self.n):
            mylst += str(self.data[elem])
            if elem == self.n-1:
                mylst += "]"
            else:
                mylst += ", "
        return mylst

    def __add__(self, other):
        new_list = MyList()
        for i in self:
            new_list.append(i)
        for j in other:
            new_list.append(j)
        return new_list

    def __mul__(self, other):
        result = MyList()
        for i in range (other):
            for j in range (self.n):
                result.append(self.data[j]) 
        return result

    def __rmul__(self,other):
        return self * other


my_lst1 = MyList()
my_lst1.append(1)
my_lst1.append(2)
print(my_lst1)

my_lst2 = MyList()
my_lst2.append(3)
my_lst2.append(4)
my_lst2.append(5)
print(my_lst2)

my_lst3 = my_lst1 + my_lst2
# ===> my_lst3 = my_lst1.
print(my_lst3)




