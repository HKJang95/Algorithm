N = int(input())
xlst = list()
ylst = list()
for i in range(N):
    x,y = list(map(int, input().split()))
    xlst.append(x)
    ylst.append(y)

xlst.sort()
ylst.sort()

if N % 2 == 0:
    x = xlst[N // 2 - 1]
    y = ylst[N // 2 - 1]
else:
    x = xlst[N // 2]
    y = ylst[N // 2]
dist = 0
for i in range(N):
    dist += abs(x - xlst[i]) + abs(y - ylst[i])

print(dist)