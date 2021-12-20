import sys

def input():
    return sys.stdin.readline().rstrip()

N, M = map(int, input().split())

ans = []
checked = [False for _ in range(N+1)]
# print(checked)
def dfs(i):
    if len(ans) >= M:
        if len(ans) == M:
            print(*ans)
        return
    else:
        for i in range(1, N+1):
            if ans[-1] <= i:
                ans.append(i)
                dfs(i+1)
                ans.pop()
for n in range(1, N+1):
    ans.append(n)
    dfs(n)
    ans.pop()