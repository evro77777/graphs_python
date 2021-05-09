import deikstra as gr

v1 = gr.Node('v1')
v2 = gr.Node('v2')
v3 = gr.Node('v3')
v4 = gr.Node('v4')
v5 = gr.Node('v5')
graph = gr.Graph.create_from_nodes([v1, v2, v3, v4, v5])
graph.connect(v1, v4, 3)
graph.connect(v1, v3, 4)
graph.connect(v1, v2, 7)
graph.connect(v1, v5, 5)
graph.connect(v4, v3, 1)
graph.connect(v3, v2, 8)
graph.connect(v4, v5, 2)
graph.connect(v5, v2, 6)


def get_all_ways(g, origin_vertex):
    res = []
    itr = list(set(g.get_vertexes()) - {origin_vertex})
    itr.insert(0, origin_vertex)

    def find(arr, pref):
        flag = False
        for i in range(len(pref)):
            if arr[0] == pref[i][0] and arr[1] == pref[i][1]:
                flag = True
                break
        return flag

    def inner(g, vrtxs, m: int = -1, prefix=None):
        m = len(vrtxs) if m == -1 else m
        prefix = prefix or []
        if m == 0:
            temp = []
            for x in prefix:
                temp.append(x[0])
            res.append(temp)
        for i in range(len(vrtxs)):
            if find([vrtxs[i], i], prefix):
                continue
            else:
                if not prefix:
                    prefix.append([vrtxs[i], i])
                    inner(g, vrtxs, m - 1, prefix)
                elif g.can_traverse_dir(prefix[-1][0], vrtxs[i]):
                    prefix.append([vrtxs[i], i])
                    inner(g, vrtxs, m - 1, prefix)
                    prefix.pop()

    inner(g, itr)
    return res


def backtracking(g, ways):
    best_weight = float('inf')
    best_path = None

    for w in ways:
        temp = 0
        for j in range(len(w) - 1):
            temp += g.get_weight(w[j], w[j + 1])
            if temp >= best_weight:
                break
        if temp < best_weight:
            best_weight = temp
            best_path = w
    return best_weight, best_path


t = get_all_ways(graph, origin_vertex=v1)

print(backtracking(graph, t))
