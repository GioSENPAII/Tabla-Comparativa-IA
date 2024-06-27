from heapq import heappop, heappush

def a_star(grafo, inicio, objetivo, heuristica):
    cola = []
    heappush(cola, (0, inicio))
    costos = {inicio: 0}
    padres = {inicio: None}

    while cola:
        _, actual = heappop(cola)

        if actual == objetivo:
            camino = []
            while actual:
                camino.append(actual)
                actual = padres[actual]
            return camino[::-1]

        for vecino, costo in grafo[actual].items():
            nuevo_costo = costos[actual] + costo
            if vecino not in costos or nuevo_costo < costos[vecino]:
                costos[vecino] = nuevo_costo
                prioridad = nuevo_costo + heuristica(vecino, objetivo)
                heappush(cola, (prioridad, vecino))
                padres[vecino] = actual
    return None

# Ejemplo de uso
grafo = {
    'A': {'B': 5, 'C': 3},
    'B': {'D': 7, 'E': 2},
    'C': {'F': 4},
    'D': {'G': 6},
    'E': {'G': 8},
    'F': {'G': 3},
    'G': {}
}

def heuristica(nodo, objetivo):
    # Ejemplo de una heurística simple (distancia en línea recta)
    distancias = {'A': 10, 'B': 7, 'C': 8, 'D': 5, 'E': 3, 'F': 6, 'G': 0}
    return distancias[nodo]

inicio = 'A'
objetivo = 'G'
camino = a_star(grafo, inicio, objetivo, heuristica)
print(camino)  # Salida: ['A', 'C', 'F', 'G']
