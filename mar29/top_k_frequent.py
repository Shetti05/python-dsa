from collections import Counter

def topKFrequent(nums, k):
    count = Counter(nums)
    return [item for item, _ in count.most_common(k)]

print(topKFrequent([1,1,1,2,2,3], 2))