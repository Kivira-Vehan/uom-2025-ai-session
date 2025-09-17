## Given x (int) print a christmas tree of height x
def print_christmas_tree(x):
    for i in range(x):
        print(" " * (x - i - 1) + "*" * (2 * i + 1))

## x0 = "apple", y0 = "adcsjncjsppaxjjnaxle" --> True if all characters of x0 are in y0 in order, y0 = "bsdpple" --> False, y0 = "paple" --> False
def is_subsequence(x0, y0):
        i = 0  # pointer for x0
        for letter in y0:
            if i < len(x0) and x0[i] == letter:
                i += 1
        return i == len(x0)


x= int(input("Enter Height: "))
print_christmas_tree(x)
print(is_subsequence("apple", "adcsjncjsppaxjjnaxle"))  