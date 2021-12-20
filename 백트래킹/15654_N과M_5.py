import sys

def input():
    return sys.stdin.readline().rstrip()

N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

ans = []
checked = [False for _ in range(N)]
# print(checked)
def dfs(j):
    if len(ans) >= M:
        if len(ans) == M:
            print(*ans)
        return
    else:
        for j in range(N):
            if not checked[j]:
                ans.append(nums[j])
                checked[j] = True
                dfs(j+1)
                ans.pop()
                checked[j] = False
for n in range(N):
    ans.append(nums[n])
    checked[n] = True
    dfs(n)
    ans.pop()
    checked[n] = False