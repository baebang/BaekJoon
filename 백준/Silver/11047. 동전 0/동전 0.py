N, K = map(int, input().split()) 
coin_lst = list()
for i in range(N):
    coin_lst.append(int(input()))
result = 0
count = 0
for i in range(1,N+1):
    if coin_lst[-i] <= K:
        while True:
            result+=K // coin_lst[-i]
            count +=result
            K -= coin_lst[-i] * result
            if K < coin_lst[-i] : 
                result = 0 
                break

print(count)