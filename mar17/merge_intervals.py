def merge(intervals):
    intervals.sort()
    res = [intervals[0]]

    for curr in intervals[1:]:
        if curr[0] <= res[-1][1]:
            res[-1][1] = max(res[-1][1], curr[1])
        else:
            res.append(curr)

    return res