import pandas as pd
from tabulate import tabulate

# este é o dicionário que criamos para servir como o conteúdo do DataFrame
dados = {'Título:': ['A Volta Dos Que Não Foram', 'Senhor Dos Aneis', 'Os Cachos De Um Careca'],
         'Autor:': ['Falcão', 'J. R. R. Tolkien', 'O Careca'],
         'Editora:': ['SBS Editora', 'Martin Fontes', 'Carecas Editora'],
         'Número de Cópias:': [25, 300, 150],
         'Status:': ['Disponível', 'Emprestado', 'Disponível']}


# definindo explicitamente o DataFrame
df = pd.DataFrame(data=dados) # função do dataframe

# importando os dados do csv
dataframe = pd.read_csv('dados.csv')
print("csv")
print(tabulate(dataframe, headers='keys', tablefmt='rounded_grid'))

print("PRIMEIRO DATA FRAME:")
print(tabulate(df, headers='keys', tablefmt='rounded_grid'))

# INSERINDO NOVO DADO:

# esta é uma lista para inserir os novos dados. lembre de digitar as chaves do jeito que foram criadas no df
novo_dado = [{'Título:': 'Ladrão de Raios', 'Autor:': 'Rick Riordan',
              'Editora:': 'Intrínseca', 'Número de Cópias:': 50, 'Status:': 'Disponível'},
             {'Título:': 'A Droga do Amor', 'Autor:': 'Pedro Bandeira',
              'Editora:': '', 'Número de Cópias:': 200, 'Status:': 'Disponível'}]

# função para adicionar a lista ao df
df = df._append(novo_dado, ignore_index=True)

print('APÓS A INSERÇÃO:')
print(tabulate(df, headers='keys', tablefmt='rounded_grid'))

# inserindo uma coluna

df['Nova coluna'] = ''
print("INSERINDO COLUNA:")
print(tabulate(df, headers='keys', tablefmt='rounded_grid'))

# ATUALIZANDO UM DADO

df.loc[df['Título:'] == 'Senhor Dos Aneis', 'Título:'] = 'Senhor Dos Anéis'
df.loc[df['Título:'] == 'Senhor Dos Anéis', 'Status:'] = 'Disponível'
df.loc[df['Título:'] == 'A Droga do Amor', 'Status:'] = 'Emprestado'

print('APÓS A ATUALIZAÇÃO:')
print(tabulate(df, headers='keys', tablefmt='rounded_grid'))
#df.to_csv('dados.csv', index=False)

# REMOVER UM DADO.

df.drop(index=3, inplace=True)

print("APÓS A DELEÇÃO:")
print(tabulate(df, headers='keys', tablefmt='rounded_grid'))

# também podemos remover uma coluna especificando no argumento da função.

df.drop(columns='Nova coluna', inplace=True)

print('DELETANDO COLUNA:')
print(tabulate(df, headers='keys', tablefmt='rounded_grid'))


#relatórios de consultas
livros_disponiveis = df.loc[df['Status:'] == 'Disponível']
print("Livros disponiveis: ")
print(tabulate(livros_disponiveis, headers='keys', tablefmt='rounded_grid'))

livros_emprestados = df.loc[df['Status:'] == 'Emprestados']
print("Livros emprestados: ")
print(tabulate(livros_emprestados, headers='keys', tablefmt='rounded_grid'))

#transpor coluna x index
print(tabulate(df.columns, headers='keys', tablefmt='rounded_grid'))

#tamanho
tamanho = df.size
print(tamanho)
