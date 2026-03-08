def intersection(nums1, nums2):
    return list(set(nums1) & set(nums2))


a = [1,2,2,1]
b = [2,2]

print(intersection(a, b))