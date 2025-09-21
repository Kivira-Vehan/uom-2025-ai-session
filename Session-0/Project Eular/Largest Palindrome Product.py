def find_pilindrome(num):
    return str(num) == str(num)[::-1]


def largest_palindrome_product(n):
    max_palindrome = 0
    for i in range(10**(n-1), 10**n):
        for j in range(i, 10**n):
            product = i * j
            if find_pilindrome(product) and product > max_palindrome:
                max_palindrome = product
    return max_palindrome

n = int(input("Enter the number of digits: "))
result = largest_palindrome_product(n)
print(f"The largest palindrome made from the product of two {n}-digit numbers is: {result}")