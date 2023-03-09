import sys
from collections import deque

num  = int(sys.stdin.readline())
arr = deque([])
for i in range(num):
    a = str(sys.stdin.readline().strip())
    result = a.split(" ")
    if result[0] == "push":
        arr.append(result[1])
    elif result[0] == "pop":
        if len(arr) > 0:
            print(arr[0])
            arr.popleft()
        else:
            print(-1)
    elif result[0] == "size":
        print(len(arr))
    elif result[0] == "front":
        if len(arr) > 0:
            print(arr[0])
        else:
            print(-1)
    elif result[0] == "empty":
        if len(arr) > 0:
            print(0)
        else:
            print(1)
    else:
        if len(arr) > 0:
            print(arr[len(arr)-1])
        else:
            print(-1)
    



   

