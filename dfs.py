import deikstra as gr

v1 = gr.Node('v1')
v2 = gr.Node('v2')
v3 = gr.Node('v3')
v4 = gr.Node('v4')
v5 = gr.Node('v5')
graph = gr.Graph.create_from_nodes([v1, v2, v3, v4,v5])
graph.connect(v1, v4, 3)
graph.connect(v1, v3, 4)
graph.connect(v1, v2, 7)
graph.connect(v4, v3, 1)
# graph.connect(v4, v2, 2)
graph.connect(v3, v2, 8)

graph.connect(v1, v5, 5)
graph.connect(v4, v5, 2)
graph.connect(v5, v2, 6)

def generate_permutations(itr):
    res = []

    def find(arr, pref):
        flag = False
        for i in range(len(pref)):
            if arr[0] == pref[i][0] and arr[1] == pref[i][1]:
                flag = True
                break
        return flag

    def inner(s, m: int = -1, prefix=None):
        m = len(s) if m == -1 else m
        prefix = prefix or []
        if m == 0:
            temp = []
            for x in prefix:
                temp.append(x[0])
            res.append(temp)
        for i in range(len(s)):
            if find([s[i], i], prefix):
                continue
            else:
                prefix.append([s[i], i])
                inner(s, m - 1, prefix)
                prefix.pop()

    inner(itr)

    return res


def check_comb(g, comb):
    assert len(comb) > 1
    flag = True
    for i in range(len(comb) - 1):
        if not g.can_traverse_dir(comb[i], comb[i + 1]):
            flag = False
            break
    return flag


def all_ways(g, vertex):
    all_v = g.get_vertexes()
    init_v = [vertex]
    all_comb = generate_permutations(list(set(all_v) - set(init_v)))
    res = []
    for comb in all_comb:
        if check_comb(g, comb):
            res.append(comb)
    return res


test= [v4,v2,v3,v5]

def dfs(vertex,g,used= None):
    used = used or []
    used.append(vertex)
    for n in test:
        if n not in used:
            dfs(n,g,used)
    print(used)
dfs(v1,graph)

