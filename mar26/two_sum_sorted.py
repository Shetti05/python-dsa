def two_sum_sorted(nums, target):
    l, r = 0, len(nums) - 1
    while l < r:
        s = nums[l] + nums[r]
        if s == target:
            return [l, r]
        elif s < target:
            l += 1
        else:
            r -= 1
    return []

print(two_sum_sorted([1,2,3,4,6], 6))