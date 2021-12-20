from collections import defaultdict
import sys
# from collections import defaultdict
def input():
    return sys.stdin.readline().rstrip()

N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

ans = []
final_answer = defaultdict(int)

checked = [False for _ in range(N)]
# print(checked)
def dfs(j):
    if len(ans) >= M:
        if len(ans) == M:
            string = ' '.join(map(str, ans))
            if not final_answer[string]:
                final_answer[string] = 1
        return
    else:
        for j in range(N):
            if ans[-1] <= nums[j]:
                ans.append(nums[j])
                # checked[j] = True
                dfs(j+1)
                ans.pop()
                # checked[j] = False
for n in range(N):
    ans.append(nums[n])
    # checked[n] = True
    dfs(n)
    ans.pop()
    # checked[n] = False
for finals in final_answer:
    print(finals)