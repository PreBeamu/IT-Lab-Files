def main():
    s1 = input().strip()
    s2 = input().strip()
    
    n = len(s1)
    max_len = 0
    best_sub = ""
    
    for i in range(n):
        if n - i <= max_len:
            break
        
        length = max_len + 1
        while i + length <= n:
            sub = s1[i : i + length]
            
            if sub in s2:
                max_len = length
                best_sub = sub
                length += 1
            else:
                break
                
    if max_len > 0:
        print(best_sub)
    else:
        print("No common substring.")
        return
        
    print(max_len)

main()