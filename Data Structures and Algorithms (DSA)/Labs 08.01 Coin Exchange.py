def convert_key(data):
    """JSON"""
    return {int(k): v for k, v in data.items()}

def main():
    import json
    total = int(input())
    left = total
    data = convert_key(json.loads(input()))
    coins = [i for i in data.keys()]
    result = {}
    cgiven = 0

    for c in coins:
        result[c] = 0
        required = left//c
        if required >= data[c]:
            result[c] = data[c]
            left -= c*data[c]
        else:
            result[c] = required
            left -= c*required
        cgiven += result[c]

    print(f"Amount: {total}")
    
    if left > 0:
        print("Coins are not enough.")
        return
    
    print("Coin exchange result:")
    for c in coins:
        print(f"  {c} baht = {result[c]} coins")
    print(f"Number of coins: {cgiven}")

main()