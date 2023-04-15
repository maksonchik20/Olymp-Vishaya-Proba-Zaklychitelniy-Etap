n = int(input())
a = list(map(int, input().split()))

s = {}
for el in a:
    if s.get(el) is None:
        s[el] = 1
    else:
        s[el] += 1
_max = 0
items = list(s.items())
for i in range(len(items)):
    if s.get(items[i][0] + 1) is not None:
        _max = max(_max, items[i][1] + s.get(items[i][0] + 1))
    else:
        _max = max(_max, items[i][1])
print(n - _max)