# С использованием библиотеки NetworkX требуется написать скрипт для генерации графа в модели Эрдёша-Реньи с заданными характеристиками. Преподавателем будут даны значения количества вершин и вероятность появления случайного ребра. Требуется вычислить в программе среднюю степень вершины и сравнить её со значением средней степени вершины, полученной по формуле из материала лекций.

#  Ожидается (n=12, p=0.6)
# n - количество вершин
# p - вероятность появления ребер

import networkx as nx

G = nx.erdos_renyi_graph(12, 0.6)
a = 0
# Вычисляем среднее по формуле из презентации
average_formula = (12 - 1) * 0.6
# print(average_formula) # проверка

for n in G.nodes():
    a += G.degree(n)

# Вычисляем среднее по результату цикла
average_by_cycle = float(a) / len(G.nodes())
# print(average_by_cycle) # проверка

if average_formula != average_by_cycle:
    print("Средняя степень по формуле и средняя степень вычисленная в программе не равны.")
else:
    print("Средняя степень по формуле и средняя степень вычисленная в программе равны.")
    
print(f"Средняя степень по формуле - {average_formula}")
print(f"Средняя степень вычисленная в программе - {average_by_cycle}")
