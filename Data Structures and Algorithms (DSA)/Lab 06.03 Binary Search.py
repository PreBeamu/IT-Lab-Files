import json

class Student:
    def __init__(self, std_id, name, gpa):
        self.std_id = std_id
        self.name = name
        self.gpa = gpa

    def print_details(self):
        print(f'ID: {self.std_id}')
        print(f'Name: {self.name}')
        print(f'GPA: {self.gpa:.02f}')

def binary_search(data, name):
    low = 0
    high = len(data) - 1
    compare = 0
    founded = None

    while low <= high:
        compare += 1
        mid = (low + high) // 2
        mid_name = data[mid].name

        if mid_name == name:
            print(f"Found {name} at index {mid}")
            founded = data[mid]
            break
        elif name < mid_name:
            high = mid - 1
        else:
            low = mid + 1
    
    if not founded:
        print(f"{name} does not exists.")
    else:
        founded.print_details()

    print(f"Comparisons times: {compare}")

def main(text_in):
    std_in = json.loads(text_in)
    all_std = []
    for i in std_in:
        std = Student(i["id"], i["name"], i["gpa"])
        all_std.append(std)
    binary_search(all_std, input())

main(input())