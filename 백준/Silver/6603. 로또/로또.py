from shlex import join
import sys
from itertools import combinations

result = list()
while True:
    S = list(map(int, sys.stdin.readline().split()))

    if S[0] == 0:
        break
    result.append(list(combinations(S[1:], 6)))

  
for i in range(len(result)):
    for j in result[i]:
         print(' '.join([str(a) for a in j]))
       
    print()