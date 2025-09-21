def find_prime_factors(n):
    factors = []

    while n % 2 == 0:
        factors.append(2)
        n //= 2

    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i

    if n > 2:
        factors.append(n)
    return factors

def largest_prime_factor(n):
    factors = find_prime_factors(n)
    return max(factors) 

number = int(input("Enter a number: "))
result = largest_prime_factor(number)
print(f"The largest prime factor of {number} is: {result}")