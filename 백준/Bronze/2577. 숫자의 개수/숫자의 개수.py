a = int(input())
b = int(input())
c = int(input())

count = 0
arr = [0,0,0,0,0,0,0,0,0,0]

result = a*b*c
stresult = str(result)

for i in stresult:
    for k in range(0,10):
        if i==str(k):
            add = int(arr[k] + 1)
            arr[k]=add

for i in arr:
    print(i)