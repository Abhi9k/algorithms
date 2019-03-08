from collections import deque
import json


class Edge(object):
    def __init__(self, v, w):
        self.v = v
        self.w = w

    def __str__(self):
        return "->{0}".format(self.v)

    def __repr__(self):
        return self.__str__()


class Graph(object):
    def __init__(self, N, is_directed):
        self.adj = [None] * N
        self.directed = is_directed
        for i in range(N):
            self.adj[i] = list()

    def addEdge(self, u, v, w):
        edgeF = Edge(v, w)
        self.adj[u].append(edgeF)

        if not self.directed:
            edgeB = Edge(u, w)
            self.adj[v].append(edgeB)

    def printGraph(self):
        N = len(self.adj)
        for i in range(N):
            print(i),
            for edge in self.adj[i]:
                print(edge),
            print("")
        print("")


def bfs(graph, root):
    queue = deque()
    N = len(graph.adj)
    states = [0] * N
    parent = [None] * N
    states[root] = 1
    queue.append(root)

    while len(queue) != 0:
        u = queue.pop()
        print(u)

        # pre process node

        for edge in graph.adj[u]:
            v = edge.v
            # process edge
            if states[v] == 0:
                parent[v] = u
                states[v] = 1
                queue.appendleft(v)
        states[u] = 2


if __name__ == '__main__':
    N = int(raw_input())
    graph = Graph(N, False)
    try:
        while True:
            u = int(raw_input())
            edges = json.loads(raw_input())
            for v in edges:
                graph.addEdge(u, v, 1)
    except Exception:
        pass
    graph.printGraph()
    bfs(graph, 0)
