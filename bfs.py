from collections import deque

n, m = map(int, input().split())
test = [(0,1),(0,12),(0,11),(0,10),(2,6),(1,7),(3,11),(4,10),(5,8),(5,13),(6,10),(7,13),(8,12),(9,11),(11,12),(11,14)]
graph = {i: set() for i in range(n)}
for i in range(m):
    graph[test[i][0]].add(test[i][1])
    graph[test[i][1]].add(test[i][0])
distances = [None] * n
start_vertex = 0
distances[start_vertex] = 0
queue = deque([start_vertex])

while queue:
    cur_v = queue.popleft()
    for neigh_v in graph[cur_v]:
        # проверка на то, что расстояние до соседей-вершин еще не известно(не посещено)
        if distances[neigh_v] is None:
            distances[neigh_v] = distances[cur_v] + 1
            queue.append(neigh_v)

print(graph)
print(distances)