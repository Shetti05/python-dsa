def merge(intervals):
    intervals.sort()
    res = [intervals[0]]
    
    for start, end in intervals[1:]:
        if start <= res[-1][1]:
            res[-1][1] = max(res[-1][1], end)
        else:
            res.append([start, end])
    return res

print(merge([[1,3],[2,6],[8,10],[15,18]]))