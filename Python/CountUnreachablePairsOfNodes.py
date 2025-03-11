class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:

        # First approach: DFS
        # To use DFS, we will first need to construct a graph.
        # Let us make an adjacency list.
        # We will also have a list that stores the size of every component.
        # Lastly, we will use our math trick to calculate the result

        graph = {}
        components = []
        visited = [False for _ in range(n)]
        res = n*(n - 1) // 2

        def dfs(i):
            if visited[i]:
                return 0
            size = 1
            visited[i] = True
            for neighbours in graph[i]:
                size += dfs(neighbours)
            return size

        for i in range(n):
            graph[i] = []
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        for i in range(n):
            if not visited[i]:
                components.append(dfs(i))
        for i in components:
            res -= i*(i - 1) // 2
        return res

        # Our approach: Find connected components
        # Use union-find algorithm to find connected components. 
        # Iterate over edges, and do a union for two vertices
        # Calculate the number of components in every connected-component.
        # Once that is done, we will use a Math Trick:
        # Total number of pairs in a graph = n*(n-1)//2.
        # From this, we will subtract the number of pairs possible in every component.

        uf = UnionFind(n)

        for i, j in edges:
            uf.union(i, j)

        for i in range(n):
            uf.parent[i] = uf.find(i)
        
        count = Counter(uf.parent)
        sizeOfConnectedComponents = count.values()

        totalPossiblePairs = n*(n-1)//2
        for i in sizeOfConnectedComponents:
            totalPossiblePairs -= i*(i - 1)//2
        return totalPossiblePairs
        

class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.sizeOfComponent = [1 for _ in range(n)]
    
    def find(self, value):
        # if parent of value is value itself, we've reached the node
        if self.parent[value] == value:
            return value
        # else, we recursively call the find function on the parent of value, and return this value
        p = self.find(self.parent[value])
        return p

    def union(self, u, v):
        rootU, rootV = self.find(u), self.find(v)
        uBiggerThanV = self.sizeOfComponent[rootU] > self.sizeOfComponent[rootV]
        
        if rootU != rootV:
            if uBiggerThanV:
                self.parent[rootV] = rootU
                self.sizeOfComponent[rootU] += 1
            else:
                self.parent[rootU] = rootV
                self.sizeOfComponent[rootV] += 1

