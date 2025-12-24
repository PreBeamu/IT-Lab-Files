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

def arrange_students(groups):
    """Arrange them!"""
    Stacks = []
    for _ in range(1,groups+1):
        Stacks.append(ArrayStack())
    while not NAMES.is_empty():
        for v in Stacks:
            if not NAMES.is_empty():
                v.push(NAMES.pop())
    count = 1
    for v in Stacks:
        txt = ""
        for i in v.data:
            txt += i+", "
        txt = txt.rstrip(", ")
        print((f"Group {count}: {txt}"))
        count += 1

groups = int(input())
students = int(input())
NAMES = ArrayStack()
for _ in range(1,students+1):
    name = input()
    NAMES.push(name)
arrange_students(groups)