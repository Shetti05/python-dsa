def jobScheduling(startTime, endTime, profit):
    jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
    dp = [(0, 0)]  # (endTime, profit)

    for s, e, p in jobs:
        i = binarySearch(dp, s)
        curr_profit = dp[i][1] + p
        if curr_profit > dp[-1][1]:
            dp.append((e, curr_profit))
    return dp[-1][1]

def binarySearch(dp, target):
    l, r = 0, len(dp)-1
    while l <= r:
        mid = (l+r)//2
        if dp[mid][0] <= target:
            l = mid + 1
        else:
            r = mid - 1
    return r
