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

def oper_priority(x):
    if x == '/' or x == '*':
        return 2
    elif x == '+' or x == '-':
        return 1
    else:
        return -1

def infix_to_postfix(exp=input()):
    """POSTFIX them!"""
    STACK = ArrayStack()
    output = ""

    for i in exp:
        if i.isalnum():
            output += i
        elif i == '(':
            STACK.push(i)
        elif i == ')':
            while not STACK.is_empty() and STACK.get_stack_top() != '(':
                output += STACK.pop()
            STACK.pop()
        elif i in "+-*/":
            while (not STACK.is_empty() and oper_priority(STACK.get_stack_top()) >= oper_priority(i)):
                output += STACK.pop()
            STACK.push(i)

    while not STACK.is_empty():
        output += STACK.pop()
    print(output)

infix_to_postfix()
