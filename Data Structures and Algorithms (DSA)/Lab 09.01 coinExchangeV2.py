import json

def main():
    amount = int(input().strip())
    dict_str = input().strip()
    
    coins_dict = json.loads(dict_str)
    
    coin_values = sorted([int(k) for k in coins_dict.keys()], reverse=True)
    
    limits = []
    for v in coin_values:
        if str(v) in coins_dict:
            limits.append(int(coins_dict[str(v)]))
        else:
            limits.append(int(coins_dict[v]))
            
    n_coins = len(coin_values)
    
    dp = [None] * (amount + 1)
    dp[0] = tuple(0 for _ in range(n_coins))
    
    for j in range(n_coins):
        v = coin_values[j]
        limit = limits[j]
        
        for i in range(amount, -1, -1):
            if dp[i] is not None:
                max_k = min(limit, (amount - i) // v)
                
                for k in range(1, max_k + 1):
                    next_amount = i + k * v
                    
                    curr_list = list(dp[i])
                    curr_list[j] += k
                    curr_tuple = tuple(curr_list)
                    curr_sum = sum(curr_tuple)
                    
                    if dp[next_amount] is None:
                        dp[next_amount] = curr_tuple
                    else:
                        best_sum = sum(dp[next_amount])
                        if curr_sum < best_sum:
                            dp[next_amount] = curr_tuple
                        elif curr_sum == best_sum:
                            if curr_tuple > dp[next_amount]:
                                dp[next_amount] = curr_tuple
                                
    print(f"Amount: {amount}")
    if dp[amount] is None:
        print("Can not exchange.")
    else:
        print("Coin exchange result:")
        ans_tuple = dp[amount]
        for j in range(n_coins):
            print(f"  {coin_values[j]} baht = {ans_tuple[j]} coins")
        print(f"Number of coins: {sum(ans_tuple)}")

main()