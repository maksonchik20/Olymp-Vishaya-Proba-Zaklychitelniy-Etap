n = int(input())
cnt = 0
for _ in range(n):
    num = int(input())
    a = (num // 4) + (num % 4) - (1 if num % 4 == 3 else 0)
    cnt += a

print(cnt)
