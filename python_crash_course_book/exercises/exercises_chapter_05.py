# =============================================================================
# PYTHON CRASH COURSE - CHAPTER 5: IF STATEMENTS
# =============================================================================

# -----------------------------------------------------------------------------
# 5.1 & 5.2 Conditional Tests
# -----------------------------------------------------------------------------
rock_bands = ['blink-182', 'linkin park', 'green day', 'foo fighters']
my_favorite = 'blink-182'

# True Tests
print(f"1. Is my_favorite == 'blink-182'? {my_favorite == 'blink-182'}")
print(f"2. Is 'green day' in rock_bands? {'green day' in rock_bands}")
print(f"3. Is 'linkin park' != 'blink-182'? {'linkin park' != my_favorite}")
print(f"4. Is 20 < 23? {20 < 23}")
print(f"5. Is 'a7x' not in rock_bands? {'a7x' not in rock_bands}")

# False Tests
print(f"\n6. Is my_favorite == 'foo fighters'? {my_favorite == 'foo fighters'}")
print(f"7. Is 'queen' in rock_bands? {'queen' in rock_bands}")
print(f"8. Is 'linkin park' == 'blink-182'? {my_favorite == 'linkin park'}")
print(f"9. Is 20 > 23? {20 > 23}")
print(f"10. Is 'blink-182' not in rock_bands? {'blink-182' not in rock_bands}")

# -----------------------------------------------------------------------------
# 5.3 Alien Colors & 5.6 Stages of Life
# -----------------------------------------------------------------------------
age = 100
if age < 2:
    print("\nIt's a baby!")
elif age < 4:
    print("\nIt's a toddler!")
elif age < 13:
    print("\nIt's a kid!")
elif age < 20:
    print("\nIt's a teenager!")
elif age < 65:
    print("\nIt's an adult!")
else:
    print("\nIt's an elder!")

# -----------------------------------------------------------------------------
# 5.7 Favorite Fruit
# -----------------------------------------------------------------------------
favorite_fruits = ['strawberry', 'orange', 'passion fruit']

for fruit in ['strawberry', 'orange', 'passion fruit', 'banana', 'apple']:
    if fruit in favorite_fruits:
        print(f"You really like {fruit}!")

# -----------------------------------------------------------------------------
# 5.8 Hello Admin & 5.9 No Users
# -----------------------------------------------------------------------------
staff = ['john', 'mark', 'scot', 'admin', 'jaden']

if staff:
    for user in staff:
        if user == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {user}, thank you for logging in again.")
else:
    print("We need to find some users!")

# -----------------------------------------------------------------------------
# 5.10 Checking Usernames
# -----------------------------------------------------------------------------
current_users = ['smith', 'keanu', 'travis', 'scott', 'dave']
new_users = ['brian', 'dave']

# Convert current_users to lowercase for case-insensitive comparison
current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"The name '{new_user}' is already taken.")
    else:
        print(f"The name '{new_user}' is available.")
        current_users.append(new_user)

print(f"\nUpdated list: {current_users}")

# -----------------------------------------------------------------------------
# 5.11 Ordinal Numbers
# -----------------------------------------------------------------------------
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for number in numbers:
    if number == 1:
        print("1st")
    elif number == 2:
        print("2nd")
    elif number == 3:
        print("3rd")
    else:
        print(f"{number}th")