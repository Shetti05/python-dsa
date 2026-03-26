from collections import Counter

def top_k(nums, k):
    return [item for item, _ in Counter(nums).most_common(k)]

print(top_k([1,1,1,2,2,3], 2))