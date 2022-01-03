import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())

ans = [i for i in range(1,N+1)]

def erase(ans):
    return ans[1::2]

while len(ans) > 1:
    # print(*ans)
    ans = erase(ans)
print(*ans)
