
graph = {}
vert_count, edge_count = [int(x) for x in input().split()]
for i in range(vert_count):
    graph[i + 1] = set()
for _ in range(edge_count):
    start, end = [int(x) for x in input().split()]
    graph[start].add(end)
    graph[end].add(start)


stack = [1]
visited = set()
finished = set()
while stack:
    vert = stack.pop()
    for next_state in graph[vert] - finished:
        if next_state in visited:
            print(vert, next_state)
            exit()
        stack.append(next_state)
        visited.add(next_state)
    finished.add(vert)
print(-1)

