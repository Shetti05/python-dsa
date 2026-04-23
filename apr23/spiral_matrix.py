def spiral(matrix):
    res = []
    while matrix:
        res += matrix.pop(0)
        matrix = list(zip(*matrix))[::-1]
    return res

print(spiral([[1,2,3],[4,5,6],[7,8,9]]))