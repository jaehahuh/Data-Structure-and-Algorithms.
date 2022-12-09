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
       
        



def main():
    expr = "[{{([])}}([])]"
    result = balanced_expression(expr)
    print(result)


main()
