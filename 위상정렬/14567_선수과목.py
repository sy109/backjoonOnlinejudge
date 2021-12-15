import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

N, M = map(int,input().split())

graph = [[] for _ in range(N+1)]
# print(graph)
for _ in range(M):
    parent, child = map(int, input().split())
    # graph[parent].append(child)
    graph[child].append(parent)
# print(graph)
q = deque()
finished = [-1 for _ in range(N+1)]
cnt = 1

# for _ in range(N):
for i in range(1, len(graph)):
    if len(graph[i]) == 0:
        q.append(i)
        if finished[i] == -1:
            finished[i] = cnt
cnt += 1
loop = len(q)
while q:
    while loop:
        cur = q.popleft()
        for i in range(1, len(graph)):
            if cur in graph[i]:
                graph[i].remove(cur)
            if len(graph[i]) == 0 and finished[i] == -1:
                q.append(i)
                finished[i] = cnt
        loop -= 1
    loop = len(q)
    # print(loop)
    cnt += 1
print(*finished[1:])