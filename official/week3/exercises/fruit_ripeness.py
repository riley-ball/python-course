# Importing the random library to generate random fruits and their ripeness level
import random

# List of fruits and their ripeness level (1 to 5, 5 being fully ripe)
fruits = {
    "apple": random.randint(1, 5),
    "banana": random.randint(1, 5),
    "cherry": random.randint(1, 5),
    "date": random.randint(1, 5),
    "elderberry": random.randint(1, 5),
    "fig": random.randint(1, 5),
    "grape": random.randint(1, 5),
}

fruit, ripeness = random.choice(list(fruits.items()))
print(f"Selected Fruit: {fruit}")
print(f"Ripeness Level: {ripeness}")

# --------------------------
# Exercise: Classify the given fruit based on its ripeness.
# - If the ripeness is 1 or 2, print "Not Ripe"
# - If the ripeness is 3, print "Ripe"
# - If the ripeness is 4 or 5, print "Overripe"
# - If the fruit is "banana" and ripeness is 5, print "Very Overripe Banana"
# - If the fruit is "apple" and ripeness is 1, print "Green Apple"
# - For any other condition, print "Unknown Ripeness"
#
# Hint: Use multiple if and elif statements to classify the ripeness.
# TODO: Write your code below this line

# TODO: Write your code above this line
# --------------------------
