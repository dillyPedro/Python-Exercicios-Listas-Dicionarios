idades_por_setor = {
    'Setor A': [22, 26, 30, 30, 35, 38, 40, 56, 57, 65],
    'Setor B': [22, 24, 26, 33, 41, 49, 50, 54, 60, 64],
    'Setor C': [23, 26, 26, 29, 34, 35, 36, 41, 52, 56],
    'Setor D': [19, 20, 25, 27, 34, 39, 42, 44, 50, 65]
}

# Somando os valores dos setores:
novo_idades_por_setor = {}

for chaves, valores in idades_por_setor.items():
    novo_idades_por_setor[chaves] = sum(valores)

'''
Rascunho novo_idades_por_setor = {
        'Setor A': 399, 
        'Setor B': 423, 
        'Setor C': 358, 
        'Setor D': 365
        }
'''

media_por_setor = []

for valores in novo_idades_por_setor.values():
    media = valores / 10
    media_por_setor.append(media)

setores = []

for chaves in novo_idades_por_setor.keys():
    setores.append(chaves)

'''
Rascunho setores = ['Setor A', 'Setor B', 'Setor C', 'Setor D']
Rascunho média_por_setor = [39.9, 42.3, 35.8, 36.5]
'''

# Unindo as listas "setores" e "media_por_setor" em um dicionário:
dic_media_por_setores = {}

dic_media_por_setores = dict(zip(setores, media_por_setor))

'''
Rascunho dic_media_por_setores = {
                'Setor A': 39.9, 
                'Setor B': 42.3, 
                'Setor C': 35.8, 
                'Setor D': 36.5
                }
'''

soma = 0

for valores in novo_idades_por_setor.values():
    soma = soma + valores
    
media_geral = soma / (len(novo_idades_por_setor.keys()) * 10) 

# Criar uma lista com todos os valores presentes nos valores do dicionário "idades_por_setor":

'''
rascunho idades_por_setor = {
        'Setor A': [22, 26, 30, 30, 35, 38, 40, 56, 57, 65],
        'Setor B': [22, 24, 26, 33, 41, 49, 50, 54, 60, 64],
        'Setor C': [23, 26, 26, 29, 34, 35, 36, 41, 52, 56],
        'Setor D': [19, 20, 25, 27, 34, 39, 42, 44, 50, 65]
        }
'''

todas_as_idades = []

for valores in idades_por_setor.values():
    todas_as_idades.append(valores)

todas_as_idades_atualizado = []

for lista in todas_as_idades:
    todas_as_idades_atualizado.extend(lista)

contagem_idades = 0

for idades in todas_as_idades_atualizado:
    if(idades > media_geral):
        contagem_idades +=1
    else:
        continue

print(f'Média de idades por setor = {dic_media_por_setores}')
print(f'Média geral = {media_geral:.2f}')
print(f'Quantidade de idades maiores que a média geral = {contagem_idades}')
