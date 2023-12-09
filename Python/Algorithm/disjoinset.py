class Disjointset:
    def __init__(self, n):
        self.parent = [i for i in range(n)]

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)

        if x_root == y_root:
            return
        
        self.parent[x_root] = y_root
    
if __name__ == '__main__':
    ds = Disjointset(5)
    ds.union(0,2)
    ds.union(4,2)
    ds.union(3,1)

    print("4 with 0:", ds.find(4) == ds.find(0))
    print("1 with 0:", ds.find(1) == ds.find(0))
    print("3 with 4:", ds.find(3) == ds.find(4))