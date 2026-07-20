# objetivo = 300
# gastos = 120
# reservas = 80

# print(f"\nObjetivo diário: R$ {objetivo}")
# print(f"Gastos diários: R$ {gastos}")
# print(f"Valor para reserva: R$ {reservas}")

# # Lógica do Objetivo
# if objetivo >= 280:
#     print("\nVocê bateu a meta!")
# else:
#     print("\nVocê não bateu a meta!")

# # Lógica dos Gastos (Corrigida)
# if gastos > 120:
#     print("\nVocê ultrapassou o limite de gastos diários!")
# elif gastos == 120:
#     print("\nVocê está exatamente no limite diário!")
# else:
#     print("\nVocê está abaixo do limite! Quanto menos gastar, mais lucro terá!")

# # Lógica das Reservas (Corrigida)
# if reservas >= 80:
#     print("\nReserva feita com sucesso! Continue assim.")
# else:
#     print("\nFalha no planejamento de reservas! Tente ajustar os custos.")

# 1. Coleta de dados (Entrada)
print("--- Calculadora de Lucro Diário ---\n")
objetivo = float(input("Qual o seu objetivo de ganho bruto hoje? R$ "))

# Coletando gastos específicos
combustivel = float(input("Quanto gastou com combustível? R$ "))
alimentacao = float(input("Quanto gastou com alimentação? R$ "))
reservas = float(input("Quanto deseja guardar de reserva? R$ "))

# 2. Processamento (O "Coração" contábil)
total_gastos = combustivel + alimentacao
lucro_liquido = objetivo - total_gastos - reservas

# 3. Saída (Feedback)
print(f"\n--- Resumo Financeiro ---")
print(f"Ganho Bruto: R$ {objetivo:.2f}")
print(f"Total de Custos (Combustível + Alimentação): R$ {total_gastos:.2f}")
print(f"Reserva: R$ {reservas:.2f}")
print(f"Saldo Líquido no bolso: R$ {lucro_liquido:.2f}")

# 4. Decisão baseada no saldo
if lucro_liquido > 0:
    print("\nÓtimo! Você teve lucro hoje.")
elif lucro_liquido == 0:
    print("\nVocê trabalhou para cobrir os custos e a reserva. Equilíbrio atingido.")
else:
    print("\nAtenção: Você teve prejuízo operacional hoje!")
    
     