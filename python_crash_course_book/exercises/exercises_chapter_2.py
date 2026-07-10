# =============================================================================
# PYTHON CRASH COURSE - CHAPTER 2: VARIABLES AND SIMPLE DATA TYPES
# =============================================================================

# -----------------------------------------------------------------------------
# Exercise 2.1 - Simple Message
# -----------------------------------------------------------------------------
message = "Hello Python World!"
print(message)


# -----------------------------------------------------------------------------
# Exercise 2.2 - Simple Messages
# -----------------------------------------------------------------------------
message = "Hello Python World!"
print(message)

message = "A new future begins!"
print(message)


# -----------------------------------------------------------------------------
# Exercise 2.3 - Personal Message
# -----------------------------------------------------------------------------
user_name = "Henrique"
print(f"Hello {user_name}, would you like to learn some Python today?")


# -----------------------------------------------------------------------------
# Exercise 2.4 - Name Cases
# -----------------------------------------------------------------------------
person = "Blink-182"
print(person.upper())
print(person.lower())
print(person.title())


# -----------------------------------------------------------------------------
# Exercise 2.5, 2.6 & 2.11 - Famous Quote & Adding Comments
# -----------------------------------------------------------------------------
# Note: Combined the famous quote exercises to practice clean variables,
# maintainable structural code, and clear inline documentation.
famous_person = "henry ford"
message = (
    f"\nFailure is simply the opportunity to begin again, "
    f"this time more intelligently.\n\t{famous_person.title()}"
)
print(message)


# -----------------------------------------------------------------------------
# Exercise 2.7 - Stripping Names
# -----------------------------------------------------------------------------
most_famous_artist = " michael jackson "

# 1. Left strip (Removes whitespaces from the left side)
artist_message = (
    f"\n\t{most_famous_artist.title().lstrip()} "
    f"is the most famous artist of all time!"
)
print(artist_message)

# 2. Right strip (Removes whitespaces from the right side)
artist_message = (
    f"\n\t{most_famous_artist.title().rstrip()} "
    f"is the most famous artist of all time!"
)
print(artist_message)

# 3. Full strip (Removes whitespaces from both sides)
artist_message = (
    f"\n\t{most_famous_artist.title().strip()} "
    f"is the most famous artist of all time!"
)
print(artist_message)


# -----------------------------------------------------------------------------
# Exercise 2.8 - File Extensions
# -----------------------------------------------------------------------------
simple_url = "https://google.com"
simple_url = simple_url.removeprefix("https://")
print(simple_url)


# -----------------------------------------------------------------------------
# Exercise 2.9 - Number Eight
# -----------------------------------------------------------------------------
print(2 * 4)
print(40 / 5)
print(4 + 4)
print(12 - 4)
print(2 ** 3)


# -----------------------------------------------------------------------------
# Exercise 2.10 - Favorite Number
# -----------------------------------------------------------------------------
number = 10
print(f"My favorite number is {number}")


# -----------------------------------------------------------------------------
# Exercise 2.12 - Zen of Python
# -----------------------------------------------------------------------------
print("--- The Zen of Python ---")
import this  # Automatically prints the Zen of Python principles in terminal

# The Zen of Python reference checklist for documentation purposes:
#
# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.
# Flat is better than nested.
# Sparse is better than dense.
# Readability counts.
# Special cases aren't special enough to break the rules.
# Although practicality beats purity.
# Errors should never pass silently.
# Unless explicitly silenced.
# In the face of ambiguity, refuse the temptation to guess.
# There should be one-- and preferably only one --obvious way to do it.
# Although that way may not be obvious at first unless you're Dutch.
# Now is better than never.
# Although never is often better than *right* now.
# If the implementation is hard to explain, it's a bad idea.
# If the implementation is easy to explain, it may be a good idea.
# Namespaces are one honking great idea -- let's do more of those!