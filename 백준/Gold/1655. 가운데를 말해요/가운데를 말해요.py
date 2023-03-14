import sys
import heapq

n = int(sys.stdin.readline())

# 최소 힙과 최대 힙을 준비합니다.
left_heap = []   # 중간값보다 작은 값들이 저장됩니다.
right_heap = []  # 중간값보다 큰 값들이 저장됩니다.

# 처음 입력된 값은 중간값으로 설정합니다.
mid = int(sys.stdin.readline().strip())
print(mid)

# 값을 하나씩 입력받으면서 중간값을 찾아 출력합니다.
for i in range(n-1):
    x = int(sys.stdin.readline().strip())
    
    # 새로운 값 x를 어느 힙에 추가할지 결정합니다.
    if x < mid:
        heapq.heappush(left_heap, -x)
    else:
        heapq.heappush(right_heap, x)
    
    # 두 힙의 크기를 유지합니다.
    if len(left_heap) > len(right_heap):
        heapq.heappush(right_heap, mid)
        mid = -heapq.heappop(left_heap)
    elif len(right_heap) - len(left_heap) > 1:
        heapq.heappush(left_heap, -mid)
        mid = heapq.heappop(right_heap)
    
    # 중간값을 출력합니다.
    print(mid)
