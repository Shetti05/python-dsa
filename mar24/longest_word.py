# File: longest_word.py
def longest_word(s):
    return max(s.split(), key=len)

print(longest_word("I love programming in python"))