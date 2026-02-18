from collections import Counter

nums = [1,1,1,2,2,3]
k = 2

count = Counter(nums)
result = sorted(count, key=count.get, reverse=True)[:k]

print("Top K Frequent:", result)
