import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

N, M = map(int, input().split())


# graph = [[] for _ in range(N+1)]
graph2 = [[] for _ in range(N+1)]

degree = [0] * (N+1)
for _ in range(M):
    parent, child = map(int, input().split())
    # graph[child].append(parent)
    graph2[parent].append(child)
    degree[child] += 1
# print(graph)
# print(graph2)
q = deque()
for i in range(1, N+1):
    if degree[i] == 0:
        q.append(i)

loop = len(q)
ans = []
while q:
    while loop:
        cur = q.popleft()
        ans.append(cur)
        for node in graph2[cur]:
            degree[node] -= 1
            if degree[node] == 0:
                q.append(node)
        loop -= 1
    loop = len(q)
print(*ans)