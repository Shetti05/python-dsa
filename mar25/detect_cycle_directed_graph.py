def has_cycle(graph):
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

    return any(dfs(node) for node in graph)