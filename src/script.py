#!/usr/bin/python3

# O script pide algúns datos por teclado
nome = input('Dame o teu nome: ')
apelido1 = input('Dame o teu primeiro apelido: ')
nif = input('Dame o teu NIF (formato: 11111111A)')
#print(nome, apelido1, nif)

# Crea un DataFrame cos datos introducidos
import pandas as pd

df = pd.DataFrame({'nome':[nome], 'apelido':[apelido1], 'nif':[nif]})
#print(df)

# Escribe os datos do DataFrame a un par de ficheiros
df.to_json('ti.json')
print('Ficheiro JSON escrito a disco.')
df.to_parquet('ti.parquet')
print('Ficheiro PARQUET escrito a disco.')

# Aparece unha vaca parlante
import cowsay
texto = 'Ola '+nome+'. Sorte co exame!'
cowsay.cow(texto)