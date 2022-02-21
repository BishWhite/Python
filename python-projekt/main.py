import unittest
import heapq
import math


def dijkstra(G,s):

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
            test_d = dijkstra(G,0)
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
    
            test_d = dijkstra(G,0)
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
    
            test_d = dijkstra(G,2)
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
    
            test_d = dijkstra(G,0)
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
    
            test_d = dijkstra(G,5)
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
    
            test_d = dijkstra(G,0)
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
    
            test_d = dijkstra(G,0)
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
    
            test_d = dijkstra(G,0)
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
    
            test_d = dijkstra(G,2)
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
    
            test_d = dijkstra(G,0)
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
    
            test_d = dijkstra(G,7)
            self.assertEqual(test_d,[14, 16, 14, 13, 12, 8, 10, 0])

    








if __name__ == "__main__":

    
        


    
        unittest.main()