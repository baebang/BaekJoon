import sys
import heapq

N = int(sys.stdin.readline())
max_heap = []

for i in range(0,N):
    
    arr = int(sys.stdin.readline())
    heapq.heappush(max_heap, (-arr, arr))
    if arr ==0:
        # 최대값 나오게하기
        max_item = heapq.heappop(max_heap)[1]
        # 최대값 삭제
        print(max_item) # 9
        