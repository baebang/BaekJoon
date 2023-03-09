import sys
from collections import deque

num = int(sys.stdin.readline())
card = deque([])

if num>1:
    for i in range(1,num+1):
        card.append(i)

    while True:
        card.popleft()
        item = card.popleft()
        card.append(item)
        if len(card) == 1:
            print(card[0])
            break
else:
    print(num)