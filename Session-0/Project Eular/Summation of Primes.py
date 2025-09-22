def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def sum_of_primes_below(limit):
    total = 0
    for num in range(2, limit):
        if is_prime(num):
            total += num
    return total

limit = 2000000
result = sum_of_primes_below(limit)
print(f"The sum of all primes below {limit} is: {result}")