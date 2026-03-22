# File: detect_cycle_directed.py
def hasCycle(graph):
    visited = set()
    rec = set()

    def dfs(node):
        if node in rec:
            return True
        if node in visited:
            return False

        visited.add(node)
        rec.add(node)
        for nei in graph[node]:
            if dfs(nei):
                return True
        rec.remove(node)
        return False

    return any(dfs(n) for n in graph)

graph = {0:[1], 1:[2], 2:[0]}
print(hasCycle(graph))