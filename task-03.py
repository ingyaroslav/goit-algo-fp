import heapq

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[] for _ in range(vertices)]

    def add_edge(self, u, v, w):
        self.graph[u].append((v, w))
        self.graph[v].append((u, w))  # Для неорієнтованого графа

    def dijkstra(self, src):
        dist = [float('inf')] * self.V
        dist[src] = 0

        pq = [(0, src)]  # Бінарна купа для оптимізації вибору вершин
        while pq:
            d, u = heapq.heappop(pq)
            if d > dist[u]:
                continue
            for v, w in self.graph[u]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    heapq.heappush(pq, (dist[v], v))
        return dist

# Приклад використання
if __name__ == "__main__":
    # Створення графа з 5 вершинами
    graph = Graph(5)
    # Додавання ребер у граф
    graph.add_edge(0, 1, 10)
    graph.add_edge(0, 2, 5)
    graph.add_edge(1, 2, 2)
    graph.add_edge(1, 3, 1)
    graph.add_edge(2, 3, 9)
    graph.add_edge(2, 4, 2)
    graph.add_edge(3, 4, 4)
    
    # Запуск алгоритму Дейкстри від вершини 0
    source = 0
    shortest_distances = graph.dijkstra(source)
    
    # Виведення результату
    print("Найкоротші відстані від вершини", source)
    for i in range(len(shortest_distances)):
        print("До вершини", i, ":", shortest_distances[i])
