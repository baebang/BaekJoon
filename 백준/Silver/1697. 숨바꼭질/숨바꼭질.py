import sys
from collections import deque

def bfs(v,k):
    q = deque([v])
    while q:
        v = q.popleft()
        if v == k:
            #도달점에 왔다면 return
            return array[v]
        for next_v in (v-1, v+1, 2*v):
            #모든 상황을 다  대입해 보자
            if 0 <= next_v < max and not array[next_v]:
                array[next_v] = array[v] + 1
                #몇초에 방문했는지 처리
                q.append(next_v)
                #다음 연산에 쓰일 값들을 q에 저장


max = 100001
n, k = map(int, sys.stdin.readline().split())
array = [0] * max
print(bfs(n,k))