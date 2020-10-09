m1, m2 = list(map(int, input().split()))
n1, n2 = list(map(int, input().split()))

for i in range(m1, m2 + 1):
    for j in range(n1, n2 + 1):
        print(str(i) + ' x ' + str(j) + ' = ' + str(i * j))
