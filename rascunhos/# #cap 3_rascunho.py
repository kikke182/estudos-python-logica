# #cap 3

# # motorcycles = []
# # motorcycles.append('honda')
# # motorcycles.append('ducati')
# # motorcycles.append('yamaha')

# # print(motorcycles)
# #insert
# # motorcycles =['honda', 'ducati', 'yamaha']
# # motorcycles.insert(0, 'yamaha')
# # print(motorcycles)

# #del - delete
# # motorcycles =['honda', 'ducati', 'yamaha']
# # print(motorcycles)
# # del motorcycles[0]
# # print(motorcycles)

# #removendo com pop
# # motorcycles =['honda', 'ducati', 'yamaha']
# # print(motorcycles)
# # popped_motorcycles = motorcycles.pop()
# # print(popped_motorcycles)

# #pop exemplos
# # motorcycles =['honda', 'ducati', 'yamaha']

# # last_owned = motorcycles.pop()
# # print(f"The last motorcycle I owned was a {last_owned.title()}")

# # motorcycles =['honda', 'ducati', 'yamaha']

# # last_owned = motorcycles.pop(0)
# # print(f"The last motorcycle I owned was a {last_owned.title()}")

# #3-5 Changing Guest List:

# # new_guests = ["Jesus", "david", "joseph"]
# # print(new_guests)
# # popped_new_guests = new_guests.pop()
# # print(popped_new_guests)
# # new_guests.insert(2, 'peter')
# # print(new_guests)
# # print(f"Dear {new_guests[0].title()}, I would like to invite you to dinner")
# # print(f"Dear {new_guests[1].title()}, I would like to invite you to dinner")
# # print(f"Dear {new_guests[2].title()}, I would like to invite you to dinner")

# # # Exercise 3-7: Shrinking Guest List

# # guests = ["Jesus", "david", "peter"]
# # print("Bad news! The bigger dinner table can arrived today.\n")

# # guests.insert(0, 'james')  
# # guests.insert(2, 'simon')  
# # guests.append('barth')    
# # print(f"Sorry {guests[5].title()}, the dinner is canceled.")
# # guests.pop(5)
# # print(f"Sorry {guests[4].title()}, the dinner is canceled.")
# # guests.pop(4)
# # print(f"Sorry {guests[3].title()}, the dinner is canceled.")
# # guests.pop(3)
# # print(f"Sorry {guests[2].title()}, the dinner is canceled.")
# # guests.pop(2)

# # print(guests)

# # # O jeito mais pratico:

# # guests = ["james", "Jesus", "simon", "david", "peter", "barth"]
# # print("Bad news! The bigger dinner table won't arrive in time.\n")

# # # Um loop 'while' que roda AUTOMATICAMENTE até sobrarem só 2 pessoas
# # while len(guests) > 2:
# #     removed_guest = guests.pop()
# #     print(f"Sorry {removed_guest.title()}, I can't invite you to dinner anymore.")

# # print("-" * 40)

# # # Um loop 'for' que manda o convite para quem sobrou, sem digitar print um por um
# # for guest in guests:
# #     print(f"Dear {guest.title()}, you are still invited to dinner!")

# # # Limpando a lista inteira com uma única palavra
# # guests.clear()

# # print("\nFinal list:", guests)

# #sort - em ordem alfabetica
# # cars = ['bmw', 'audi', 'toyota', 'subaru']
# # cars.sort()
# # print(cars)

# #reverse=True - na ordem reversa
# # cars = ['bmw', 'audi', 'toyota', 'subaru']
# # cars.sort(reverse=True)
# # print(cars)

# #sorted()
# # cars = ['bmw', 'audi', 'toyota', 'subaru']
# # print('Here is the original list:')
# # print(cars)
# # print('\nHere is the sorted list:')
# # print(sorted(cars))
# # print('\nHere is the original list again:')
# # print(cars)

# #reverse
# # cars = ['bmw', 'audi', 'toyota', 'subaru']
# # cars.reverse()
# # print(cars)

# #len
# cars = ['bmw', 'audi', 'toyota', 'subaru']
# print(len(cars))

