from collections import Counter

def minWindow(s, t):
    need = Counter(t)
    have = {}
    res = ""
    l = 0
    formed = 0

    for r in range(len(s)):
        c = s[r]
        have[c] = have.get(c, 0) + 1

        if c in need and have[c] == need[c]:
            formed += 1

        while formed == len(need):
            if res == "" or (r - l + 1) < len(res):
                res = s[l:r+1]

            have[s[l]] -= 1
            if s[l] in need and have[s[l]] < need[s[l]]:
                formed -= 1
            l += 1

    return res