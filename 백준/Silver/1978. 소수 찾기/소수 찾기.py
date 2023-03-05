a = int(input())
data = list(map(int,input().split()))
primes = 0

for i in data:
    prime =0
    if i>2:
        for k in range(1,int(i)):
            k+=1
            if i%k==0 and i!=k:
                prime +=1
            if i==k and prime ==0:
                primes+=1
    elif i==2:
        primes+=1

print(primes)