import sys

input = sys.stdin.readline

n, k = map(int, input().split())

stack = []
number = list(input().rstrip()) # rstrip() 안 해주면 뒤에 \n 원소도 생김

for i in range(n):
    while k>0 and stack and stack[-1] < number[i]:
        stack.pop()
        k-=1
    stack.append(number[i])

print(''.join(stack[:len(stack)-k])) # 다 돌고 나왔는데 k 가 0 이상일 경우