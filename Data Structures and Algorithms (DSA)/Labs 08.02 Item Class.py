class Item:
    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight

    def get_name(self):
        return self.name
    
    def get_price(self):
        return self.price
    
    def get_weight(self):
        return self.weight
    
    def get_cost(self):
        return self.price/self.weight
    
def knapsack(itemList, capacity):
    curr_capacity =  capacity
    taken = []
    while True:
        skip = 0
        mostValuable = None

        for item in itemList:
            if curr_capacity >= item.get_weight():
                if not mostValuable or mostValuable.get_cost() < item.get_cost():
                    mostValuable = item
            else:
                skip += 1

        if mostValuable: 
            curr_capacity -= mostValuable.get_weight()
            taken.append(mostValuable)
            itemList.pop(itemList.index(mostValuable))

        if curr_capacity <= 0 or skip >= len(itemList):
            break

    total = 0
    print(f"Knapsack Size: {capacity} kg")
    print("===============================")
    for i in taken:
        print(f"{i.get_name()} -> {i.get_weight()} kg -> {i.get_price()} THB")
        total += i.get_price()
    print(f"Total: {total} THB")

def main():
    import json
    items = []
    num_items = int(input())
    while num_items != 0:
        item_in = json.loads(input())
        items.append(Item(item_in['name'], item_in['price'], item_in['weight']))
        num_items = num_items - 1
    knapsack_capacity = float(input())
    knapsack(items, knapsack_capacity)
main()
