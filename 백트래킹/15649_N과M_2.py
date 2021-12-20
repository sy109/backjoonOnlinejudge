N , M = map(int, input().split())

def recursive(n):
    if len(ans) >= M:
        if len(ans) == M:
            print(*ans)
        return
    else:
        for i in range(1, N+1):
            if i not in ans and ans[-1] < i:
                ans.append(i)
                recursive(i+1)
                ans.pop()

for i in range(1,N+1):
    ans = []
    ans.append(i)
    recursive(i)