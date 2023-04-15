MOD = 10**9 + 7
def f(a, n):
    if a == 1:
        return 0
    if not n % 2:
        print((a ** 2 ** (n-1) - 1))
        print((a - 1))
        return ((a ** 2 ** (n-1)) - 1) / (a - 1) - (n/2)
    else:
        return (a ** 2 ** (n-1) - 1) / (a**2 - 1) - ((n+1)/2)

a, n = map(int, input().split())

print(f(a, n))