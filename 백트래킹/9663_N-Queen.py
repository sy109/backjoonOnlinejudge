import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
di = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1)]
maps = [[0]*N for _ in range(N)]
# print(maps)
cnt = 0
ans = 0

def dfs(i,j, direction):
    ni = i + di[direction][0]
    nj = j + di[direction][1]
    if 0 <= ni <= N-1 and 0 <= nj <= N-1:
        maps[ni][nj] = -1
        dfs(ni,nj, direction)


for i in range(N):
    for j in range(N):
        if maps[i][j] == 0:
            cnt += 1
            print(i, j)
            for k in range(8):
                    dfs(i,j,k)
if cnt == 8:
    ans += 1
if cnt > 8:
    ans += (cnt - 7)
# # print(cnt)
# for map in maps:
#     print(map)
# print()
