# -------------------------------------------------------------
# PYTHON CRASH COURSE - CHAPTER 3
# -------------------------------------------------------------

# Exercise 3-1 Names

names = ["mark", "matt", "travis", "tom"]

print("--- Exercise 3-1 ---")
print(f"My friend's name is {names[0].title()}.")
print(f"My friend's name is {names[1].title()}.")
print(f"My friend's name is {names[2].title()}.")
print(f"My friend's name is {names[3].title()}.")

# Exercise 3-2 Greetings

print("\n--- Exercise 3-2 ---")
print(f"Have a great day, {names[0].title()}!")
print(f"Have a great day, {names[1].title()}!")
print(f"Have a great day, {names[2].title()}!")
print(f"Have a great day, {names[3].title()}!")

# Exercise 3-3 Your Own List

cars = ["ferrari", "lamborghini", "mclaren"]
motorcycles = ["bmw", "ducati", "YZF-R1"]  

print("\n--- Exercise 3-3 ---")
print(f"One day I will have a {cars[2].title()}")
print(f"One day I will have a {motorcycles[1].title()}")

# Exercise 3-4 Guest List

guests = ["Jesus", "david", "joseph"]

print("\n--- Exercise 3-4 ---")
print(f"Dear {guests[0].title()}, I would like to invite you to dinner")
print(f"Dear {guests[1].title()}, I would like to invite you to dinner")
print(f"Dear {guests[2].title()}, I would like to invite you to dinner")

# Exercise 3-5 Changing Guest List

print("\n--- Exercise 3-5 ---")
# Original invitations
print(f"Dear {guests[0].title()}, I would like to invite you to dinner.")
print(f"Dear {guests[1].title()}, I would like to invite you to dinner.")
print(f"Dear {guests[2].title()}, I would like to invite you to dinner.")

# Announcing who cannot attend
print(f"\nUnfortunately, {guests[2].title()} can't make it to dinner.\n")

# Modifying the list: removing Joseph and putting Peter in his place
guests[2] = "peter"

print(f"Dear {guests[0].title()}, I would like to invite you to dinner.")
print(f"Dear {guests[1].title()}, I would like to invite you to dinner.")
print(f"Dear {guests[2].title()}, I would like to invite you to dinner.")

# Exercise 3-6 More Guests

print("\n--- Exercise 3-6 ---")
print("Great news! I just found a bigger dinner table.\n")

guests.insert(0, 'james')  # beginning
guests.insert(2, 'simon')  # middle
guests.append('barth')     # end

print(f"Dear {guests[0].title()}, I would like to invite you to dinner.")
print(f"Dear {guests[1].title()}, I would like to invite you to dinner.")
print(f"Dear {guests[2].title()}, I would like to invite you to dinner.")
print(f"Dear {guests[3].title()}, I would like to invite you to dinner.")
print(f"Dear {guests[4].title()}, I would like to invite you to dinner.")
print(f"Dear {guests[5].title()}, I would like to invite you to dinner.")

# Exercise 3-7 Shrinking Guest List

print("\n--- Exercise 3-7 ---")
print("Bad news! The bigger dinner table won't arrive in time.\n")

# Removing guests until only two remain (capturing the popped guest)
popped_guest = guests.pop()
print(f"Sorry {popped_guest.title()}, I can't invite you to dinner anymore.")

popped_guest = guests.pop()
print(f"Sorry {popped_guest.title()}, I can't invite you to dinner anymore.")

popped_guest = guests.pop()
print(f"Sorry {popped_guest.title()}, I can't invite you to dinner anymore.")

popped_guest = guests.pop()
print(f"Sorry {popped_guest.title()}, I can't invite you to dinner anymore.")

print("-" * 40)

# Confirming the two remaining guests
print(f"Dear {guests[0].title()}, you are still invited to dinner!")
print(f"Dear {guests[1].title()}, you are still invited to dinner!")

# Emptying the list using 'del'
del guests[0]
del guests[0]

print("\nFinal guest list status:")
print(guests)

# Exercise 3-8 Seeing the World

places = ['sydney', 'melbourne', 'london', 'new york', 'california']

print("\n--- Exercise 3-8 ---")
print("1. Here is the original list:")
print(places)

print("\n2. Here is the sorted list:")
print(sorted(places))

print("\n3. Here is the original list again:")
print(places)

print("\n4. Here is the reverse alphabetical sorted list:")
print(sorted(places, reverse=True))

print("\n5. Here is the original list again:")
print(places)

places.reverse()
print("\n6. Here is the permanently reversed list:")
print(places)

places.reverse()
print("\n7. Here is the list back to its original order:")
print(places)

places.sort()
print("\n8. Here is the permanently sorted alphabetical list:")
print(places)

places.sort(reverse=True)
print("\n9. Here is the permanently sorted reverse alphabetical list:")
print(places)

# Exercise 3-9 Dinner Guests

print("\n--- Exercise 3-9 ---")
# Re-defining the base list to get the original count
dinner_guests = ["Jesus", "david", "joseph"]
print(f"Total number of people invited to dinner: {len(dinner_guests)}")

# Exercise 3-10 Every Function

local = ['yangtze', 'las vegas', 'croatia', 'everest', 'english']

print("\n--- Exercise 3-10 ---")
print("1. Here is the original list:")
print(local)

print("\n2. Here is the temporarily sorted list:")
print(sorted(local))

print("\n3. Here is the original list again:")
print(local)

print("\n4. Here is the temporarily sorted reverse alphabetical list:")
print(sorted(local, reverse=True))

print("\n5. Here is the original list again:")
print(local)

local.reverse()
print("\n6. Here is the permanently reversed list:")
print(local)

local.reverse()
print("\n7. Here is the list back to its original order:")
print(local)

local.sort()
print("\n8. Here is the permanently sorted alphabetical list:")
print(local)

local.sort(reverse=True)
print("\n9. Here is the permanently sorted reverse alphabetical list:")
print(local)