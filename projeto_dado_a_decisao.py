import json
import re
import time

# ==========================================
# 1. SIMULAÇÃO DOS DADOS BRUTOS DOS SISTEMAS
# ==========================================

# Dados bagunçados que o comercial cadastrou no HubSpot CRM
vendas_hubspot = [
    {
        "id_negocio": "901",
        "empresa": "Tech Solucoes LTDA",
        "cnpj": "12.345.678/0001-99",  # Formatado com pontos/traço
        "valor": 4500.00,
        "vendedor": "Henrique Mariano"
    },
    {
        "id_negocio": "902",
        "empresa": "Fábrica de Software S/A",
        "cnpj": "98.765.432/0001-00",
        "valor": 8200.00,
        "vendedor": "Henrique Mariano"
    },
    {
        "id_negocio": "903",
        "empresa": "Pizzaria do Bairro",
        "cnpj": "11.222.333/0001-44",
        "valor": 1300.00,
        "vendedor": "Amanda Silva"
    }
]

# Dados financeiros que estão dentro do Omie ERP
financeiro_omie = [
    {"cnpj_cliente": "12345678000199", "status_nota": "Emitida", "pago": "Sim"},
    {"cnpj_cliente": "98765432000100", "status_nota": "Emitida", "pago": "Não"},
    {"cnpj_cliente": "11222333000144", "status_nota": "Pendente", "pago": "Não"}
]


# ==========================================
# 2. AS FUNÇÕES DE INTEGRAÇÃO (O SEU TRABALHO)
# ==========================================

def limpar_cnpj(cnpj_sujo):
    """Remove pontos, barras e traços do CNPJ para o padrão Omie."""
    return re.sub(r'\D', '', cnpj_sujo)


def processar_integracao(crm_dados, erp_dados):
    print("🤖 Iniciando motor de integração Python...")
    time.sleep(1) # Simula o tempo de processamento
    
    visao_unica_clientes = []
    faturamento_total = 0.0
    
    # Loop: Passa de cliente em cliente que veio do HubSpot
    for venda in crm_dados:
        # 1. Automação e Limpeza: Tratando o CNPJ
        cnpj_limpo = limpar_cnpj(venda["cnpj"])
        
        # 2. Inteligência Operacional: Cruzando com os dados do Omie
        status_nota = "Não Encontrado no ERP"
        foi_pago = "Desconhecido"
        
        for lancamento in erp_dados:
            if lancamento["cnpj_cliente"] == cnpj_limpo:
                status_nota = lancamento["status_nota"]
                foi_pago = lancamento["pago"]
                break
        
        # 3. Visão Única: Juntando tudo em um formato limpo
        cliente_consolidado = {
            "ID Venda": venda["id_negocio"],
            "Cliente": venda["empresa"],
            "CNPJ Tratado": cnpj_limpo,
            "Valor Contrato": f"R$ {venda['valor']:.2f}",
            "Vendedor": venda["vendedor"],
            "Status NF (Omie)": status_nota,
            "Pago?": foi_pago
        }
        
        # Adiciona na nossa lista final
        visao_unica_clientes.append(cliente_consolidado)
        
        # Somando para o Dashboard Executivo
        faturamento_total += venda["valor"]
        
    return visao_unica_clientes, faturamento_total


# ==========================================
# 3. EXECUTANDO E MOSTRANDO O RESULTADO
# ==========================================

# Executa a função principal passando os dados falsos
clientes_integrados, total_receita = processar_integracao(vendas_hubspot, financeiro_omie)

print("\n" + "="*50)
print("📈 DASHBOARD EXECUTIVO (Previsibilidade de Receita)")
print("="*50)
print(f"Faturamento Total Mapeado: R$ {total_receita:.2f}")
print(f"Total de Contratos Conectados: {len(clientes_integrados)}")

print("\n" + "="*50)
print("👥 VISÃO ÚNICA DO CLIENTE (Dados Conectados Ponta a Ponta)")
print("="*50)
# Usa o json.dumps apenas para deixar o dicionário bonito na tela (com recuos)
print(json.dumps(clientes_integrados, indent=3, ensure_ascii=False))

print("\n✅ Processo concluído com sucesso!")