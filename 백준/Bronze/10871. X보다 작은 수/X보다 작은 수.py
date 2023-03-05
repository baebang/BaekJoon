max,X = map(int,input().split())
array = list(map(int,input().split()))

for i in range(max):
    if array[i]<X:
        print(array[i], end=" ")
    