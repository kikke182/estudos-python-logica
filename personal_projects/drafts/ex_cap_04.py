#ex_cap_04.py 
#magicians.py

# magicians = ['alice', 'david', 'carolina']
# for magician in magicians:
#     print(magician)

# import time

# # 1. Criamos uma lista base e multiplicamos ela para chegar a 1.000.000 de itens
# # (3 nomes repetidos até dar um milhão)
# lista_base = ['alice', 'david', 'carolina']
# magicians = lista_base * 333334  # Isso gera uma lista com 1.000.002 nomes!

# print(f"Tamanho da lista criada: {len(magicians):,} itens.\n")
# print("Iniciando o laço for... Aguarde um momento.\n")

# # 2. Marcamos o tempo de início
# tempo_inicio = time.time()

# # 3. O laço FOR passando por 1 milhão de nomes
# for magician in magicians:
#     # ATENÇÃO: Não usamos o print(magician) aqui dentro porque o que demora 
#     # não é o Python processar, é o VS Code desenhar 1 milhão de linhas na tela!
#     # Em vez disso, apenas fazemos uma operação leve com o nome.
#     nome_maiusculo = magician.upper()

# # 4. Marcamos o tempo de término
# tempo_fim = time.time()

# # 5. Calculamos a diferença
# tempo_total = tempo_fim - tempo_inicio

# print("--- RESULTADO ---")
# print(f"O Python terminou de processar 1 milhão de nomes!")
# print(f"Tempo gasto: {tempo_total:.4f} segundos.")

# magicians = ['alice', 'david', 'carolina']
# for magician in magicians:
#     print(f"{magician.title()}, that was a great trick!")

# magicians = ['alice', 'david', 'carolina']
# for magician in magicians:
#     print(f"{magician.title()}, that was a great trick!")
#     print(f"I can't wait to see your next trick, {magician.title()}.\n")

# magicians = ['alice', 'david', 'carolina']
# for magician in magicians:
#     print(f"{magician.title()}, that was a great trick!")
#     print(f"I can't wait to see your next trick, {magician.title()}.\n")
    
#     print(f"Thank you, everyone. That was a great magic show!")

# for value in range(1,5):
#     print(value)

# for value in range(1,6):
#     print(value)

# numbers = list(range(1,6))
# print(numbers)

# even_number = list(range(2,11,2))
# print(even_number)

# squares = []
# for value in range(1,11):
#     square = value ** 2
#     squares.append(square)
# print(squares)

# squares = []
# for value in range(1,11):
#     squares.append(value ** 2)
# print(squares)

# digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

# print(min(digits))  # Vai exibir: 0
# print(max(digits))  # Vai exibir: 9
# print(sum(digits))  # Vai exibir: 45

# squares = [value ** 2 for value in range(1,11)]
# print(squares)

# # 4.3 Counting to Twenty

# numbers = [value*1 for value in range(1,21)]
# print(numbers)

# # # 4.4 One Million
# # numbers = [value for value in range(1,1000000)]
# # print(numbers)

# # 4.5 Summing a Million: 
# numbers = (1,1000000)
# print(min(numbers))
# print(max(numbers))
# print(sum(numbers))

# # 4.6 Odd Numbers
# odd_number = [value*3 for value in range(1, 20, 1)]
# print(odd_number)

# #4.7 Threes
# number_three = [value*3 for value in range(3, 30, 3)]
# print(number_three)

# #4.8 Cubes
# cubes = [value**1 for value in range(1,10)]
# cubes = [value**2 for value in range(1,10)]
# cubes = [value**3 for value in range(1,10)]
# cubes = [value**4 for value in range(1,10)]
# cubes = [value**5 for value in range(1,10)]
# cubes = [value**6 for value in range(1,10)]
# cubes = [value**7 for value in range(1,10)]
# cubes = [value**8 for value in range(1,10)]
# cubes = [value**9 for value in range(1,10)]
# cubes = [value**10 for value in range(1,10)]
# print(cubes)

# players = ['charles', 'martina', 'michael', 'florence', 'eli']
# print(players[0:3])

# players = ['charles', 'martina', 'michael', 'florence', 'eli']
# print(players[1:4])

# players = ['charles', 'martina', 'michael', 'florence', 'eli']
# print(players[2:])

# players = ['charles', 'martina', 'michael', 'florence', 'eli']
# print(players[-3:])

# players = ['charles', 'martina', 'michael', 'florence', 'eli']
# print(f"Here are the first three players on my team:")
# for player in players[:3]:
#     print(player.title())

# my_foods = ['pizza', 'falafel', 'carrot cake']
# friend_foods = my_foods[:]

# print('My favorite foods are:')
# print(my_foods)

# print(f"\nMy friend's favorite foods are:")
# print(friend_foods)

# my_foods = ['pizza', 'falafel', 'carrot cake']
# friend_foods = my_foods[:]

# my_foods.append('cannoli')
# friend_foods.append('ice cream')

# print('My favorite foods are:')
# print(my_foods)

# print(f"\nMy friend's favorite foods are:")
# print(friend_foods)

# my_foods = ['pizza', 'falafel', 'carrot cake']
# #friend_foods = my_foods[:]
# friend_foods = my_foods

# my_foods.append('cannoli')
# friend_foods.append('ice cream')

# print('My favorite foods are:')
# print(my_foods)

# print(f"\nMy friend's favorite foods are:")
# print(friend_foods)

# # 4.10 Slices
# places = ['rio', 'london', 'ny', 'melbourne', 'amsterdan']
# print(f"Here are the first three places on my list:")
# for place in places[0:1:2]:
#     print(places[:3])
# print(f"Here are the middle three places on my list:")
# for place in places[0:1:2]:
#     print(places[1:4])
# print(f"Here are the last three places on my list:")
# for place in places[0:1:2]:
#     print(places[2:5])

# # 4.11 My Pizzas, Your Pizzas
# pizzas = ['cheese','bacon', 'chicken']
# pizzas.append('chocolate')
# for pizza in pizzas[0:5:2]: 
#     print(pizzas)
#     print(f"My favorite pizza is {pizzas[1]}!")
# friend_pizzas = pizzas[:]
# print(friend_pizzas)
# friend_pizzas.append('pinaple')

# 4.12 More Loops

# foods = ['hamburguer', 'hot dog', 'taco', 'ice cream', 'fries']
# friend_foods = foods[:]

# print("My favorite foods are:")
# for food in foods:
#     print(f"- {food.title()}")

# print("\nMy friend's favorite foods are: ")
# for food in foods:
#     print(f"-{food.title()}")    

# dimensions = (200, 50)
# print(dimensions[0])
# print(dimensions[1])

# dimensions = (200, 50) # gera erro pq nao se muda uma tupla
# print(dimensions[0]) = 250


# dimensions = (200, 50)
# for dimension in dimensions:
#     print(dimension)

dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)
    
dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)
    
buffets = ['sushi', 'bbq', 'pasta', 'hamburguer', 'fruit']
for buffet in buffets:
    print(f"-{buffet.title()}")
    

buffets = ('sushi', 'bbq', 'pasta', 'hamburguer', 'fruit')
for buffet in buffets:
    print(f"-{buffet.title()}")

buffets = ('sushi', 'bbq', 'pasta', 'hamburguer', 'fruit')
buffets = 'fries' 

buffets = ('chicken', 'tacos')
print('\nModified buffet:')
for buffet in buffets:
    print(buffets)
    