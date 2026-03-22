# File: word_ladder.py
from collections import deque

def ladderLength(beginWord, endWord, wordList):
    wordSet = set(wordList)
    q = deque([(beginWord, 1)])

    while q:
        word, steps = q.popleft()
        if word == endWord:
            return steps

        for i in range(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                new = word[:i] + c + word[i+1:]
                if new in wordSet:
                    wordSet.remove(new)
                    q.append((new, steps+1))
    return 0

print(ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"]))