from operator import le
import re
import unittest
import heapq
import math

graph={}
class Edge:
    

    def __init__(self, source, target, weight=1):
        
        self.source = source
        self.target = target
        self.weight = weight

    def __repr__(self):
        
        if self.weight == 1:
            return "Edge({}, {})".format(repr(self.source), repr(self.target))
        else:
            return "Edge({}, {}, {})".format(
                repr(self.source), repr(self.target), repr(self.weight))

    def __eq__(self, other):
        
        return (self.source, self.target, self.weight) == (
            other.source, other.target, other.weight)

    def __ne__(self, other):
        
        return not self == other

    def __lt__(self, other):
       
        return (self.weight, self.source, self.target) < (
            other.weight, other.source, other.target)

    def __le__(self, other):
        
        return (self.weight, self.source, self.target) <= (
            other.weight, other.source, other.target)

    def __hash__(self):
        
        return hash((self.source, self.target, self.weight))

    def __invert__(self):
        
        return Edge(self.target, self.source, self.weight)

class Graph:
    
    def __init__(self, n=0, directed=False):
        self.n = n                     
        self.directed = directed   
    
    
    def v(self):
        return len(graph)                  
    
    def e(self):
        s = 0
        for elem in graph:
            s += len(graph[elem])
        return s
       

    def is_directed(self):  
        return self.directed

    
    def add_node(self, node):
        if node not in graph:
            graph[node] = []     


   
    def del_node(self, node):
        if node in graph:
            graph.pop(node)     
    
    
    def add_edge(self, edge):
        source = edge.source
        target = edge.target
        weight = edge.weight
        self.add_node(source)
        self.add_node(target)
    
        if source == target:
            raise ValueError("pętle są zabronione")
        if (target, weight) not in graph[source]:
            graph[source].append((target, weight))
        if (source, weight) not in graph[target]:
            graph[target].append((source, weight))      

 
    def del_edge(self, edge):
        source = edge.source
        target = edge.target
        weight = edge.weight
        if(target,weight) in graph[source]:
            i = graph[source].index((target,weight))
            graph[source].pop(i)
        if(source,weight) in graph[target]:
            i = graph[target].index((source,weight))
            graph[target].pop(i)

  


def transform(G):
    L = []
    for elem in G:
        L.append(G[elem])
    
    return L

    

def dijkstra(G,s):

    G = transform(G)

    def relax(u,v, weight):
        if d[v] > d[u] + weight:
            d[v] = d[u] + weight
            parent[v] = u
            heapq.heappush(queue, (d[v], v))


    n = len(G)
    visited = [False]*n
    d = [math.inf]*n
    parent = [None]*n
    queue = []
    d[s] = 0
    heapq.heappush(queue, (0,s))
    while len(queue)>0:
        distance, u = heapq.heappop(queue)
        visited[u] = True
        for v, weight in G[u]:
            if not visited[v]:
                relax(u,v, weight)
    
    return d



