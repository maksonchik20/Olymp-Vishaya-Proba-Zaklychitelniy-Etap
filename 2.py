n, m = map(int, input().split())

# Считываем удовольствие для каждого студента на каждой лекции
a = []
for i in range(n):
    row = list(map(int, input().split()))
    a.append(row)

# Считываем удовольствие, получаемое студентами за непосещение каждой лекции
b = []
for i in range(n):
    row = list(map(int, input().split()))
    b.append(row)

# Функция для проверки, можно ли посетить лекцию j с участием студента i
def can_attend(i, j):
    return a[i][j] - b[i][j] >= 0

def max_matching(graph):
    """
    Находит максимальное паросочетание в двудольном графе.
    
    Аргументы:
    graph -- словарь, ключи которого -- вершины первой доли графа,
             значения -- списки вершин второй доли, соединённых рёбрами с соответствующей вершиной из первой доли.
    
    Возвращает список рёбер, входящих в максимальное паросочетание.
    """
    # Функция для поиска увеличивающей цепи в графе.
    def dfs(node):
        if visited[node]:
            return False
        visited[node] = True
        for neighbor in graph[node]:
            if neighbor not in matched or dfs(matched[neighbor]):
                matched[neighbor] = node
                return True
        return False

    matched = {}
    for node in graph:
        visited = {node: False for node in graph}
        dfs(node)

    # Строим список рёбер максимального паросочетания.
    matching = [(matched[node], node) for node in matched]

    return matching

# Строим список смежности для алгоритма Куна
adj_list = []
for i in range(n):
    adj_list.append([])
    for j in range(m):
        if can_attend(i, j):
            adj_list[i].append(j + n) # Студенты имеют номера от 0 до n-1, а лекции от n до n+m-1
        else:
            adj_list[i].append(-1) # Если студент не может посетить лекцию, то ребра нет

# Используем алгоритм Куна для поиска максимального паросочетания
matching = max_matching(adj_list)

# Считаем суммарное удовольствие
total_happiness = 0
for i in range(n):
    for j in adj_list[i]:
        if j != -1 and j - n in matching[i]:
            total_happiness += a[i][j - n]
        else:
            total_happiness += b[i][j - n]

print(total_happiness)
