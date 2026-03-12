import json

def insertionSort(arr, last):
    comparisons = 0
    for c in range(1, last + 1):
        key = arr[c]
        w = c - 1
        while w >= 0:
            comparisons += 1
            if key[0] < arr[w][0] or (key[0] == arr[w][0] and int(key[1::]) < int(arr[w][1::])):
                arr[w + 1] = arr[w]
                w -= 1
            else:
                break 
        arr[w + 1] = key
        print(arr)
        
    print(f"Comparison times: {comparisons}")

insertionSort(json.loads(input()),int(input()))