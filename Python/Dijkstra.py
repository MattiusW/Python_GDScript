import queue

class Node:

    def __init__(self):
        self.neighbours = []
        self.cost = float('inf')  # Ustaw koszt na nieskończoność (początkowa wartość)
        self.previous = None

    def __lt__(self, other):
        return self.cost < other.cost
    
    
    def __str__(self):
        return f'Node(neighbours: {self.neighbours}, cost: {self.cost})'

def main():
    print("Dijkstra's Algorithm")

    n1 = Node()
    n2 = Node()
    n3 = Node()
    n4 = Node()
    n5 = Node()
    n6 = Node()

    n1.neighbours.append((2, n2))
    n1.neighbours.append((1, n4))
    n2.neighbours.append((2, n1))
    n4.neighbours.append((1, n1))
    n2.neighbours.append((5, n3))
    n2.neighbours.append((15, n5))
    n3.neighbours.append((5, n2))
    n5.neighbours.append((15, n2))
    n3.neighbours.append((4, n5))
    n5.neighbours.append((4, n3))
    n5.neighbours.append((3, n6))
    n6.neighbours.append((3, n5))
    n4.neighbours.append((13, n5))
    n5.neighbours.append((13, n4))

    # Wywołanie algorytmu Dijkstry
    path = dijkstra(n1, n6)
    print("Najkrótsza ścieżka:")
    for node in path:
        print(node)

def dijkstra(start: Node, end: Node) -> list[Node]:
    pq = queue.PriorityQueue()
    pq.put(start)
    start.cost = 0

    while not pq.empty():
        curr = pq.get()

        for neighbor_cost, neighbor_node in curr.neighbours:
            new_cost = curr.cost + neighbor_cost

            if new_cost < neighbor_node.cost:
                neighbor_node.cost = new_cost
                neighbor_node.previous = curr
                pq.put(neighbor_node)
        
    path = []
    while end is not None:
        path.insert(0, end)  # Wstaw węzły na początek listy (od końca do początku)
        end = end.previous
    return path

if __name__ == "__main__":
    main()