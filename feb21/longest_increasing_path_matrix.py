def longestIncreasingPath(matrix):
    rows, cols = len(matrix), len(matrix[0])
    dp = [[0]*cols for _ in range(rows)]

    def dfs(r, c):
        if dp[r][c]:
            return dp[r][c]

        val = matrix[r][c]
        max_path = 1

        for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
            nr, nc = r+dr, c+dc
            if 0 <= nr < rows and 0 <= nc < cols and matrix[nr][nc] > val:
                max_path = max(max_path, 1 + dfs(nr, nc))

        dp[r][c] = max_path
        return max_path

    return max(dfs(r, c) for r in range(rows) for c in range(cols))