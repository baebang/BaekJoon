#9498
score = int(input())

if score >= 90 :
    print('A')
elif score >= 80 :
    print('B')
elif score >= 70 :
    print('C')
elif score >= 60 :
    print('D')
else:
    print('F')

# 2753
year = int(input())

print('1') if ((year%4 == 0)and(year%100 != 0)) or (year%400 == 0) else print('0')

#2884
h, m = map(int, input().split())
if m > 44:
    print(h,m-45)
elif m < 45 and h > 0:
    print(h-1,m+15)
else:
    print(23,m+15)