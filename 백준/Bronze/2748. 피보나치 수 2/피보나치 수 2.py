num = int(input())
arr = []
arr.append(0)
arr.append(1)

if num > 1:
    for i in range(2,num+1):
        result = arr[i-1] + arr[i-2]
        arr.append(result)
print(arr[num])