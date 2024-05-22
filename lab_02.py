# Ожидается (требуется получить центральность для четырёх узлов, среди которых три имеют одинаковую центральность, а четвёртый — отличающуюся от них в большую сторону).

import networkx as nx

# Создаем ребра
edges = [
    ("A", "D"),
    ("B", "D"),
    ("C", "D")
]

# Создаем граф
G = nx.Graph()
# Добавляем ребра в граф
G.add_edges_from(edges)

# Вычисление степень центральности
centrality_level = nx.degree_centrality(G)
# print(centrality_level) # проверка

for node, centrality in centrality_level.items():
    print(f"Мера центральности узла {node}: {centrality:.3f}")