# # 3-8. Seeing the World

# places = ['sydney', 'melbourne', 'london','new york', 'california']
# print('Here is the list:')
# print(places)

# places = ['sydney', 'melbourne', 'london','new york', 'california']
# print('\nHere is the sorted list:')
# print(sorted(places))

# places = ['sydney', 'melbourne', 'london','new york', 'california']
# print('\nHere is the original list:')
# print(places)

# places = ['sydney', 'melbourne', 'london','new york', 'california']
# print('Here is the revers list:')
# places.sort(reverse=True)
# print(places)

# places = ['sydney', 'melbourne', 'london','new york', 'california']
# print('\nHere is the original list again:')
# print(places)

# places = ['sydney', 'melbourne', 'london','new york', 'california']
# print('Here is the reverse list:')
# places.sort(reverse=True)
# print(places)

# places = ['sydney', 'melbourne', 'london','new york', 'california']
# print('Here is the reverse:')
# places.reverse()
# print(places)

# places = ['sydney', 'melbourne', 'london','new york', 'california']
# print('Here is the reverse list:')
# places.sort(reverse=False)
# print(places)

# places = ['sydney', 'melbourne', 'london','new york', 'california']
# print('Here is the sort list:')
# places.sort()
# print(places)

# places = ['sydney', 'melbourne', 'london','new york', 'california']
# print('Here is the  list:')
# places.reverse()
# print(places)

# # -------------------------------------------------------------
# # PYTHON CRASH COURSE - CHAPTER 3
# # -------------------------------------------------------------

# # Exercise 3-1 Names

# names = ["mark", "matt", "travis", "tom"]

# print(f"My friend's name is {names[0].title()}.")
# print(f"My friend's name is {names[1].title()}.")
# print(f"My friend's name is {names[2].title()}.")
# print(f"My friend's name is {names[3].title()}.")

# # Exercise 3-2 Greetings

# names = ["mark", "matt", "travis", "tom"]

# print(f"Have a great day, {names[0].title()}!")
# print(f"Have a great day, {names[1].title()}!")
# print(f"Have a great day, {names[2].title()}!")
# print(f"Have a great day, {names[3].title()}!")

# # Exercise 3-3 Your Own List

# cars = ["ferrari", "lamborghini", "mclaren"]
# motorcycles = ["bmw", "ducati", "YZF-R1"]  

# print(f"One day I will have a {cars[2].title()}")
# print(f"One day I will have a {motorcycles[1].title()}")

# # Exercise 3-4 Guest List

# guests = ["Jesus", "david", "joseph"]

# print(f"Dear {guests[0].title()}, I would like to invite you to dinner")
# print(f"Dear {guests[1].title()}, I would like to invite you to dinner")
# print(f"Dear {guests[2].title()}, I would like to invite you to dinner")

# #Exercise 3-5 Changing Guest List

# # Original guest list
# guests = ["Jesus", "david", "joseph"]

# # Original invitations
# print(f"Dear {guests[0].title()}, I would like to invite you to dinner.")
# print(f"Dear {guests[1].title()}, I would like to invite you to dinner.")
# print(f"Dear {guests[2].title()}, I would like to invite you to dinner.")

# # Announcing who cannot attend (using the name directly from the list)
# print(f"\nUnfortunately, {guests[2].title()} can't make it to dinner.\n")

# # Modifying the list: removing Joseph and putting Peter in his place (2)
# guests[2] = "peter"

# print(f"Dear {guests[0].title()}, I would like to invite you to dinner.")
# print(f"Dear {guests[1].title()}, I would like to invite you to dinner.")
# print(f"Dear {guests[2].title()}, I would like to invite you to dinner.")

# # Exercise 3-6 More Guests

# # 1. Starting list from exercise 3-5
# guests = ["Jesus", "david", "peter"]
# print("Great news! I just found a bigger dinner table.\n")

# guests.insert(0, 'james')  # beginning
# guests.insert(2, 'simon')  # middle
# guests.append('barth')     # end

