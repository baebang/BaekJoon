from collections import deque

# 미로의 크기와 미로 정보 입력
n, m = map(int, input().split())
maze = [list(map(int, input())) for _ in range(n)]

# 상, 하, 좌, 우 이동
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS 알고리즘 수행
def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        # 상, 하, 좌, 우 이동
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로 범위를 벗어나지 않는 경우
            if 0 <= nx < n and 0 <= ny < m:
                # 길일 경우
                if maze[nx][ny] == 1:
                    maze[nx][ny] = maze[x][y] + 1
                    queue.append((nx, ny))

    # (N, M)까지의 최단거리 반환
    return maze[n-1][m-1]

# (1, 1)에서 BFS 알고리즘 수행
print(bfs(0, 0))
