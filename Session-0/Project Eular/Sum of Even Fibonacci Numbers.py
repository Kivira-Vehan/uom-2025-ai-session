def find_fibonacci(limit):
    fibonacci = [0, 1]
    while True:
        next_fib = fibonacci[-1] + fibonacci[-2]
        if next_fib >= limit:
            break
        fibonacci.append(next_fib)
    return fibonacci

def sum_of_even_fibonacci(limit):
    fibonacci = find_fibonacci(limit)
    even_fib = []
    for num in fibonacci:
        if num % 2 == 0:
            even_fib.append(num)
    return sum(even_fib)

limit = int(input("Enter a limit: "))
result = sum_of_even_fibonacci(limit)
print(f"The sum of even Fibonacci numbers below {limit} is: {result}")