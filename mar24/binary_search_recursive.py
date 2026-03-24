# File: binary_search_recursive.py
def binary_search(arr, l, r, x):
    if l > r:
        return -1
    mid = (l + r) // 2
    if arr[mid] == x:
        return mid
    elif arr[mid] > x:
        return binary_search(arr, l, mid-1, x)
    else:
        return binary_search(arr, mid+1, r, x)

print(binary_search([1,2,3,4,5], 0, 4, 3))