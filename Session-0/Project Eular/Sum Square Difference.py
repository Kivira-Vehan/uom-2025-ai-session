def sum_of_squares(n):
    return sum(i**2 for i in range(1, n + 1))

def square_of_sum(n):
    return sum(range(1, n + 1))**2

def difference(n):
    return square_of_sum(n) - sum_of_squares(n) 

n = int(input("Enter a number: "))
result = difference(n)  
print(f"The difference between the square of the sum and the sum of the squares for the first {n} natural numbers is: {result}")