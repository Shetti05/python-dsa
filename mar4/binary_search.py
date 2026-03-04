arr = [1,2,3,4,5,6,7]
target = 5

left = 0
right = len(arr)-1

while left <= right:
    mid = (left + right)//2

    if arr[mid] == target:
        print("Found at index", mid)
        break
    elif arr[mid] < target:
        left = mid + 1
    else:
        right = mid - 1