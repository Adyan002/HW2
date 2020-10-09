n = int(input())
s = ''
ans = 0
for i in range(1, n):
    ans += (i * (i + 1))
    if i != (n - 1):
        s = s + str(i) + '*' + str(i + 1) + '+'
    else:
        s = s + str(i) + '*' + str(i + 1) + '='
print(s + str(ans))
