import heapq

INF = float('inf')

def dijkstra(graph, start):
    n = len(graph)
    dist = [INF] * n
    pred = [-1] * n
    dist[start] = 0
    
    pq = [(0, start)]
    
    while pq:
        current_dist, u = heapq.heappop(pq)
        
        if current_dist > dist[u]:
            continue
            
        for v in range(n):
            weight = graph[u][v]
            if weight != 0 and weight != INF:
                if dist[v] > dist[u] + weight:
                    dist[v] = dist[u] + weight
                    pred[v] = u
                    heapq.heappush(pq, (dist[v], v))
                    
    return dist, pred

def get_path(pred, target):
    path = []
    curr = target
    while curr != -1:
        path.append(curr + 1)
        curr = pred[curr]
    return " -> ".join(map(str, path[::-1]))

def floyd_warshall(graph):
    n = len(graph)
    dist = [[graph[i][j] for j in range(n)] for i in range(n)]
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    
    return dist

if __name__ == '__main__':
    # Матриця суміжності графа (Варіант 7)
    # Відсутнє ребро (2,5) прийнято за 7 згідно з приміткою
    G = [
        [0,   2,   5,   1,   INF, INF, 1,   INF],
        [2,   0,   INF, 3,   7,   INF, INF, INF],
        [5,   INF, 0,   INF, 2,   4,   4,   INF],
        [1,   3,   INF, 0,   9,   INF, 9,   4  ],
        [INF, 7,   2,   9,   0,   3,   INF, INF],
        [INF, INF, 4,   INF, 3,   0,   INF, 1  ],
        [1,   INF, 4,   9,   INF, INF, 0,   6  ],
        [INF, INF, INF, 4,   INF, 1,   6,   0  ]
    ]

    print("=== Алгоритм Дейкстри (від вершини 1) ===")
    dist_dijkstra, pred_dijkstra = dijkstra(G, 0)
    
    print(f"{'З':<3} | {'В':<3} | {'Шлях':<25} | {'Вага':<5}")
    print("-" * 45)
    for i in range(1, len(G)):
        path_str = get_path(pred_dijkstra, i)
        print(f"1   | {i+1:<3} | {path_str:<25} | {dist_dijkstra[i]:<5}")

    print("\n=== Алгоритм Флойда (Фінальна матриця) ===")
    dist_floyd = floyd_warshall(G)
    
    header = "    " + " ".join([f"{i+1:3}" for i in range(len(G))])
    print(header)
    print("-" * len(header))
    for i in range(len(G)):
        row_str = f"{i+1:2} |"
        for j in range(len(G)):
            val = dist_floyd[i][j]
            row_str += f"{val:4}" if val != INF else " INF"
        print(row_str)
