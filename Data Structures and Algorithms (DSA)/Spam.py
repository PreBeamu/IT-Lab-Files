class ArrayStack:
    def __init__(self):
        self.size = 0
        self.data = []

    def push(self, input_data):
        """Stack"""
        try:
            if input_data.isdigit():
                input_data = int(input_data)
            elif input_data.replace(".", "", 1).isdigit():
                input_data = float(input_data)
        except (TypeError, ValueError, ArithmeticError, AttributeError):
                    pass
        finally:
            self.data.append(input_data)
            self.size += 1

    def pop(self):
        """Stack"""
        if self.is_empty():
            print("Underflow: Cannot pop data from an empty list")
            return None
        self.size -= 1
        return self.data.pop()
    
    def is_empty(self):
        """Stack"""
        return self.size <= 0
    
    def get_stack_top(self):
        """Stack"""
        if self.is_empty():
            print("Underflow: Cannot get stack top from an empty list")
            return None
        return self.data[-1]
    
    def get_size(self):
        return self.size
    
    def print_stack(self):
        print(self.data)

STACK1 = ArrayStack()
STACK2 = ArrayStack()
STACK3 = ArrayStack()
def is_p_matching(txt):
    """Matching!"""
    last = True
    for i in txt:
        if i == "(":
            STACK1.push(i)
        elif i == ")":
            last = STACK1.pop()
    if not last:
        return False
    return STACK1.is_empty()

def is_b_matching(txt):
    """Matching!"""
    last = True
    for i in txt:
        if i == "[":
            STACK2.push(i)
        elif i == "]":
            last = STACK2.pop()
    if not last:
        return False
    return STACK2.is_empty()

def is_c_matching(txt):
    """Matching!"""
    last = True
    for i in txt:
        if i == "{":
            STACK3.push(i)
        elif i == "}":
            last = STACK3.pop()
    if not last:
        return False
    return STACK3.is_empty()

txt = input()
p_valid = is_p_matching(txt)
c_valid = is_c_matching(txt)
b_valid = is_b_matching(txt)
print(p_valid and c_valid and b_valid)
