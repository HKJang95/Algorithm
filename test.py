def binsearch(lst,tgt):
    start = 0
    end = len(lst) - 1

    while start <= end:
        mid = (start + end) // 2
        if lst[mid] > tgt:
            end = mid - 1
        elif lst[mid] < tgt:
            start = mid + 1
        else:
            return True
    return False

T = int(input())
anslst = list()
for i in range(T):
    N = int(input())
    lst = list(map(int, input().split()))
    lst.sort()
    ans = 0
    for i in range(N-2):
        for j in range(i+1,N-1):
            diff = abs(lst[i] - lst[j])
            if binsearch(lst[i+1:], lst[j] + diff):
                ans += 1
    anslst.append(ans)

for i in anslst:
    print(i)