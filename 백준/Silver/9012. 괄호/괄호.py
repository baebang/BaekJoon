import sys
num = int(sys.stdin.readline())
card = []

for i in range(num):
    arr = str((sys.stdin.readline()))
    left = 0
    right = 0


    for k in range(len(arr)):
        if arr[k] == "(":
            left+=1
        elif arr[k] == ")":
            if left==0:
                right =-1
                break
            right +=1
            if left == right:
                left = 0
                right = 0

    if left == right and right!=-1:
        print("YES")
    else:
        print("NO")