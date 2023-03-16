import sys 

ppap = list(map(str,sys.stdin.readline().strip()))
check = ['P', 'P', 'A', 'P']
result_arr = []
result = 0
i = 0

for i in range(0,len(ppap)):
    result_arr.append(ppap[i])
    if len(result_arr) >=4:
        if result_arr[-4:] == check:
            for _ in range(3):
                result_arr.pop()
        
if result_arr == ['P']:
    print("PPAP")
else: print("NP")