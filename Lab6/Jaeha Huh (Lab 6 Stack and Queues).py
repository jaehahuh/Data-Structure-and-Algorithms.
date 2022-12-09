#problem 1

class ArrayDeque:
    INITIAL_CAPACITY = 8
    
    def __init__(self):
        self.data = [None] * ArrayDeque.INITIAL_CAPACITY
        self.num_of_elems = 0
        self.front_ind = None   
    
    def __len__(self):
        return self.num_of_elems
   
    def is_empty(self):
        return len(self) == 0

    def first(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.data[self.front_ind]

    def last(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.data[-1]

    def enqueue_first(self, elem):
        if self.num_of_elems == len(self.data):
            self.resize(2 * len(self.data))
        
        if self.is_empty():
            self.data[-1] = elem
            self.front_ind = -1
            self.num_of_elems += 1
        else:
            front_ind = (self.front_ind - 1) % len(self.data)
            self.data[front_ind] = elem
            self.front_ind = front_ind
            self.num_of_elems += 1    
      
    def enqueue_last(self, elem):
        if self.num_of_elems == len(self.data):
            self.resize(2 * len(self.data))
        if self.is_empty():
            self.data[0] = elem
            self.front_ind = 0
            self.num_of_elems += 1
        else:
            back_ind = (self.front_ind + self.num_of_elems) % len(self.data)
            self.data[back_ind] = elem
            self.num_of_elems += 1

    def delete_first(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        elem = self.data[self.front_ind]
        self.data[self.front_ind] = None
        self.front_ind = (self.front_ind + 1) % len(self.data)
        self.num_of_elems -= 1
        if self.is_empty():
            self.front_ind = None
        elif len(self) < len(self.data) // 4:
            self.resize(len(self.data)//2)
        return elem
        
    def delete_last(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        elem = (self.front_ind + self.num_of_elems - 1) % (len(self.data))
        back_ind = self.data[elem]
        self.data[elem] = None
        self.back_ind = -1
        self.num_of_elems -= 1
       
        if self.is_empty():
            self.front_ind = None
        elif len(self) < len(self.data) // 4:
            self.resize(len(self.data)//2)
        return elem

    def resize(self, new_capacity):
        old_data = self.data
        self.data = [None] * new_capacity

        old_ind = self.front_ind
        for new_ind in range(self.num_of_elems):
            self.data[new_ind] = old_data[old_ind]
            old_ind = old_ind + 1
            old_ind = (old_ind + 1) % len(old_data)
        self.front_ind = 0






#Stack ADT
class ArrayStack:
    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return len(self.data) == 0

    def push(self, item):
        self.data.append(item)

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.data.pop()

    def top(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.data[-1]





#problem 2
def balanced_expression(str_input):
    right_parenthesis = ")}]"
    exp_stack = ArrayStack()
    for paren in str_input:
        if paren not in right_parenthesis:
            exp_stack.push(paren)
        else:
            left_parenthesis = exp_stack.pop()
            if left_parenthesis == "(" and paren == ")":
                continue
            elif left_parenthesis == "{" and paren == "}":
                continue
            elif left_parenthesis == "[" and paren == "]":
                continue
            else:
                return False
    return exp_stack.is_empty()






#problem 3
def get_tags(html_str):
    start_ind = 0
    end_ind1 = html_str.find("<", start_ind)
    end_ind2 = html_str.find(">", start_ind)
    while end_ind1 != -1 or end_ind2 != -1 :
        if  end_ind1 < end_ind2  and end_ind1 != -1 and end_ind2 != -1 :
            yield html_str[end_ind1]
            yield html_str[end_ind2]                  
        elif end_ind1 > end_ind2 and end_ind1 != -1 and end_ind2 != -1 :
            yield html_str[end_ind2]
            yield html_str[end_ind1]
        elif end_ind1 == -1:
            yield html_str[end_ind2]
        elif end_ind2 == -1:
            yield html_str[end_ind1]
            
        start_ind = end_ind1+1
        start_ind = end_ind2+1
        end_ind1 = html_str.find("<", start_ind)
        end_ind2 = html_str.find(">", start_ind)


def is_matched_html(html_str):
    tags_stack = ArrayStack()
    for tag in get_tags(html_str):
        if tag == "<":
            tags_stack.push(tag)
        elif tag == ">":
            if tags_stack.is_empty():
                return False
            else:
                tags_stack.pop()
    return tags_stack.is_empty()






#Testing codes

def main():

#Testing codes for problem 1
    d1 = ArrayDeque()

    for i,k in enumerate("12345678"):
        d1.enqueue_first(k)
        print(d1.data)

    for j in range(8):
        d1.delete_first()
        print(d1.data)


    d2 = ArrayDeque()
    for i,k in enumerate("12345678"):
        d2.enqueue_last(k)
        print(d2.data)

    for j in range(8):
        d2.delete_last()
        print(d2.data)

        


#spaces
    print()
    print()     
#Testing codes for problem 2
    expr = "[{{([])}}([])]"
    result = balanced_expression(expr)
    print(result)


#spaces
    print()
    print()     
#Testing codes for problem 3
    
    s = "<!DOCTYPE html><html><head><meta http-equiv= Content-Style-Type content=text/css /> </html>"

    for val in get_tags(s):
        print(val)
    print(is_matched_html(s))

    s2 = "><<><>>>>>" 
    for val in get_tags(s2):
        print(val)
    print(is_matched_html(s2))

main()

#end

