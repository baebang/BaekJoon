def divide_conquer(x, y, n, paper):
    # Base case: 만약 현재 종이가 모두 같은 색이라면,
    if is_same_color(x, y, n, paper):
        color = paper[x][y]
        if color == 0:
            white[0] += 1
        else:
            blue[0] += 1
        return
    
    # Recursive case: 종이를 4등분하여 각각에 대해 재귀적으로 해결
    n //= 2
    divide_conquer(x, y, n, paper)
    divide_conquer(x, y + n, n, paper)
    divide_conquer(x + n, y, n, paper)
    divide_conquer(x + n, y + n, n, paper)
    
def is_same_color(x, y, n, paper):
    color = paper[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if color != paper[i][j]:
                return False
    return True
    
# 입력 받기
n = int(input())
paper = []
for _ in range(n):
    paper.append(list(map(int, input().split())))
    
# 분할정복 알고리즘 수행
white = [0]
blue = [0]
divide_conquer(0, 0, n, paper)

# 출력
print(white[0])
print(blue[0])
