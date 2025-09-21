def find_multiples(limit):
    multiples = []
    for num in range(limit):
        if num % 3 == 0 or num % 5 == 0:
            multiples.append(num)
    return multiples

def sum_of_multiples(limit):
    multiples = find_multiples(limit)
    return sum(multiples)

limit = int(input("Enter a limit: "))
result = sum_of_multiples(limit)
print(f"The sum of multiples of 3 or 5 below {limit} is: {result}")

