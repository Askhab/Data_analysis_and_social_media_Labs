import networkx as nx

def dijkstra(graph, start):
    # Инициализация
    # Создаем словарь - ключ = вершина графа, значение = минимальное расстояние
    distances = {node: float('inf') for node in graph.nodes}
    # print(f"This is distances {distances} - first")   # проверка
    # значение расстояния у начальной вершины 0
    distances[start] = 0
    # print(f"This is distances {distances} - after start is added")    # проверка
    # словарь для отслеживания посещенных вершин графа
    visited = {node: False for node in graph.nodes}
    # print(f"This is visited {visited}")   # проверка
    # вершины графа
    nodes = list(graph.nodes)
    # print(f"This is nodes {nodes}")   # проверка

    while nodes:
        # Находим непосещенную вершину с минимальным расстоянием
        min_node = None
        for node in nodes:
            if not visited[node]:
                if min_node is None or distances[node] < distances[min_node]:
                    min_node = node
        
        if min_node is None:
            break

        # Отмечаем вершину как посещенную
        nodes.remove(min_node)
        visited[min_node] = True

        # Обновляем расстояния до соседей текущей вершины
        for neighbor, attrs in graph[min_node].items():
            weight = attrs.get('weight', 1)
            if not visited[neighbor]:
                new_distance = distances[min_node] + weight
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
    
    return distances

# Пример использования
if __name__ == "__main__":
    # Создание графа с использованием networkx
    G = nx.Graph()
    
    # Добавление ребер и весов
    # обьяснение кортежа
    # (0, 1, 7)
    # Начальная вершина: 0
    # Конечная вершина: 1
    # Вес ребра: 7
    edges = [
        (0, 1, 7), (0, 2, 9), (0, 5, 14),
        (1, 2, 10), (1, 3, 15),
        (2, 3, 11), (2, 5, 2),
        (3, 4, 6),
        (4, 5, 9)
    ]

    # Добавляем ребра и веса в граф
    G.add_weighted_edges_from(edges)

    # начальная вершина - 0
    start_vertex = 0
    distances = dijkstra(G, start_vertex)
    
    print(f"Кратчайшие пути от вершины {start_vertex} до всех остальных:")
    for vertex, distance in distances.items():
        print(f"До вершины {vertex}: {distance}")
