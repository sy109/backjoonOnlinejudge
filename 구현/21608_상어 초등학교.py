import sys
# from collections import deque

def input():
    return sys.stdin.readline().rstrip()

N = int(input())

preferred = [[] for _ in range(N**2)]
maps = [[0 for _ in range(N)] for _ in range(N)]
scores = [[0 for _ in range(N)] for _ in range(N)]
di = [(1,0),(-1,0),(0,1),(0,-1)]
cur_max_score = 0
line_priority = []

for i in range(N**2):
    line = list(map(int, input().split()))
    preferred[line[0]-1]=line[1:]
    line_priority.append(line[0])

def getEmpty(i,j):
    for d in di:
        ni = i + d[0]
        nj = j + d[1]
        if 0 <= ni <= N-1 and 0 <= nj <= N-1 and maps[ni][nj] == 0:
            scores[i][j] += 1

for i in range(N):
    for j in range(N):
        getEmpty(i,j)


for student in line_priority:
    q = []
    for i in range(N):
        for j in range(N):
            if maps[i][j] == 0:
                like_cnt = 0
                for d in di:
                    new_i = i + d[0]
                    new_j = j + d[1]
                    if 0 <= new_i <= N-1 and 0 <= new_j <= N-1:
                        if maps[new_i][new_j] in preferred[student - 1]:
                            like_cnt += 1
                q.append((i,j,like_cnt, scores[i][j]))
                    
    q.sort(key = lambda x : (-x[2], -x[3], x[0], x[1]))
    # print(q)
    x,y = q[0][0],q[0][1]
    maps[x][y] = student
    scores[x][y] = -1
    for d in di:
        ni = x + d[0]
        nj = y + d[1]
        if 0 <= ni <= N-1 and 0 <= nj <= N-1:
            scores[ni][nj] -= 1
    q.clear()
score = 0
# def getScore(maps):
for i in range(N):
    for j in range(N):
        like_cnt = 0
        for d in di:
            ni = i + d[0]
            nj = j + d[1]
            if 0 <= ni <= N-1 and 0 <= nj <= N-1:
                if maps[ni][nj] in preferred[maps[i][j] - 1]:
                    like_cnt += 1
        if like_cnt == 1:
            score += 1
        elif like_cnt == 2:
            score += 10
        elif like_cnt == 3:
            score += 100
        elif like_cnt == 4:
            score += 1000
print(score)