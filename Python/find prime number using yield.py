def find_prime_number(n):
    for i in range(2, n + 1):
        is_prime = True
        for j in range(2, int(i) + 1):
            if i % j == 0:
                is_prime = False
                    
        if is_prime:
            yield i
n = int(input("Enter a positive integer: "))
for value in find_prime_number(n):
    print(value)

