# Exercício 2: Resumo de devoluções (RMA)

devolucoes = [
    {"pedido": 1001, "motivo": "Defeito",                   "valor": 899.90},
    {"pedido": 1002, "motivo": "Arrependimento",            "valor": 129.90},
    {"pedido": 1003, "motivo": "Defeito",                   "valor": 2499.00},
    {"pedido": 1004, "motivo": "Avaria no transporte",      "valor": 349.90},
    {"pedido": 1005, "motivo": "Arrependimento",            "valor": 59.90},
    {"pedido": 1006, "motivo": "Defeito",                   "valor": 189.90},
    {"pedido": 1007, "motivo": "Avaria no transporte",      "valor": 1299.00},
]

# Armazena o valor total das devoluções agrupado por motivo
totais = {}

for devolucao in devolucoes:
    motivo = devolucao["motivo"]
    valor = devolucao["valor"]
    
    if motivo not in totais:
        totais[motivo] = 0

    totais[motivo] += valor

print(totais)

maior_num = max(totais.values())

# Identifica qual motivo possui esse maior valor
for motivo, valor in totais.items():
    if valor == maior_num:
        maior = motivo

print(f"Motivo com maior valor: {maior} - R$ {maior_num:.2f}")

acima_500 = 0

for devolucao in devolucoes:
    valor = devolucao["valor"]

    if valor > 500:
        acima_500 += 1

print(f"Devoluções acima de R$500,00: {acima_500}")
