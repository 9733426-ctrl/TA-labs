INF = 9999999

# --- Алгоритм Пріма ---
def prim_mst(graph):
    V = len(graph)
    selected = [False] * V
    selected[0] = True
    no_edge = 0
    total_weight = 0
    
    print("--- Алгоритм Пріма ---")
    print("Edge : Weight")
    
    while no_edge < V - 1:
        minimum = INF
        x = 0
        y = 0
        
        for i in range(V):
            if selected[i]:
                for j in range(V):
                    if not selected[j] and graph[i][j] != 0 and graph[i][j] != INF:
                        if minimum > graph[i][j]:
                            minimum = graph[i][j]
                            x = i
                            y = j
                            
        # Виводимо вершини зсунуті на +1, щоб відповідало завданню (1-8 замість 0-7)
        print(f"{x + 1} - {y + 1} : {graph[x][y]}")
        total_weight += graph[x][y]
        selected[y] = True
        no_edge += 1
        
    print(f"Total weight (Prim): {total_weight}\n")


# --- Алгоритм Крускала ---
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []
        self.parent = list(range(vertices))

    def add_edge(self, u, v, w):
        self.graph.append([w, u, v])

    def find_set(self, i):
        if self.parent[i] == i:
            return i
        return self.find_set(self.parent[i])

    def union_set(self, u, v):
        self.parent[u] = self.parent[v]

    def kruskal(self):
        result = []
        # Сортуємо ребра за вагою
        self.graph = sorted(self.graph)
        
        for w, u, v in self.graph:
            u_rep = self.find_set(u)
            v_rep = self.find_set(v)
            
            # Якщо немає циклу, додаємо ребро до MST
            if u_rep != v_rep:
                result.append([u, v, w])
                self.union_set(u_rep, v_rep)
                
        print("--- Алгоритм Крускала ---")
        print("Edge : Weight")
        total_weight = 0
        for u, v, w in result:
            print(f"{u + 1} - {v + 1} : {w}")
            total_weight += w
        print(f"Total weight (Kruskal): {total_weight}")


if __name__ == '__main__':
    # Матриця суміжності для 7-го варіанту (8 вершин)
    G = [
        [0,   2,   1,   5,   INF, INF, 7,   INF],
        [2,   0,   3,   1,   9,   INF, INF, INF],
        [1,   3,   0,   9,   INF, 4,   6,   INF],
        [5,   1,   9,   0,   2,   3,   INF, INF],
        [INF, 9,   INF, 2,   0,   3,   INF, INF],
        [INF, INF, 4,   3,   3,   0,   1,   1  ],
        [7,   INF, 6,   INF, INF, 1,   0,   8  ],
        [INF, INF, INF, INF, INF, 1,   8,   0  ]
    ]
    
    prim_mst(G)
    
    # Ініціалізація графа для Крускала
    g = Graph(8)
    edges = [
        (0, 1, 2), (0, 2, 1), (0, 3, 5), (0, 6, 7),
        (1, 2, 3), (1, 3, 1), (1, 4, 9),
        (2, 3, 9), (2, 5, 4), (2, 6, 6),
        (3, 4, 2), (3, 5, 3),
        (4, 5, 3),
        (5, 6, 1), (5, 7, 1),
        (6, 7, 8)
    ]
    
    for u, v, w in edges:
        g.add_edge(u, v, w)
        
    g.kruskal()
