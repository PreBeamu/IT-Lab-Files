import json

def knapsackV2(amount, itemList):
    n = len(itemList)
    dp = [[0] * (amount + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        name, price, weight = itemList[i-1]
        for w in range(amount + 1):
            if weight <= w:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w - weight] + price)
            else:
                dp[i][w] = dp[i-1][w]
                
    res = dp[n][amount]
    w = amount
    selected_items = []
    
    for i in range(n, 0, -1):
        if res <= 0:
            break
        if res == dp[i-1][w]:
            continue
        else:
            selected_items.append(itemList[i-1])
            res -= itemList[i-1][1]
            w -= itemList[i-1][2]
            
    selected_items.sort(key=lambda x: x[0])
    
    print(f"Total: {dp[n][amount]}")
    for name, price, weight in selected_items:
        print(f"{name} -> {weight} kg -> {price} THB")

line1 = input()
line2 = input()

if line1.startswith('['):
    itemList = json.loads(line1)
    amount = int(line2)
else:
    amount = int(line1)
    itemList = json.loads(line2)
    
knapsackV2(amount, itemList)