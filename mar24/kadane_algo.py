# File: kadane_algo.py
def max_subarray(arr):
    max_sum = curr = arr[0]
    for num in arr[1:]:
        curr = max(num, curr + num)
        max_sum = max(max_sum, curr)
    return max_sum

print(max_subarray([-2,1,-3,4,-1,2,1,-5,4]))