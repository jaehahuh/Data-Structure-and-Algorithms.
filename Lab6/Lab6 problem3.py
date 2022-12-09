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
       


s = "<!DOCTYPE html><html><head><meta http-equiv= Content-Style-Type content=text/css /> </html>"

for val in get_tags(s):
    print(val)
print(is_matched_html(s))




s2 = "><<><>>>>>" 
for val in get_tags(s2):
    print(val)
print(is_matched_html(s2))

        
