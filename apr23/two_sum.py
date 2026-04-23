def two_sum(arr, target):
    d = {}
    for i, num in enumerate(arr):
        if target - num in d:
            return [d[target-num], i]
        d[num] = i
    return [-1,-1]

print(two_sum([2,7,11,15],9))