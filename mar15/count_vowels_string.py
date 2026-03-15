def count_vowels(s):
    vowels = "aeiou"
    return sum(1 for c in s.lower() if c in vowels)

print(count_vowels("programming"))