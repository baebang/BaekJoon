A = list(input())
B = list(input())


def LCS(A, B):
    m = len(A)
    n = len(B)
    # 2차원 리스트를 생성하고 0으로 초기화합니다.
    dp = [[0] * (n+1) for _ in range(m+1)]
    
    # LCS 길이 계산을 위한 테이블을 채웁니다.
    for i in range(1, m+1):
        for j in range(1, n+1):
            if A[i-1] == B[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i][j-1], dp[i-1][j])
    
    # LCS 길이를 반환합니다.
    return dp[m][n]

print(LCS(A, B))