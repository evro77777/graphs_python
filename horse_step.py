graph = dict()
letters = 'abcdefgh'
numbers = '12345678'

def add_edge(v1,v2):
    graph[v1].add(v2)
    graph[v2].add(v1)


for l in letters:
    for n in numbers:
        graph[l+n] = set()

for i  in range(8):
    for j in range(8):
        v1 = letters[i] + numbers[j]
        for i_mod, j_mod in (i+2, j+1),(i-2,j+1),(i+1,j+2),(i-1,j+2):
            if 0 <= i_mod<len(letters) and 0 <=j_mod<len(numbers):
                v2 = letters[i_mod]+numbers[j_mod]
                add_edge(v1,v2)

print(graph)