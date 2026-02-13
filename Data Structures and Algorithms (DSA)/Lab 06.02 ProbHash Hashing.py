class Student:
    def __init__(self, std_id, name, gpa):
        self.std_id = std_id
        self.name = name
        self.gpa = gpa

    def print_details(self):
        print(f'ID: {self.std_id}')
        print(f'Name: {self.name}')
        print(f'GPA: {self.gpa:.02f}')

class ProbHash:
    def __init__(self, size):
        self.hash_table = [None for _ in range(size)]
        self.size = size

    def hash(self, key):
        return key % self.size

    def rehash(self, hkey):
        return (hkey + 1)%self.size
    
    def checkSize(self):
        x = 0
        for i in self.hash_table:
            if i is not None:
                x += 1
        return x
    
    def insert_data(self, student):
        key = self.hash(student.std_id)
        
        while self.hash_table[key]:
            key = self.rehash(key)
            if key >= self.size:
                key = 0
            if self.checkSize() >= self.size:
                print(f"The list is full. {student.std_id} could not be inserted.")
                return
        
        self.hash_table[key] = student
        print(f"Insert {student.std_id} at index {key}")

    def search_data(self, std_id):
        start = std_id % self.size
        idx = start
        
        while self.hash_table[idx] is not None:
            if self.hash_table[idx].std_id == std_id:
                print(f"Found {std_id} at index {idx}")
                return self.hash_table[idx]
            idx = self.rehash(idx)
            
            if idx == start:
                break
                
        print(f"{std_id} does not exist.")
        return None

def main():
    import json
    size = int(input())
    hashtable = ProbHash(size)
    while True:
        finish = input()
        if finish == "Done":
            break
        condition, data = finish.split(" = ")
        if condition == "I":
            std_in = json.loads(data)
            std = Student(std_in["ID"], std_in["Name"], std_in["GPA"])
            hashtable.insert_data(std)
        elif condition == "S":
            print("------")
            student = hashtable.search_data(int(data))
            if student is not None:
                student.print_details()
            print("------")
        else:
            print("Invalid Condition!")
main()