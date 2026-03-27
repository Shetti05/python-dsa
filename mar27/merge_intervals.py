def merge(intervals):
    intervals.sort()
    res = [intervals[0]]

    for i in intervals[1:]:
        if res[-1][1] < i[0]:
            res.append(i)
        else:
            res[-1][1] = max(res[-1][1], i[1])

    return res