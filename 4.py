# n = int(input())
# cnt = 0
# a = []
# while a != [2] * n:
#     a = []
#     while len(a) != n:
#         for i in range(3):
#             a.append(3)
MOD = 10**9 + 7

def max_matching(n):
    # инициализация массива dp
    dp = [[[0 for _ in range(3)] for _ in range(2*n+1)] for _ in range(n+1)]
    dp[0][0][0] = 1

    # заполнение массива dp
    for i in range(1, n+1):
        for j in range(i, 2*i+1):
            for k in range(3):
                # рассматриваем случай, когда i-й элемент равен 0
                dp[i][j][k] = dp[i-1][j][k] + dp[i-1][j-1][(k*2)%3] + dp[i-1][j-2][(k*4)%3]
                dp[i][j][k] %= MOD

                # рассматриваем случай, когда i-й элемент равен 1 или 2
                for x in range(1, 3):
                    dp[i][j][k] += dp[i-1][j-x][((k*2+x)%3+3)%3] + dp[i-1][j-2*x][((k*4+x*x)%3+3)%3]
                    dp[i][j][k] %= MOD

    # вычисление ответа
    ans = 0
    for j in range(n+1):
        ans += dp[n][j][0]
        ans %= MOD

    return ans
print(max_matching(int(input())))