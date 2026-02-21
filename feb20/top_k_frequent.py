from collections import Counter
import heapq

def top_k_frequent(nums, k):
    count = Counter(nums)
    return heapq.nlargest(k, count.keys(), key=count.get)

if __name__ == "__main__":
    arr = [1,1,1,2,2,3]
    print(top_k_frequent(arr, 2))