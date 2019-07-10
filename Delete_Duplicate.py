test_case = int(input())
while (test_case > 0):
    n = int(input())
    arr = list(map(int, input().split()))
    count = {}
    for i in arr:
        if i not in count:
            count[i] = 1
            print(i, end=' ')
        else:
            count[i] = count[i] + 1

    #print()
    test_case -= 1