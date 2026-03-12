import json

def selectionSort(arr, last):
    comparisons = 0
    for c in range(last):
        smol = arr[c]
        w = c + 1
        while w <= last:
            comparisons += 1
            if arr[w][0] < smol[0] or (arr[w][0] == smol[0] and int(arr[w][1::]) < int(smol[1::])):
                smol = arr[w]
            w += 1
        c_key = arr[c]
        arr[arr.index(smol)] = c_key
        arr[c] = smol
        c += 1
        print(arr)
        
    print(f"Comparison times: {comparisons}")
    
selectionSort(json.loads(input()),int(input()))
