# File: subarray_sum.py
def subarray_sum(arr, target):
    res = []
    for i in range(len(arr)):
        s = 0
        for j in range(i, len(arr)):
            s += arr[j]
            if s == target:
                res.append((i, j))
    return res

print(subarray_sum([1,2,3,4,5], 5))