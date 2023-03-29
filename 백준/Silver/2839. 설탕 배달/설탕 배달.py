n = int(input())

dp = [float('inf') for i in range(n+1)]
dp[0] = 0  
for i in range(3, n+1):
    dp[i] = min(dp[i-3], dp[i-5]) + 1

if dp[n] == float('inf'):
    print("-1")
else:
    print(dp[n])