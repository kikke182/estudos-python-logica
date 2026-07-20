# =============================================================================
# PYTHON CRASH COURSE - CHAPTER 4: WORKING WITH LISTS & TUPLES
# =============================================================================

# -----------------------------------------------------------------------------
# Exercise 4.1 - Pizza
# -----------------------------------------------------------------------------
pizzas = ['cheese', 'bacon', 'chicken']

print("Pizza Preferences:")
for pizza in pizzas: 
    print(f"I love {pizza} pizza!")

print("I really love pizza!")

# -----------------------------------------------------------------------------
# Exercise 4.2 - Animals
# -----------------------------------------------------------------------------
animals = ['koala', 'kangaroo', 'quokkas']

print("\nAnimal Warnings:")
for animal in animals:
    print(f"The {animal} is a wild animal. Be careful!")    

print("All these animals live in Australia.")

# -----------------------------------------------------------------------------
# Exercise 4.3 - Counting to Twenty
# -----------------------------------------------------------------------------
numbers = [value for value in range(1, 21)]
print("\n4.3 Counting to Twenty:", numbers)

# -----------------------------------------------------------------------------
# Exercise 4.4 & 4.5 - One Million & Summing a Million
# -----------------------------------------------------------------------------
a_million = list(range(1, 1000001))

print("\n4.5 Summing a Million:")
print("Min:", min(a_million))
print("Max:", max(a_million))
print("Sum:", sum(a_million))

# -----------------------------------------------------------------------------
# Exercise 4.6 - Odd Numbers
# -----------------------------------------------------------------------------
odd_numbers = [value for value in range(1, 21, 2)]
print("\n4.6 Odd Numbers:", odd_numbers)

# -----------------------------------------------------------------------------
# Exercise 4.7 - Threes
# -----------------------------------------------------------------------------
threes = [value for value in range(3, 31, 3)]
print("4.7 Threes (Multiples of 3):", threes)

# -----------------------------------------------------------------------------
# Exercise 4.8 & 4.9 - Cubes & Cube Comprehension
# -----------------------------------------------------------------------------
cubes = [value**3 for value in range(1, 11)]
print("4.8/4.9 Cubes:", cubes)

# -----------------------------------------------------------------------------
# Exercise 4.10 - Slices
# -----------------------------------------------------------------------------
places = ['rio', 'london', 'ny', 'melbourne', 'amsterdam']

print("\nThe first three places in the list are:")
for place in places[:3]:
    print(place.title())

print("\nThree places from the middle of the list are:")
for place in places[1:4]:
    print(place.title())

print("\nThe last three places in the list are:")
for place in places[-3:]:
    print(place.title())

# -----------------------------------------------------------------------------
# Exercise 4.11 - My Pizzas, Your Pizzas
# -----------------------------------------------------------------------------
pizzas = ['cheese', 'bacon', 'chicken']
friend_pizzas = pizzas[:]

pizzas.append('chocolate')
friend_pizzas.append('pineapple')

print("\nMy favorite pizzas are:")
for pizza in pizzas:
    print(f"- {pizza.title()}")

print("\nMy friend's favorite pizzas are:")
for friend_pizza in friend_pizzas:
    print(f"- {friend_pizza.title()}")
    
# -----------------------------------------------------------------------------
# Exercise 4.12 - More Loops
# -----------------------------------------------------------------------------
foods = ['hamburger', 'hot dog', 'taco', 'ice cream', 'fries']
friend_foods = foods[:]

print("\nMy favorite foods are:")
for food in foods:
    print(f"- {food.title()}")

print("\nMy friend's favorite foods are:")
for friend_food in friend_foods:
    print(f"- {friend_food.title()}")

# -----------------------------------------------------------------------------
# Exercise 4.13, 4.14 & 4.15 - Buffet & PEP 8 Code Review
# -----------------------------------------------------------------------------
buffet_foods = ('sushi', 'bbq', 'pasta', 'hamburger', 'fruit')

print("\Original menu:")
for food in buffet_foods:
    print(f"- {food.title()}")

# Intentional Assignment Error Test (PEP 8 Commented out for execution):
# buffet_foods[0] = 'fries'

# Overwriting the tuple to adjust the menu items cleanly
buffet_foods = ('sushi', 'bbq', 'pasta', 'chicken', 'tacos')

print("\nModified menu:")
for food in buffet_foods:
    print(f"- {food.title()}")

# -----------------------------------------------------------------------------
# Chapter Examples: Dimensions & Squares (Refactored for Clean Structure)
# -----------------------------------------------------------------------------
dimensions = (200, 50)

print("\nOriginal dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)

print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)

# Calculating numerical squares
squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)

print("\nCalculated squares:")
print(squares)