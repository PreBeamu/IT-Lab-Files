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

STACK = ArrayStack()
def is_parentheses_matching(expression):
    """Matching!"""
    last = True
    for i in expression:
        if i == "(":
            STACK.push(i)
        elif i == ")":
            last = STACK.pop()
    if not last:
        return False
    return STACK.is_empty()

expression = input()
result = is_parentheses_matching(expression)
if result:
    print("Parentheses in "+expression+" are matched")
else:
    print("Parentheses in "+expression+" are unmatched")
print(result)
