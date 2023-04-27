from queue import Queue
import heapq

# BFS algorithm
def bfs(graph, start):
    visited = set()
    distances = {start: 0}
    q = Queue()
    q.put(start)
    while not q.empty():
        vertex = q.get()
        if vertex in visited:
            continue
        visited.add(vertex)
        for neighbor, weight in graph[vertex].items():
            if neighbor not in visited:
                q.put(neighbor)
                new_distance = distances[vertex] + weight
                if neighbor not in distances or new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
    return distances

# A* algorithm
def astar(graph, start, target, heuristic):
    visited = set()
    distances = {start: 0}
    q = [(0, start)]
    while q:
        current_distance, current_vertex = heapq.heappop(q)
        if current_vertex == target:
            return distances[target]
        if current_vertex in visited:
            continue
        visited.add(current_vertex)
        for neighbor, weight in graph[current_vertex].items():
            new_distance = distances[current_vertex] + weight
            if neighbor not in distances or new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                priority = new_distance + heuristic(neighbor, target)
                heapq.heappush(q, (priority, neighbor))
    return -1  # if target is unreachable

# example graph
graph = {
    'A': {'B': 5, 'C': 6},
    'B': {'D': 9},
    'C': {'D': 8, 'E': 12},
    'D': {'E': 3},
    'E': {}
}

# example usage
print(bfs(graph, 'A'))  # prints {'A': 0, 'B': 5, 'C': 6, 'D': 14, 'E': 17}
print(astar(graph, 'A', 'E', lambda u, v: 0))  # prints 17 (same as BFS)
print(astar(graph, 'A', 'E', lambda u, v: abs(ord(u) - ord(v))))  # prints 18 (using a simple heuristic function)