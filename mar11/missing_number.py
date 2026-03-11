def find_missing(arr, n):
    expected = n*(n+1)//2
    return expected - sum(arr)

print(find_missing([1,2,4,5],5))