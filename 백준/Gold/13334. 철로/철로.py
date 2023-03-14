import sys
import heapq

n = int(sys.stdin.readline())
houses = []
for i in range(n):
    start, end = map(int, sys.stdin.readline().split())
    if start > end:  # 출발지와 도착지를 바꿔줌
        start, end = end, start
    houses.append((start, end))

d = int(sys.stdin.readline())
houses.sort(key=lambda x: x[1])  # 도착지 기준으로 오름차순 정렬

heap = []  # 출발지점을 저장할 최소힙
max_count = 0
for house in houses:
    start, end = house
    if end - start <= d:  # 선로 길이보다 짧은 집들만 골라서 최소힙에 추가
        heapq.heappush(heap, start)
        while heap and end - heap[0] > d:  # 선로 길이보다 큰 집은 최소힙에서 제거
            heapq.heappop(heap)
        max_count = max(max_count, len(heap))  # 최대 집의 개수 갱신

print(max_count)