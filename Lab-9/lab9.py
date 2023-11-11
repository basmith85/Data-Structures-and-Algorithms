import sys

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def add_edge(self, u, v, w):
        self.graph[u][v] = w
        self.graph[v][u] = w

    def dijkstra(self, src):
        dist = [sys.maxsize] * self.V
        dist[src] = 0
        pq = [(0, src)]
        while pq:
            current_distance, current_vertex = min(pq)
            pq.remove((current_distance, current_vertex))
            if current_distance > dist[current_vertex]:
                continue
            for neighbor, weight in enumerate(self.graph[current_vertex]):
                if weight != 0:
                    distance = current_distance + weight
                    if distance < dist[neighbor]:
                        dist[neighbor] = distance
                        pq.append((dist[neighbor], neighbor))
        self.print_dijkstra(dist)

    def print_dijkstra(self, dist):
        print("Vertex \t Distance from Source")
        for node in range(self.V):
            print(f"{node} \t->\t {dist[node]}")

    def prim(self):
        result = [None] * self.V
        key = [sys.maxsize] * self.V
        mst_set = [False] * self.V
        key[0] = 0
        result[0] = -1
        for _ in range(self.V):
            min_val = sys.maxsize
            min_index = -1
            for v in range(self.V):
                if key[v] < min_val and not mst_set[v]:
                    min_val = key[v]
                    min_index = v
            u = min_index
            mst_set[u] = True
            for v in range(self.V):
                if self.graph[u][v] and not mst_set[v] and key[v] > self.graph[u][v]:
                    key[v] = self.graph[u][v]
                    result[v] = u
        self.print_prim(result)

    def print_prim(self, result):
        print("Edge \t Weight")
        for i in range(1, self.V):
            print(f"{result[i]} - {i} \t {self.graph[i][result[i]]}")

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        x_root = self.find(parent, x)
        y_root = self.find(parent, y)

        if rank[x_root] < rank[y_root]:
            parent[x_root] = y_root
        elif rank[x_root] > rank[y_root]:
            parent[y_root] = x_root
        else:
            parent[y_root] = x_root
            rank[x_root] += 1

    def kruskal_mst(self):
        result = []
        i = 0
        e = 0
        edges = []
        for u in range(self.V):
            for v in range(u + 1, self.V):
                if self.graph[u][v] != 0:
                    edges.append((u, v, self.graph[u][v]))
        edges = sorted(edges, key=lambda x: x[2])

        parent = [i for i in range(self.V)]
        rank = [0] * self.V

        while e < self.V - 1:
            u, v, w = edges[i]
            i += 1
            x = self.find(parent, u)
            y = self.find(parent, v)

            if x != y:
                e += 1
                result.append((u, v, w))
                self.union(parent, rank, x, y)

        self.print_kruskal(result)


    def print_kruskal(self, result):
        print("Edge \t Weight")
        for edge in result:
            print (f"{edge[0]} -> {edge[1]} \t {edge[2]}")

# Create a graph with 21 vertices.
graph = Graph(21)

# Add edges and their weights.
graph.add_edge(0, 1, 4)
graph.add_edge(0, 2, 1)
graph.add_edge(1, 3, 3)
graph.add_edge(2, 4, 2)
graph.add_edge(3, 5, 2)
graph.add_edge(4, 6, 2)
graph.add_edge(5, 7, 2)
graph.add_edge(7, 8, 2)
graph.add_edge(6, 8, 2)

graph.add_edge(8, 9, 5)
graph.add_edge(8, 10, 4)
graph.add_edge(9, 11, 3)
graph.add_edge(10, 11, 1)

graph.add_edge(11, 12, 1)
graph.add_edge(12, 13, 1)
graph.add_edge(13, 14, 1)

graph.add_edge(14, 15, 1)
graph.add_edge(14, 16, 10)
graph.add_edge(15, 17, 1)
graph.add_edge(16, 20, 1)
graph.add_edge(17, 18, 1)
graph.add_edge(18, 19, 1)
graph.add_edge(19, 20, 1)

# Run Dijkstra's algorithm from source vertex 0.
print("\nDijkstra:")
graph.dijkstra(0)

# Find and print the Prim's Minimum Spanning Tree (MST).
print("\nPrim:")
graph.prim()

# Find and print the Kruskal's Minimum Spanning Tree (MST).
print("\nKruskal: ")
graph.kruskal_mst()
