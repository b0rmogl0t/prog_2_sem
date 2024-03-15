edge_list = [
    [0, 1], [0, 3],
    [1, 3],
    [2,3],
    [4, 0], [4, 3],
    [5, 0]
]
vert_num = 6

adj_list = [[] for _ in range(vert_num)]
for u, v in edge_list:
    adj_list[u].append(v)



adj_matrix = [
    [0 for _ in range(vert_num)]
    for _ in range(vert_num)
]


for edge in edge_list:
    u = edge[0]
    v = edge[1]
    adj_matrix[u][v] = 1

g = adj_list
colors = ['w' for _ in range(vert_num)]
parents = [None for _ in range(vert_num)]
timer = 0
tin = [None for _ in range(vert_num)]
tout = [None for _ in range(vert_num)]


def dfs(v, p=-1):
    global timer
    parents[v] = p
    colors[v] = 'g'
    timer += 1
    tin[v] = timer
    for u in g[v]:
        if colors[u] == 'g':
            print(f'found cycle {v} -> {u}')
            continue
        elif colors[u] == 'b':
            continue
        elif colors[u] == 'w':
            dfs(u, v)

    colors[v] = 'b'
    timer += 1
    tout[v] = timer

def top_sort():
    for v in range(vert_num):
        if colors[v] == 'w':
            dfs(v)

    vert_list = [i for i in range(vert_num)]
    ans = [
        x for y, x in sorted(zip(tout, vert_list), key = lambda pair: pair[0], reverse = True )
    ] # по tout сортируем список вершин по убыванию tout
    return ans

ts = top_sort()
path_number = [ 0 for i in range(len(ts))]
path_number[len(ts) - 1] = 1
for v in ts[::-1]:
    k = 1
    for u in adj_list[v]:
        k += path_number[u]
    path_number[v] = k

