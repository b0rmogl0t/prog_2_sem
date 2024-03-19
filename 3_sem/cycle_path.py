edge_list = [
    [0, 1], [0, 2], [0, 3],
    [1, 2], [1, 4],
    [2,4],
    [3, 4],
    [4, 5],
    [5, 3]
]
vert_num = 6

adj_list = [[] for _ in range(vert_num)]
for u, v in edge_list:
    adj_list[u].append(v)

# dfs
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
            cycle = ''
            sep = '->'
            for i in range(tin[u], tin[v] + 1):
                cycle += f"{tin.index(i)}{sep}"
            cycle += str(u)
            print(f"found cycle {cycle}")
            continue
        elif colors[u] == 'b':
            continue
        elif colors[u] == 'w':
            dfs(u, v)

    colors[v] = 'b'
    timer += 1
    tout[v] = timer


dfs(0)
print(colors)
print(tin)
print('exit timer:', tout)