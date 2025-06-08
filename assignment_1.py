# Taking the input from user
n = int(input("Enter the number of rows: "))

# Code for the Lower Triangular Pattern
print("\nLower Triangular Pattern:")
for i in range(1, n+1):
    print("* " * i)

# Code for the Upper Triangular Pattern
print("\nUpper Triangular Pattern:")
for i in range(n, 0, -1):
    print("* " * i)

# Code for the Pyramid Pattern
print("\nPyramid Pattern:")
for i in range(1, n+1):
    print(" " * (n - i) + "* " * i)
