from collections import defaultdict
import heapq

def prim_mst(graph):
    """Алгоритм Прима для поиска минимального остовного дерева"""
    mst = defaultdict(set)
    visited = set([list(graph.keys())[0]])
    edges = [
        (cost, start, end) 
        for start, ends in graph.items() 
        for end, cost in ends.items()
    ]
    heapq.heapify(edges)

    while edges:
        cost, start, end = heapq.heappop(edges)
        if end not in visited:
            visited.add(end)
            mst[start].add(end)
            mst[end].add(start)

            for e, c in graph[end].items():
                if e not in visited:
                    heapq.heappush(edges, (c, end, e))

    return mst

def dfs(start, graph, visited):
    """Алгоритм DFS для обхода остовного дерева"""
    visited.add(start)
    total_time = 0

    for end, cost in graph[start].items():
        if end not in visited:
            total_time += cost + dfs(end, graph, visited)

    return total_time

n = int(input())
graph = defaultdict(dict)

for _ in range(n-1):
    u, v, t = map(int, input().split())
    graph[u][v] = t
    graph[v][u] = t

mst = prim_mst(graph)
visited = set()
total_time = dfs(1, mst, visited)

print(total_time)
