import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
M = int(input())
des_cos = [ [10000000 for _ in range(N)] for _ in range(N)]

# print(des_cos)
for _ in range(M):
    a, b, cost = map(int, input().split())
    if des_cos[a-1][b-1] > cost:
        des_cos[a-1][b-1] = cost

def getMinimumCost():
    for via in range(N):
        for start in range(N):
            for end in range(N):
                if start == end:
                    des_cos[start][end] = 0
                if des_cos[start][via] + des_cos[via][end] < des_cos[start][end]:
                   des_cos[start][end]  = des_cos[start][via] + des_cos[via][end]
getMinimumCost()
# print(des_cos)
for i in range(N):
    for j in range(N):
        if des_cos[i][j] == 10000000:
            des_cos[i][j] = 0
for via in des_cos:
    print(*via)
print()