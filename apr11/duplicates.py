arr = [1,2,3,2,4,1]
seen = set()
for num in arr:
    if num in seen:
        print(num)
    else:
        seen.add(num)