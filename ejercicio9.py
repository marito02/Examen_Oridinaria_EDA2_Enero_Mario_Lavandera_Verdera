import sys
from heapq import heappop, heappush 
# Una clase para almacenar un nodo de heap
class Node:
    def __init__(self, vertice, peso=0):
        self.vertice = vertice
        self.peso = peso
 
    # Anule la función lt() para hacer que la clase `Node` funcione con un min-heap
    def __lt__(self, other):
        return self.peso < other.peso
 
 
# Una clase para representar un objeto graph
class Graph:
    def __init__(self, edges, n):
        # asigna memoria para la lista de adyacencia
        self.adjList = [[] for _ in range(n)]
 
        # agrega bordes al graph dirigido
        for (principio, destino, peso) in edges:
            self.adjList[source].append((destino, peso))
 
 
def ruta(previo, i, ruta):
    if i >= 0:
        ruta(previo, previo[i], ruta)
        ruta.append(i)
        
def planetas_ruta(ruta):
    planetas=['Alderaan','Endor','Dagobah','Hoth','Tatooine','Vespiner','Shapera','Insomer'
    'Chasleron','Carenler','Intersar','Zamnion','Jarlon','Rentrear','Haperon','Milestein',
    'Kiloner','Faloper','Nointer']
    planetas_ruta=[]
    for i in range(len(ruta)):
        planetas = ruta[i]
        planeta = nombres[numero]
        planeta_ruta.append(nombre)
        print
 
# Ejecutar el algoritmo de Dijkstra en un graph dado
def findShortestPaths(graph, source, n):
 
    # crea un min-heap y empuja el nodo de origen con una distancia de 0
    pq = []
    heappush(pq, Node(source))
 
    # establece la distancia inicial desde la fuente a `v` como infinito
    distancia = [sys.maxsize] * n
 
    # distancia de la fuente a sí mismo es cero
    distancia[source] = 0
 
    # Lista # para rastrear vértices para los cuales ya se encontró el costo mínimo
    done = [False] * n
    done[source] = True
    # almacena el predecesor de un vértice (en una ruta de impresión)
    previo = [-1] * n
    # se ejecuta hasta que el min-heap esté vacío
    
    while pq:
        node = heappop(pq)      # Quitar y devolver el mejor vértice
        u = node.vertice        # obtener el número de vértice
 
        # hacer para cada vecino `v` de `u`
        for (v, peso) in graph.adjList[u]:
            if not done[v] and (distancia[u] + peso) < distancia[v]:        # Escalón de relajación
                distancia[v] = distancia[u] + peso
                previo[v] = u
                heappush(pq, Node(v, distancia[v]))
 
        # marca el vértice `u` como hecho para que no se vuelva a recoger
        done[u] = True
 
    ruta = []
    planetas_ruta = []
    planetas=['Alderaan','Endor','Dagobah','Hoth','Tatooine','Vespiner','Shapera','Insomer'
    'Chasleron','Carenler','Intersar','Zamnion','Jarlon','Rentrear','Haperon','Milestein',
    'Kiloner','Faloper','Nointer']
    for i in range(n):
        if i != source and distancia[i] != sys.maxsize:
            get_ruta(previo, i, ruta)
            for r in range(len(ruta)):
                num = ruta[r]
                name_c = nombres[num]
                planetas_ruta.append(name_c)
            print(f'Path ({planetas[source]} —> {nombres[i]}): Minimum cost = {distancia[i]}, Route = {planetas_ruta}')
            ruta.clear()
            planetas_ruta.clear()
 
 
if __name__=='__main__':
 
    # inicializa los bordes según el diagrama anterior
    # (u, v, w) representa la arista del vértice `u` al vértice `v` con peso `w`
    edges = [(0, 1, 10), (0, 4, 3), (1, 2, 2), (1, 4, 4), (2, 3, 9), (3, 2, 7),
            (4, 1, 1), (4, 2, 8), (4, 3, 2)]
 
    # número total de nodos en el graph (etiquetados de 0 a 4)
    n = 5
 
    # graph de construcción
    graph = Graph(edges, n)
 
    # ejecuta el algoritmo de Dijkstra desde cada nodo
    for source in range(n):
        findShortestPaths(graph, source, n)