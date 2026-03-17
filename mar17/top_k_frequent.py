from collections import Counter
import heapq

def top_k(nums, k):
    count = Counter(nums)
    return heapq.nlargest(k, count.keys(), key=count.get)