class DijkstraTest(unittest.TestCase):

        def test_1(self):
            G = [
        [(1,100), (2,10),],
        [(0,100), (2,5), (3,1)],
        [(0,10), (1,5), (4,200)],
        [(1,1), (4,3)],
        [(2,200), (3,3)]
    ]
            Gg = {
                0:  [(1,100), (2,10),],
                1:  [(0,100), (2,5), (3,1)],
                2:  [(0,10), (1,5), (4,200)],
                3:  [(1,1), (4,3)],
                4:  [(2,200), (3,3)]
            }
            test_d = dijkstra(Gg,0)
            self.assertEqual(test_d,[0,15,10,16,19])

        
        def test_2(self):
            G = [
        [(1,4), (2,7),(6,17)],
        [(0,4), (2,5), (3,4)],
        [(0,7), (1,5), (3,2),(4,8)],
        [(1,4), (2,2),(4,1)],
        [(2,8), (3,1),(5,6),(6,5)],
        [(4,6),(6,1)],
        [(0,17),(4,5),(5,1)]
    ]

            Gg = {
                0:  [(1,4), (2,7),(6,17)],
                1:  [(0,4), (2,5), (3,4)],
                2:  [(0,7), (1,5), (3,2),(4,8)],
                3:  [(1,4), (2,2),(4,1)],
                4:  [(2,8), (3,1),(5,6),(6,5)],
                5:  [(4,6),(6,1)],
                6:  [(0,17),(4,5),(5,1)]
            }

            test_d = dijkstra(Gg,0)
            self.assertEqual(test_d,[0,4,7,8,9,15,14])
        

        def test_3(self):
            G = [
        [(1,4), (2,7),(6,17)],
        [(0,4), (2,5), (3,4)],
        [(0,7), (1,5), (3,2),(4,8)],
        [(1,4), (2,2),(4,1)],
        [(2,8), (3,1),(5,6),(6,5)],
        [(4,6),(6,1)],
        [(0,17),(4,5),(5,1)]
    ]       
            Gg = {
                0:  [(1,4), (2,7),(6,17)],
                1:  [(0,4), (2,5), (3,4)],
                2:  [(0,7), (1,5), (3,2),(4,8)],
                3:  [(1,4), (2,2),(4,1)],
                4:  [(2,8), (3,1),(5,6),(6,5)],
                5:  [(4,6),(6,1)],
                6:  [(0,17),(4,5),(5,1)]
            }
    
            test_d = dijkstra(Gg,2)
            self.assertEqual(test_d,[7, 5, 0, 2, 3, 9, 8])
        


        def test_4(self):
            G = [
        [(1,2), (2,4),(4,5)],
        [(0,2), (3,7)],
        [(0,4), (3,1), (4,1)],
        [(1,7), (2,1),(5,2),(6,12)],
        [(0,5), (2,1),(5,5),(7,4)],
        [(3,2),(4,5)],
        [(3,12),(7,1)],
        [(4,4),(6,1)]
    ]
            Gg ={
                0:  [(1,2), (2,4),(4,5)],
                1:  [(0,2), (3,7)],
                2:  [(0,4), (3,1), (4,1)],
                3:  [(1,7), (2,1),(5,2),(6,12)],
                4:  [(0,5), (2,1),(5,5),(7,4)],
                5:  [(3,2),(4,5)],
                6:  [(3,12),(7,1)],
                7:  [(4,4),(6,1)]
            }
    
            test_d = dijkstra(Gg,0)
            self.assertEqual(test_d,[0, 2, 4, 5, 5, 7, 10, 9])


        def test_5(self):
            G = [
        [(1,2), (2,4),(4,5)],
        [(0,2), (3,7)],
        [(0,4), (3,1), (4,1)],
        [(1,7), (2,1),(5,2),(6,12)],
        [(0,5), (2,1),(5,5),(7,4)],
        [(3,2),(4,5)],
        [(3,12),(7,1)],
        [(4,4),(6,1)]
    ]
            Gg ={
                0:  [(1,2), (2,4),(4,5)],
                1:  [(0,2), (3,7)],
                2:  [(0,4), (3,1), (4,1)],
                3:  [(1,7), (2,1),(5,2),(6,12)],
                4:  [(0,5), (2,1),(5,5),(7,4)],
                5:  [(3,2),(4,5)],
                6:  [(3,12),(7,1)],
                7:  [(4,4),(6,1)]
            }
    
            test_d = dijkstra(Gg,5)
            self.assertEqual(test_d,[7, 9, 3, 2, 4, 0, 9, 8])
        

        def test_6(self):
            G = [
        [(1,6), (2,6),(3,6),(4,6)],
        [(0,6), (5,6),(6,6)],
        [(0,6), (7,6), (8,6)],
        [(0,6), (9,6),(10,6)],
        [(0,6), (11,6),(12,6)],
        [(1,6)],
        [(1,6)],
        [(2,6)],
        [(2,6)],
        [(3,6)],
        [(3,6)],
        [(4,6)],
        [(4,6)]
    ]
            Gg = {
                0:  [(1,6), (2,6),(3,6),(4,6)],
                1:  [(0,6), (5,6),(6,6)],
                2:  [(0,6), (7,6), (8,6)],
                3:  [(0,6), (9,6),(10,6)],
                4:  [(0,6), (11,6),(12,6)],
                5:  [(1,6)],
                6:  [(1,6)],
                7:  [(2,6)],
                8:  [(2,6)],
                9:  [(3,6)],
                10: [(3,6)],
                11: [(4,6)],
                12: [(4,6)]
            }
    
            test_d = dijkstra(Gg,0)
            self.assertEqual(test_d,[0, 6, 6, 6, 6, 12, 12, 12, 12, 12, 12, 12, 12])


        def test_7(self):
            G = [
        [(1,3), (3,3),(5,3),(7,3)],
        [(0,3), (2,9),(7,3),(8,12)],
        [(1,9), (3,6)],
        [(0,3), (2,6),(4,12),(5,10)],
        [(3,12), (5,12)],
        [(0,3),(3,10),(4,12),(6,9)],
        [(5,9),(7,6)],
        [(0,3),(1,10),(6,6),(8,12)],
        [(1,12),(7,12)]
    ]
            Gg = {
                0: [(1,3), (3,3),(5,3),(7,3)],
                1: [(0,3), (2,9),(7,3),(8,12)],
                2: [(1,9), (3,6)],
                3: [(0,3), (2,6),(4,12),(5,10)],
                4: [(3,12), (5,12)],
                5: [(0,3),(3,10),(4,12),(6,9)],
                6: [(5,9),(7,6)],
                7: [(0,3),(1,10),(6,6),(8,12)],
                8: [(1,12),(7,12)]
            }
    
            test_d = dijkstra(Gg,0)
            self.assertEqual(test_d,[0, 3, 9, 3, 15, 3, 9, 3, 15])
        

        def test_8(self):
            G = [
        [(1,1)],
        [(0,1), (3,5),(4,3)],
        [(7,2)],
        [(1,5), (4,2),(5,4)],
        [(1,3), (3,2),(6,3)],
        [(3,4),(6,7)],
        [(4,3),(5,7)],
        [(2,2)]
    ]   
            Gg ={
                0: [(1,1)],
                1: [(0,1), (3,5),(4,3)],
                2: [(7,2)],
                3: [(1,5), (4,2),(5,4)],
                4: [(1,3), (3,2),(6,3)],
                5: [(3,4),(6,7)],
                6: [(4,3),(5,7)],
                7: [(2,2)]
            }
    
            test_d = dijkstra(Gg,0)
            self.assertEqual(test_d,[0, 1, math.inf, 6, 4, 10, 7, math.inf])
        

        def test_9(self):
            G = [
        [(1,1)],
        [(0,1), (3,5),(4,3)],
        [(7,2)],
        [(1,5), (4,2),(5,4)],
        [(1,3), (3,2),(6,3)],
        [(3,4),(6,7)],
        [(4,3),(5,7)],
        [(2,2)]
    ]       
            Gg ={
                0: [(1,1)],
                1: [(0,1), (3,5),(4,3)],
                2: [(7,2)],
                3: [(1,5), (4,2),(5,4)],
                4: [(1,3), (3,2),(6,3)],
                5: [(3,4),(6,7)],
                6: [(4,3),(5,7)],
                7: [(2,2)]
            }
    
            test_d = dijkstra(Gg,2)
            self.assertEqual(test_d,[math.inf, math.inf, 0, math.inf, math.inf, math.inf, math.inf, 2])
        

        def test_10(self):
            G = [
        [(1,5),(3,1),(4,4)],
        [(0,5), (2,3),(6,6)],
        [(1,3),(3,1)],
        [(0,1), (2,1),(5,5)],
        [(0,4), (5,4)],
        [(3,5),(4,4),(6,2),(7,8)],
        [(1,6),(5,2)],
        [(5,8)]
    ]
            Gg = {
                0: [(1,5),(3,1),(4,4)],
                1: [(0,5), (2,3),(6,6)],
                2: [(1,3),(3,1)],
                3: [(0,1), (2,1),(5,5)],
                4: [(0,4), (5,4)],
                5: [(3,5),(4,4),(6,2),(7,8)],
                6: [(1,6),(5,2)],
                7: [(5,8)]
            }
    
            test_d = dijkstra(Gg,0)
            self.assertEqual(test_d,[0, 5, 2, 1, 4, 6, 8, 14])


        def test_11(self):
            G = [
        [(1,5),(3,1),(4,4)],
        [(0,5), (2,3),(6,6)],
        [(1,3),(3,1)],
        [(0,1), (2,1),(5,5)],
        [(0,4), (5,4)],
        [(3,5),(4,4),(6,2),(7,8)],
        [(1,6),(5,2)],
        [(5,8)]
    ]
            Gg = {
    0:[(1,5),(3,1),(4,4)],
    1: [(0,5), (2,3),(6,6)],
    2: [(1,3),(3,1)], 
    3: [(0,1), (2,1),(5,5)],
    4: [(0,4), (5,4)],
    5: [(3,5),(4,4),(6,2),(7,8)],
    6: [(1,6),(5,2)],
    7: [(5,8)]
    }
    
            test_d = dijkstra(Gg,7)
            self.assertEqual(test_d,[14, 16, 14, 13, 12, 8, 10, 0])

    








if __name__ == "__main__":
    
    
    unittest.main()
    