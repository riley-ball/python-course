# Exercise: Print all the even numbers from a given list.

# List of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Print even numbers
for num in numbers:
    if num % 2 == 0:
        print("Even number:", num)
        break
