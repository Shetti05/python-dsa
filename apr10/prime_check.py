n = 29
is_prime = True
for i in range(2, n//2):
    if n % i == 0:
        is_prime = False
        break
print(is_prime)