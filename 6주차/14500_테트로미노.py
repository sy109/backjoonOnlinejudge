import sys

def input():
    return sys.stdin.readline().rstrip()

N, M = map(int, input().split())
maps = []

for _ in range(N):
    line = list(map(int, input().split()))
    maps.append(line)
# print(maps)

# def first(coord):
    # for row in range(coord[0], coord[0]+4):