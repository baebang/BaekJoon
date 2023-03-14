import heapq
from sys import stdin

cards = []
result = 0
num = int(stdin.readline())

for i in range(num):
    heapq.heappush(cards, int(stdin.readline()))

while len(cards) > 1:
    card1 = heapq.heappop(cards)
    card2 = heapq.heappop(cards)
    sum_cards = card1 + card2
    result += sum_cards
    heapq.heappush(cards, sum_cards)

print(result)
