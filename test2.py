import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for test_case in range(1,T+1):
    n = int(input())
    lst = list(map(int, input().split()))
    lst = [0] + lst
    D = [0]

    for i in range(1,len(lst)):
        for j in range(0,i):
            if lst[i] >= lst[j]:
                maxidx = j
            print(lst[j])
        D.append(D[maxidx] + 1)
    print(D)