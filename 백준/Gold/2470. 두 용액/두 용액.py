n = int(input())
arr = sorted(list(map(int, input().split())))

left, right = 0, n-1
min_sum = abs(arr[left]+arr[right])
ans = [arr[left], arr[right]]

while left < right:
    sum = arr[left] + arr[right]
    if abs(sum) < min_sum:
        min_sum = abs(sum)
        ans = [arr[left], arr[right]]
    if sum < 0:
        left += 1
    else:
        right -= 1

print(ans[0], ans[1])