# print(f"Dear {guests[0].title()}, I would like to invite you to dinner.")
# print(f"Dear {guests[1].title()}, I would like to invite you to dinner.")
# print(f"Dear {guests[2].title()}, I would like to invite you to dinner.")
# print(f"Dear {guests[3].title()}, I would like to invite you to dinner.")
# print(f"Dear {guests[4].title()}, I would like to invite you to dinner.")
# print(f"Dear {guests[5].title()}, I would like to invite you to dinner.")

# # Exercise 3-7 Shrinking Guest List

# # 1. Starting list from exercise 3-6
# guests = ["Jesus", "david", "peter"]
# print("Bad news! The bigger dinner table won't arrive in time.\n")

# # Adding the extra guests from before
# guests.insert(0, 'james')  
# guests.insert(2, 'simon')  
# guests.append('barth')    

# # 2. Removing guests until only two remain (always popping the last one)
# print(f"Sorry {guests[-1].title()}, I can't invite you to dinner anymore.")
# guests.pop()

# print(f"Sorry {guests[-1].title()}, I can't invite you to dinner anymore.")
# guests.pop()

# print(f"Sorry {guests[-1].title()}, I can't invite you to dinner anymore.")
# guests.pop()

# print(f"Sorry {guests[-1].title()}, I can't invite you to dinner anymore.")
# guests.pop()

# print("-" * 40)

# # 3. Confirming the two remaining guests
# print(f"Dear {guests[0].title()}, you are still invited to dinner!")
# print(f"Dear {guests[1].title()}, you are still invited to dinner!")

# # 4. Emptying the list using 'del'
# # When you delete index 0, the next item shifts to position 0!
# del guests[0]
# del guests[0]

# # 5. Printing the list to prove it's empty
# print("\nFinal guest list status:")
# print(guests)

# # 3-8 Seeing the World

# # 1. Original list (declared ONLY ONCE)
# places = ['sydney', 'melbourne', 'london', 'new york', 'california']
# print("1. Here is the original list:")
# print(places)

# # 2. Alphabetical order without modifying the original list
# print("\n2. Here is the sorted list:")
# print(sorted(places))

# # 3. Proving the original list is still intact
# print("\n3. Here is the original list again:")
# print(places)

# # 4. Reverse alphabetical order without modifying the original list
# print("\n4. Here is the reverse alphabetical sorted list:")
# print(sorted(places, reverse=True))

# # 5. Proving the original list is still intact again
# print("\n5. Here is the original list again:")
# print(places)

# # 6. Changing the order permanently using reverse()
# places.reverse()
# print("\n6. Here is the permanently reversed list:")
# print(places)

# # 7. Using reverse() again to go back to the original order
# places.reverse()
# print("\n7. Here is the list back to its original order:")
# print(places)

# # 8. Changing to permanent alphabetical order using sort()
# places.sort()
# print("\n8. Here is the permanently sorted alphabetical list:")
# print(places)

# # 9. Changing to permanent reverse alphabetical order using sort(reverse=True)
# places.sort(reverse=True)
# print("\n9. Here is the permanently sorted reverse alphabetical list:")
# print(places)

# # 3-9 Dinner Guests

# # Defining the guest list explicitly to ensure the count is accurate
# guests = ["Jesus", "david", "joseph"]

# # Printing the formatted message with the correct count
# print(f"Total number of people invited to dinner: {len(guests)}")

# #3-10 Every Function

# local = ['yangtze', 'las vegas', 'croatia', 'everest', 'english']
# print("\n1. Here is the original list:")
# print(local)
# print("\n2. Here is the sorted list:")
# print(sorted(local))
# print("\n3. Here is the original list again:")
# print(local)
# print("\n4. Here is the reverse alphabetical sorted list:")
# print(sorted(local,reverse=True))
# print("\n5. Here is the original list again:")
# print(local)
# local.reverse()
# print("\n6. Here is the reverse list:")
# print(local)
# local.reverse()
# print("\n7. Here is the list back to its original order:")
# print(local)
# local.sort()
# print("\n8. Here is the original list again:")
# print(local)
# local.sort(reverse=True)
# print("\n9. Here is the permanently sorted reverse alphabetical list:")
# print(local)