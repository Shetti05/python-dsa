def rotate(mat):
    n = len(mat)

    # transpose
    for i in range(n):
        for j in range(i, n):
            mat[i][j], mat[j][i] = mat[j][i], mat[i][j]

    # reverse rows
    for row in mat:
        row.reverse()