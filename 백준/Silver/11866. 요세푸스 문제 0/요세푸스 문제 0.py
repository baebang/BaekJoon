import sys
from collections import deque

N,K = map(int, sys.stdin.readline().split())
arr = deque([i for i in range(1,N+1)])
new_arr = deque([])
k_num = K-1
count = 1

while arr:
    # K번째 사람을 제거하고 결과 리스트에 추가
    arr.rotate(-K+1)
    new_arr.append(arr.popleft())



print(end="<")
for i in range(0,len(list(new_arr))-1):
    print(new_arr[i],end=", ")
print(new_arr[-1],end=">")
    