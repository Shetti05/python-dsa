mat = [[1,2,3],[4,5,6],[7,8,9]]
res = []

while mat:
    res += mat.pop(0)
    mat = list(zip(*mat))[::-1]

print(res)