import sys
import heapq

input = sys.stdin.read
data = input().split()

# 입력 처리
idx = 0
n = int(data[idx]); idx += 1
m = int(data[idx]); idx += 1

graph = [[] for _ in range(n+1)]
for _ in range(m):
    u = int(data[idx]); idx += 1
    v = int(data[idx]); idx += 1
    w = int(data[idx]); idx += 1
    graph[u].append((v, w))

start = int(data[idx]); idx += 1
end = int(data[idx])

# 다익스트라
INF = int(1e9)
distance = [INF] * (n + 1)
distance[start] = 0
heap = [(0, start)]  # (비용, 노드)

while heap:
    dist, now = heapq.heappop(heap)

    if distance[now] < dist:
        continue

    for next_node, weight in graph[now]:
        cost = dist + weight
        if cost < distance[next_node]:
            distance[next_node] = cost
            heapq.heappush(heap, (cost, next_node))

print(distance[end])
