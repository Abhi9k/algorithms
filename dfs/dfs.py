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

        if self.directed:
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


def dfs(graph, root):
    N = len(graph.adj)
    state = [0] * N
    parent = [None] * N
    stack = deque()

    stack.append(root)
    state[root] = 1

    while len(stack) != 0:
        u = stack.pop()
        print(u)
        # pre process node
        for edge in graph.adj[u]:
            v = edge.v
            if state[v] == 0:
                # process edge
                state[v] = 1
                parent[v] = u

                stack.append(v)
                continue
        # post process node
        state[u] = 2


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
    dfs(graph, 0)
