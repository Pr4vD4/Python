import numba


@numba.njit()
def n1(n):
    for i in range(1, n + 1):
        s = 0
        for j in range(1, i):
            if i % j == 0:
                s += j
        if i == s:
            print('del', s)


def n2(n):
    while n != 1:
        cc = 1
        while (n % cc != 0 or cc == 1) and cc != n:
            cc += 1
            if n % cc == 0:
                break
        print(n, cc)
        n /= cc


def n3(n, s):
    res = ""
    while n > 0:
        ost = n % s
        n //= s
        res += str(ost)
    print(res[::-1])


n = int(input())
s = int(input())
n3(n, s)
