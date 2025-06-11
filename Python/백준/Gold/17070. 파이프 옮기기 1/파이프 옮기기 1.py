import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

# 방향: 0 - 가로, 1 - 세로, 2 - 대각선
dp = [[[ -1 for _ in range(n)] for _ in range(n)] for _ in range(3)]

def dfs(y, x, dir):
    # 이미 계산한 값이면 반환
    if dp[dir][y][x] != -1:
        return dp[dir][y][x]

    # 목적지 도착
    if y == n - 1 and x == n - 1:
        return 1

    ways = 0

    # 가로 → 가로 or 대각선
    if dir == 0 or dir == 2:
        if x + 1 < n and graph[y][x + 1] == 0:
            ways += dfs(y, x + 1, 0)

    # 세로 → 세로 or 대각선
    if dir == 1 or dir == 2:
        if y + 1 < n and graph[y + 1][x] == 0:
            ways += dfs(y + 1, x, 1)

    # 어느 방향이든 → 대각선
    if x + 1 < n and y + 1 < n:
        if graph[y][x + 1] == 0 and graph[y + 1][x] == 0 and graph[y + 1][x + 1] == 0:
            ways += dfs(y + 1, x + 1, 2)

    dp[dir][y][x] = ways
    return ways

print(dfs(0, 1, 0))
