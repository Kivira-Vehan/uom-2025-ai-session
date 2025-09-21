def find_smallest_multiple(n):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    def lcm(a, b):
        return a * b // gcd(a, b)

    smallest_multiple = 1
    for i in range(1, n + 1):
        smallest_multiple = lcm(smallest_multiple, i)
    return smallest_multiple


n = int(input("Enter a number: "))
result = find_smallest_multiple(n)
print(f"The smallest multiple evenly divisible by all numbers from 1 to {n} is: {result}")