numero_bacterias_por_dia = [1.2, 2.1, 3.3, 5.0, 7.8, 11.3, 16.6, 25.1, 37.8, 56.9]

lista_cresc = []

# Adicionando um índice para percorrer a lista "numero_bacterias_por_dia":
for contagem in range(1, len(numero_bacterias_por_dia)):
    amostra_atual = numero_bacterias_por_dia[contagem]
    amostra_passada = numero_bacterias_por_dia[contagem - 1]
    if(amostra_passada != 0): # Evitando ter uma divisão por zero;
        cresc = 100 * (amostra_atual - amostra_passada) / (amostra_passada)
        lista_cresc.append(cresc)
    else:
        lista_cresc.append(None)

print(f'Lista Atualizada = {lista_cresc}')
