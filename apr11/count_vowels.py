s = "hello world"
count = sum(1 for c in s if c in "aeiou")
print(count)