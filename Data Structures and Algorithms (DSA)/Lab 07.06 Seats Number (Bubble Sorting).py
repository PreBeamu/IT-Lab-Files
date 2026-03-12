import json

def bubbleSort(arr, last):
    comparisons = 0
    sorted = False
    for c in range(last+1):
        if sorted:
            break
        w = last
        sorted = True
        while w > c:
            if arr[w][0] < arr[w-1][0] or (arr[w][0] == arr[w-1][0] and int(arr[w][1::]) < int(arr[w-1][1::])):
                sorted = False
                w_key = arr[w]
                x_key = arr[w-1]
                arr[w-1] = w_key
                arr[w] = x_key
            comparisons += 1
            w -= 1
        print(arr)
        c += 1

    print(f"Comparison times: {comparisons}")

bubbleSort(json.loads(input()),int(input()))