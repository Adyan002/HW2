def move(n, x, y):
    if n == 1:
        print(n, x, y)
    else:
        z = 6 - x - y
        move(n - 1, x, z)
        if n > 2:
            move(n - 2, y, z)
            print(n, x, y)
            move(n - 2, z, y)
        else:
            print(n, x, y)


a = int(input())

if a % 2 != 0:
    move(a, 1, 2)
else:
    move(a, 1, 3)
