# Exercise: Create a list of squares for numbers from 1 to 10 and print the list.

# A square is the result of multiplying a number by itself. e.g. 4 squared is 4 * 4 = 16.

# Create list of squares
squares = []
for i in range(1, 11):
    square = i ** 2
squares.append(square)

# Print the list
print("List of squares from 1 to 10:", squares)

# Example output
# List of squares from 1 to 10: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]