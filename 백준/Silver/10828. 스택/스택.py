
import sys
num  = int(sys.stdin.readline())
arr = []
for i in range(num):
    a = str(sys.stdin.readline().strip())
    result = a.split(" ")
 
    if result[0] == "push":
        arr.append(result[1])
    elif result[0] == "top":
        if len(arr) != 0:
            print(arr[len(arr)-1])
        else:
            print(-1)
    elif result[0] == "size":
        print(len(arr))
    elif result[0] == "empty":
        if len(arr) != 0:
            print(0)
        else:
            print(1)
    else:
        if len(arr) != 0:
            print(arr[len(arr)-1])
            arr.pop()

        else:
            print(-1)

   