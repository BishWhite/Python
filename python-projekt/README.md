# Algorytm Dijkstry

Algorytm Dijkstry wykorzystywany jest do znajdowania najkrótszej ścieżki z źródła do pozostałych wierzchołków w grafie.

## Opis algorytmu

Rozważamy graf *G*=(V,E), gdzie *V* jest zbiorem wierzchołków grafu i *E* jest zbiorem krawędzi. Dla każdej krawędzi z *u* do *v* należącej do zbioru *E* zdefiniowana jest funkcja *w*(u,v) przypisująca nieujemną wagę tej krawędzi. Dla danego źródła *s* należącego do wierzchołków grafu wyznacznamy najkrótsze ścieżki do pozostałych wierzchołków.

##### Przebieg algorytmu

    Wierzchołek *s* umieszczamy w kolejce priorytetowej z oszacowaną odległością od źródła równą 0. Do momentu, gdy kolejka nie jest pusta zdejmujemy wierzchołek. Dla każdej nieodwiedzonej krawędzi wykonujemy operacje relaksacji

```python
    def relax(u,v, weight):
        if d[v] > d[u] + weight:
            d[v] = d[u] + weight
            parent[v] = u
            heapq.heappush(queue, (d[v], v)) 
```