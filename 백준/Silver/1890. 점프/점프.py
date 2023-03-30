N = int(input())
grid = []
for i in range(N):
    row = list(map(int, input().split()))
    grid.append(row)

dp = [[0 for _ in range(N)] for _ in range(N)]
dp[0][0] = 1

for i in range(N):
    for j in range(N):
        for k in range(i):
            if k + grid[k][j] == i:
                dp[i][j] += dp[k][j]
        for l in range(j):
            if l + grid[i][l] == j:
                dp[i][j] += dp[i][l]

print(dp[N-1][N-1])