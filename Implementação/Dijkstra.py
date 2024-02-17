def dijkstra(grafo, inicio):

    distancia = {vertice: float('inf') for vertice in grafo}
    distancia[inicio] = 0
    visitados = set()
    
    while len(visitados) < len(grafo):
        vertice_atual = min((v for v in grafo if v not in visitados), key=distancia.get)
        visitados.add(vertice_atual)
        
        for vizinho, peso in grafo[vertice_atual].items():
            nova_distancia = distancia[vertice_atual] + peso
            
            if nova_distancia < distancia[vizinho]:
                distancia[vizinho] = nova_distancia
    return distancia

if __name__ == "__main__":
    exemplo = {
        'A': {'B': 2, 'C': 5},
        'B': {'A': 2, 'D': 3},
        'C': {'A': 5, 'F': 3},
        'D': {'B': 3, 'E': 3},
        'E': {'B': 1, 'F': 3},
        'F': {'C': 3, 'E': 3}
    }
    vertice_inicio = 'A'
    distancias = dijkstra(exemplo, vertice_inicio)
    
    print("\nCaminho mais curto a partir do vértice", vertice_inicio)
    for vertice, distancia in distancias.items():
        print(f"Para chegar a {vertice}: {distancia}")