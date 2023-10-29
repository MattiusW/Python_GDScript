import Node
import queue
from typing import List

class Node:

    def __init__(self):
        self.neighbours = []
        self.cost = 0
        self.previous = None

def main():
    print("Dijkstra's Algorithm")

    n1 = Node()
    n2 = Node()
    n3 = Node()
    n4 = Node()
    n5 = Node()
    n6 = Node()

    n1.neighbours.append((2, n2))


if __name__ == "__main__":
    main()