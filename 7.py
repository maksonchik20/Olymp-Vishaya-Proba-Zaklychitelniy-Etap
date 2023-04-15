n = int(input())
input()
unique = set(input().split())
for _ in range(1, n):
    input()
    tracks = set(input().split())
    unique &= tracks
unique = sorted(unique)
print(len(unique), ' '.join(unique), sep='\n')
