n = 84
i = 2
while i <= n:
    if n % i == 0:
        print(i, end=" ")
        n //= i
    else:
        i += 1