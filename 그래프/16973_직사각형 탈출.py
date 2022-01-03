import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

N , M = map(int, input().split())

maps = []
# walls = []
di = [(1,0),(-1,0),(0,1),(0,-1)]
visited = [ [0 for _ in range(M)] for _ in range(N)]
cm =[[0 for _ in range(M)] for _ in range(N)]

for i in range(N):
    line = list(map(int, input().split()))
    maps.append(line)

H, W, sr, sc, fr, fc = map(int, input().split())

q = deque()
visited[sr-1][sc-1] = 1
q.append((sr-1,sc-1, 0))

for i in range(N):
    summ = 0
    for j in range(M):
        summ += maps[i][j]
        cm[i][j] = summ
for i in range(M):
    summ = 0
    for j in range(N):
        summ += cm[j][i]
        cm[j][i] = summ


ans = -1

while q:
    cur_i, cur_j, cur_move = q.popleft()
    for d in di:
        new_i = cur_i + d[0]
        new_j = cur_j + d[1]
        if 0<= new_i <= N-1 and 0 <= new_j <= M-1:
            end_i = new_i + H -1
            end_j = new_j + W -1
            if 0 <= end_i <= N-1 and 0 <= end_j <= M-1:
                if visited[new_i][new_j] == 0:
                    checkWall = cm[end_i][end_j]
                    if new_i == 0 and new_j != 0:
                        checkWall = checkWall - cm[end_i][new_j-1]
                    elif new_j == 0 and new_i != 0:
                        checkWall = checkWall - cm[new_i-1][end_j]
                    elif new_i != 0 and new_j != 0:
                        checkWall = checkWall - cm[end_i][new_j-1] - cm[new_i-1][end_j] + cm[new_i-1][new_j-1]
                    if checkWall == 0:
                        visited[new_i][new_j] = 1
                        q.append((new_i, new_j, cur_move + 1))
                        if new_i == fr-1 and new_j == fc-1:
                            ans = cur_move +1
print(ans)