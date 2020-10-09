n = int(input())
a = list(map(int, input().split()))

max = 0
ans = 0
for i in range(n - 1):
    if a[i] > max:
        max = a[i]
        j = i
    if (a[i] % 5 == 0) and (a[i] > a[i + 1]) \
                and (i > j):
        ans = i + 1

print(ans)
