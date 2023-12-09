from disjoinset import Disjointset

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    def kruskal(self):
        result = []
        i = 0
        e = 0

        self.graph = sorted(self.graph, key=lambda item: item[2])

        ds = Disjointset(self.V)

        while e < self.V - 1:
            u, v , w = self.graph[i]
            i += 1
            x = ds.find(u)
            y = ds.find(v)

            if x != y:
                e += 1
                result.append([u,v,w])
                ds.union(x,y)
            
        return result
    
if __name__ == '__main__':
    g = Graph(4)
    g.add_edge(0,1,10)
    g.add_edge(0,2,6)
    g.add_edge(0,3,5)
    g.add_edge(1,3,15)
    g.add_edge(2,3,4)

    minimum_spanning_tree = g.kruskal()
    print("Minimum Spannig Tree:")
    for u,v, weight in minimum_spanning_tree:
        print(f"{u} -- {v} == {weight}") 
