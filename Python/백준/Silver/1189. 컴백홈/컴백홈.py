r, c, k = map(int, input().split())
MAP = [list(input()) for _ in range(r)]
visited = [[0]*c for _ in range(r)]

dy = [-1, 0, 0, 1]
dx = [0, -1, 1, 0]

cnt = 0

def dfs(y, x, dist):
    global cnt
    if y == 0 and x == c-1:
        if dist == k:
            cnt += 1
        return

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < r and 0 <= nx < c:
            if MAP[ny][nx] != 'T' and not visited[ny][nx]:
                visited[ny][nx] = 1
                dfs(ny, nx, dist + 1)
                visited[ny][nx] = 0

visited[r-1][0] = 1  # 시작 지점 방문 체크
dfs(r-1, 0, 1)       # 시작 지점 포함해서 거리 1부터 시작
print(cnt)
