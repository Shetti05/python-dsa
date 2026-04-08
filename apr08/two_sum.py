arr = [2, 7, 11, 15]
target = 9

d = {}

for i, num in enumerate(arr):
    if target - num in d:
        print(d[target - num], i)
        break
    d[num] = i