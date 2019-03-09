import json


class Edge(object):
    def __init__(self, v):
        self.v = v

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

    def addEdge(self, u, v):
        edgeF = Edge(v)
        self.adj[u].append(edgeF)

        if not self.directed:
            edgeB = Edge(u)
            self.adj[v].append(edgeB)

    def printGraph(self):
        N = len(self.adj)
        for i in range(N):
            print(i),
            for edge in self.adj[i]:
                print(edge),
            print("")
        print("")


def toIndex(x, y, M):
    return x * M + y


def toPos(x, M):
    return (x / M, x % M)


def validPos(x, y, N, M):
    return (x >= 0 and y >= 0 and x < N and y < M)


def dfs(graph, root, end, ns, covered, state, grid, M):
    count = 0
    state[root] = True
    if root == end:
        state[root] = False
        if covered == ns:
            return 1
        return 0
    # pre process node
    processed = []
    for edge in graph.adj[root]:
        pos = toPos(edge.v, M)
        v, w = edge.v, grid[pos[0]][pos[1]]
        if state[v] is False and w != -1 and v not in processed:
            # process edge
            c = covered
            if w == 0:
                c += 1
            state[v] = True

            count += dfs(graph, v, end, ns, c, state, grid, M)
            state[v] = False
            processed.append(v)
    state[root] = False
    return count


def uniquePathsIII(grid):
    N = len(grid)
    M = len(grid[0])
    start = -1
    end = -1
    graph = Graph(N * M, False)
    num_spaces = 0

    for i in range(N):
        for j in range(M):
            if grid[i][j] == 1:
                start = toIndex(i, j, M)
            if grid[i][j] == 2:
                end = toIndex(i, j, M)
            if grid[i][j] == 0:
                num_spaces += 1
            p_idx = toIndex(i, j, M)
            neighbors = [(i, j - 1), (i, j + 1),
                         (i - 1, j), (i + 1, j)]
            for nbrs in neighbors:
                if validPos(nbrs[0], nbrs[1], N, M):
                    graph.addEdge(p_idx, toIndex(nbrs[0], nbrs[1], M))
    state = [False] * (N * M)
    return dfs(graph, start, end, num_spaces, 0, state, grid, M)


if __name__ == '__main__':
    try:
        while True:
            grid = json.loads(raw_input())
            print(uniquePathsIII(grid))
    except Exception:
        pass
