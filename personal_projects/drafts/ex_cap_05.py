# cars = ['audi', 'bmw', 'subaru', 'toyota']

# for car in cars:
#     if car =='bmw':
#         print(car.upper())
#     else:
#         print(car.title())

# requested_topping = 'mushroom'

# if requested_topping != 'anchovies':
#     print("Hold the anchovies!")

# answer = 17
# if answer != 42:
#     print("That is not the correct answer. Please try again!")

# age = 19 
# age < 21

# age <= 21

# age > 21 

# age >= 21

# print(age)

# age_0 = 22 
# age_1 = 18

# age_0 >= 21 and age_1 >= 21

# age_1 = 22 
# age_0 >= 21 and age_1 >= 21

# car_list = "subaru"
# print("Is car == 'subaru'? I predict True.")
# print(car_list == 'subaru')
# car  = 'subaru' or car == 'subaru'
# car  = 'subaru' and car == 'subaru'
# car = 'subaru'

# if car in car:
#     print(f"{car.title()}, is on the list!")

# car_list_2 = "toyota"
# print("\n Is car == 'toyota'? I predict False")
# print(car == 'toyota')

# car  == 'toyota' or car_list_2 = 'subaru'
# car  == 'toyota' and car_list_2 = 'subaru'

# if car not in car_list_2:
#     print(f"{car.title()}, is not on the list!")

# age = 12 
# if age <= 4:
#     print("Your admission cost is $0")
# elif age <= 18:
#     print("Your admission cost $25")
# else:
#     print("Your admission cost is $40")

# age = 12 
# if age <= 4:
#     price = 0
# elif age <= 18:
#     price = 25
# else:
#     price = 40
# print(f"Your admission cost is {price}")

# age = 12 
# if age <= 4:
#     price = 0
# elif age <= 18:
#     price = 25
# elif age < 65:
#     price = 40
# elif age >= 65:
#     price = 40
# print(f"Your admission cost is {price}")

# requested_toppings = ["mushrooms", "extra cheese"]

# if 'mushrooms' in requested_toppings:
#     print("Adding mushrooms.")
# if 'pepperoni' in requested_toppings:
#     print("Adding pepperoni.")
# if 'extra cheese' in requested_toppings:
#     print("Adding extra cheese.")

# print('\nFinished making your pizza!')

# requested_toppings = ["mushrooms", "extra cheese"]

# if 'mushrooms' in requested_toppings:
#     print("Adding mushrooms.")
# elif 'pepperoni' in requested_toppings:
#     print("Adding pepperoni.")
# elif 'extra cheese' in requested_toppings:
#     print("Adding extra cheese.")

# print('\nFinished making your pizza!')

# ao refazer o exercicio deu erro na area do print, refiz o ex
# requested_toppings = ["mushrooms", "green peppers" ,"extra cheese"]

# for requested_topping in requested_toppings:
#     print("Adding " + requested_topping + ".")
# print("\nFinished making your pizza!")

# requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
# for requested_topping in requested_toppings:
#  print(f"Adding {requested_topping}.")
# print("\nFinished making your pizza!")

# requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
# for requested_topping in requested_toppings:
#     if requested_topping == 'green peppers':
#         print("Sorry, we are out of green peppers right now.")
# else:
#  print(f"Adding {requested_topping}.")
# print("\nFinished making your pizza!")

# requested_toppings = []

# if requested_toppings:
#     for requested_topping in requested_toppings:
#         print(f"Adding {requested_topping}")
#     print("\nFinished making your pizza!")
# else:
#     print("Are you sure you want a plain pizza?")

available_toppings = ['mushrooms', 'olives', 'green peppers',
                      'pepperoni', 'pinapples', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry we don't have {requested_topping}.")
print("\nFinished making your pizza!")

staff = ['john', 'mark', 'scot', 'admin', 'jaden' ]
if 'admin' in staff:
    print(f"\nHello admin, would you like to see a status report?")
if not 'admin' == [staff]:
    print(f"\nHello {staff[0:4]}, thank you for logging in again.")
    
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
if numbers:
    for number in numbers:
        if number == '1':
            print(f"1st")
        elif number == '2':
            print('2nd')
        elif number == '3':
            print('3rd')
        else:
            print(f"{numbers}th")    
    
    