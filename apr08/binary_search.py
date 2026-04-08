arr = [1,2,3,4,5]
target = 4

l, r = 0, len(arr)-1

while l <= r:
    mid = (l + r) // 2
    if arr[mid] == target:
        print(mid)
        break
    elif arr[mid] < target:
        l = mid + 1
    else:
        r = mid - 1