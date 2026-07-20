# ==============================================================================
# PROJETO: Missão Sydney / PROJECT: Mission Sydney
# OBJETIVO: Monitorar rotas para a Austrália / GOAL: Monitor routes to Australia
# ==============================================================================

# Dicionário estruturado em inglês (Padrão de mercado)
flight_routes = [
    {"airline": "Latam", "layover": "Santiago (SCL)", "price_brl": 9500},
    {"airline": "United", "layover": "Houston (IAH)", "price_brl": 8900}
]

max_budget = 9000

# ------------------------------------------------------------------------------
# VERSÃO EM PORTUGUÊS (Exibição para o usuário)
# ------------------------------------------------------------------------------
print("--- Varrendo rotas viáveis para Sydney ---")
for route in flight_routes:
    if route["price_brl"] <= max_budget:
        print(f"Alerta! Rota via {route['layover']} está dentro do orçamento: R${route['price_brl']}")

print("\n" + "="*40 + "\n")

# ------------------------------------------------------------------------------
# ENGLISH VERSION (User display)
# ------------------------------------------------------------------------------
print("--- Scanning viable routes to Sydney ---")
for route in flight_routes:
    if route["price_brl"] <= max_budget:
        print(f"Alert! Route via {route['layover']} is within budget: BRL {route['price_brl']}")