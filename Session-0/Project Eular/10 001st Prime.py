def find_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def nth_prime(n):
    count = 0
    num = 1
    while count < n:
        num += 1
        if find_prime(num):
            count += 1
    return num

n = int(input("Enter the value of n: "))
result = nth_prime(n)
print(f"The {n}th prime number is: {result}")