def move(no,x,y):
    if no > 1:
        move(no-1,x,6-x-y)
    
    print(x,y)
    if no > 1:
        move(no-1,6-x-y,y)



num = int(input())
print(2 ** num - 1)
if num <= 20:
    move(num,1,3)
    

