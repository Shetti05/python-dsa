def is_valid(s):
    stack = []
    mp = {')':'(', '}':'{', ']':'['}
    for c in s:
        if c in mp:
            if stack.pop() != mp[c]:
                return False
        else:
            stack.append(c)
    return not stack