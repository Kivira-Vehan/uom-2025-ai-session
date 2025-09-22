def find_pythagorean_triplet(sum_value):
    for a in range(1, sum_value):
        for b in range(a, sum_value - a):
            c = sum_value - a - b
            if a**2 + b**2 == c**2:
                return a, b, c
    return None

sum_value = int(input("Enter the sum value (e.g., 1000): "))
triplet = find_pythagorean_triplet(sum_value)
if triplet:
    a, b, c = triplet
    product = a * b * c
    print(f"The Pythagorean triplet is: a={a}, b={b}, c={c}")
    print(f"The product abc is: {product}")
else:
    print("No Pythagorean triplet found for the given sum value.")
    