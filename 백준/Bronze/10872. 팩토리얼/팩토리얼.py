num = int(input())
add=1
for i in range(1,num+1):
    add=add*i
    if num==0:
        print(1)
        break
print(add)