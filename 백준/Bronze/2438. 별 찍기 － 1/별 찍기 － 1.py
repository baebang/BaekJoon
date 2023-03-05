star= int(input())

for i in range(0,star):
    print("*")
    if(i==star-1):
        break
    for i in range(0,i+1):
        print("*",end="")