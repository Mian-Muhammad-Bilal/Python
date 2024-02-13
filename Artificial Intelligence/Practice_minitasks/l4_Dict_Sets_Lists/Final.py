# --W4/L4

# ==============================================================================

# Task no.1(4 functions that directly mutate a list)
def repeat(lst, x):
    lst *= x


def add(lst, x):
    lst.append(x)


def remove(lst, m, n):  # removing all indexes passed by the user...in this case its removing these four index:0123
    del lst[m:(n+1)]


def concat(lst, x):
    lst.extend(x)


l = [1, 2, 3, 4]
repeat(l, 3)
print(f"List after repeat function {l}")
add(l, 333)
print(f"List after add function {l}")
remove(l, 0, 3)
print(f"List after remove function {l}")
concat(l, [444, 555, 666])
print(f"List after concat function {l}")

# ==============================================================================

# Task no.2 (two_product function)


def two_product(lst, x):
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] * lst[j] == x:
                return [lst[i], lst[j]]
    else:
        print('product not found :)')


print(two_product([2, 2, 3, 4, 5, 6, 36], 30))
# print(two_product([1,2,3,4,5], 20))

# ==============================================================================

# task no.3 is same as 2nd

# ==============================================================================

# Task no.4 (dictionary representation and run bfs on given graph)
graph = {
    '0': ['1', '2'],
    '1': ['0', '2', '3', '5', '6'],
    '2': ['1', '3', '4', '5'],
    '3': ['0', '1', '2', '4'],
    '4': ['3', '2', '6'],
    '5': ['1', '2'],
    '6': ['1', '4']
}
visited = []
queue = []


def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)

    while queue:
        m = queue.pop(0)
        print(m, end=" ")
        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)


print("Following is the Breadth-First Search")
bfs(visited, graph, '1')

# ==============================================================================

# Task no.5 (Unioin and Intersection of sets)


def Union(s1, s2):
    return s1 | s2


def inters(s1, s2):
    return s1 & s2


set1 = {1, 2, 3}
set2 = {3, 4, 5}

print(Union(set1, set2))
print(inters(set1, set2))
