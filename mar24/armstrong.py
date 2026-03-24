# File: armstrong.py
def is_armstrong(n):
    power = len(str(n))
    return n == sum(int(d)**power for d in str(n))

print(is_armstrong(153))