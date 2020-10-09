x = int(input())

a = [0] * 9

while x != 0:
    a[x - 1] += 1
    x = int(input())

print(*a)
