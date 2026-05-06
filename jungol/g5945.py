n = int(input())
n_sum = 1

if 1 <= n <= 50 and n % 2 == 1:
    for i in range(1, n + 1):
        lst = []

        for j in range(1, i + 1):
            lst.append(n_sum)
            n_sum += 1

        if i % 2 == 0:
            print(*lst[::-1])
        else:
            print(*lst)
else:
    print('INPUT ERROR!')