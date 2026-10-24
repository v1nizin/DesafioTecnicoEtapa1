# Exercício 1: Conferência da separação 

pedido = [  
    { "sku": "SSD-1TB-KG",  "qtd": 2 },  
    { "sku": "MEM-16-DDR5", "qtd": 2 },  
    { "sku": "FNT-650W",    "qtd": 1 },  
    { "sku": "GAB-AIR-01",  "qtd": 1 }, 
] 

bipados = [  
    "SSD-1TB-KG", "MEM-16-DDR5", "SSD-1TB-KG", "FNT-650W",  
    "BRD-MOUSEPAD", "FNT-650W", "CBL-HDMI-2M", 
]

contagem = {}

for produto in bipados:
    if produto not in contagem: 
        contagem[produto] = 0 
    contagem[produto] += 1    
print (contagem)
        
for produto in pedido: 
    
    quantidade = produto["qtd"]
    cod_sku = produto["sku"]
    quantidade_bipada = contagem.get(cod_sku, 0)
    faltando = quantidade - quantidade_bipada
    sobrando = quantidade_bipada - quantidade
    
    
    if quantidade_bipada == quantidade:
        print (f"OK - {quantidade}x {cod_sku}")
    elif quantidade_bipada < quantidade:
        print (f"FALTANDO - {faltando}x {cod_sku}")
    else:
        print (f"SOBRANDO - {sobrando}x {cod_sku}")
        
skus_pedido = []

for produto in pedido:
    skus_pedido.append(produto["sku"])
    
for cod_sku in bipados:
    if cod_sku not in skus_pedido:
        print(f"NÃO PERTENCE AO PEDIDO - {cod_sku}")
        







