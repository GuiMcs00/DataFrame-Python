import pandas as pd
from tabulate import tabulate

# Considerações para o deploy:
print("Considerações para o deploy:")
print("1. Ferramentas utilizadas para o Projeto:")
print("   - IDE: PyCharm")
print("   - Bibliotecas: Pandas e Tabulate")
print("2. Linguagem de programação: Python")

integrantes = {'Nome:': ['Guilherme de Oliveira Amaral', 'Beatriz Silva dos Santos', 'Danilo Barbosa Lopes',
                         'Filipe Maia de Paula', 'João Victor Guimarães Caldas'],
               'RGM:': ['31891942', '30034493', '31775233', '32052341', '31369049']}
print('\nINTEGRANTES:')
print(tabulate(integrantes, headers='keys', tablefmt='double_grid'))

dataframe = pd.read_csv('dados.csv')

#para ordenar pelo título
dataframe = dataframe.sort_values(by='Título:')
# para reorganizar o índex.
dataframe.index = range(1, len(dataframe) + 1)

print('\nDATAFRAME:')
print(tabulate(dataframe, headers='keys', tablefmt='rounded_grid'))

dataframe.loc[dataframe['Título:'] == 'Under the Dome', 'Título:'] = 'Guilherme Amaral'
print(tabulate(dataframe, headers='keys', tablefmt='rounded_grid'))
dataframe.index = range(1, len(dataframe) + 1)

livros_disponiveis = dataframe.loc[dataframe['Status:'] == 'Disponível']
livros_emprestados = dataframe.loc[dataframe['Status:'] == 'Emprestado']
