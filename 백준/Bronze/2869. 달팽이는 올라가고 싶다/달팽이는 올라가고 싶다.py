import math
moning,night,hight = map(int,input().split())

day = (hight-night) / (moning-night)
print(math.ceil(day))