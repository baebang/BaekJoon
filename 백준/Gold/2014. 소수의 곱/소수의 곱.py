import sys
import heapq
input = sys.stdin.readline

K, N = map(int, input().rstrip().split(" "))

arr = list(map(int, input().rstrip().split(" ")))
q = list(arr)
heapq.heapify(q)
head = None
for _ in range(N):
    head = heapq.heappop(q)
    for a in arr:
        heapq.heappush(q, head*a)
        if(head % a == 0):
            break

print(head)