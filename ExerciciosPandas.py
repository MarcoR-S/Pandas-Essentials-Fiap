import pandas as pd 
import numpy as np
def ex1():
    df_alunos = pd.DataFrame({
        "alunoID": [1,2,3],
        "nomes": ["Ana", "Beto", "Caio"]
    }).set_index("alunoID")
    df_cursos = pd.DataFrame({
        "alunoID": [1,2,3],
        "cursos": ["Python", "Pandas","Python"]
    }).set_index("alunoID")

    df_junto = df_alunos.join(df_cursos, how="outer")
    print(df_junto)

def ex2():
    df_produtos = pd.DataFrame({
    'ProdutoID': [1, 2, 3, 4, 5],
    'Nome': ['Teclado', 'Mouse', 'Monitor', 'Headset', 'Webcam'],
    'Preco': [150.00, 80.00, 900.00, 250.00, 300.00]
})
    df_vendas = pd.DataFrame({
    'VendaID': [1001, 1002, 1003, 1004],
    'ProdutoID': [1, 2, 2, 4],
    'Quantidade': [2, 1, 3, 1]
})
    df_junto = pd.merge(df_produtos, df_vendas, on="ProdutoID", how="inner")
    df_junto["Total"] = df_junto['Preco'] * df_junto['Quantidade']
    print(df_junto)

def ex3():
    data = {
    'Funcionario': ['Ana', 'Beto', 'Caio', 'Duda', 'Enzo'],
    'Salario': [5000, None, 4500, None, 7000],
    'Departamento': ['TI', 'TI', 'RH', 'Vendas', 'RH']
    }
    df_rh = pd.DataFrame(data)
    df_limpo = df_rh.dropna()
    df_rh = df_rh.fillna(df_rh['Salario'].mean())
    print(df_limpo)
    print(df_rh)


def ex4():
    notas_data = {
    'Nota': [8.5, 9.0, 6.5, 10.0, 7.0]
    }
    df_notas = pd.DataFrame(notas_data, index=['a', 'b', 'c', 'd', 'e'])
    df_c = df_notas.loc['c']
    print(df_c)
    df_4 = df_notas.iloc[3]
    print(df_4)
    df_bd = df_notas.loc['b':'d':1]
    print(df_bd)

def ex5():
    data_carros = {
    'Marca': ['Toyota', 'Honda', 'Toyota', 'Ford', 'Honda', 'Toyota', 'Ford'],
    'Modelo': ['Corolla', 'Civic', 'Hilux', 'Ka', 'Fit', 'Yaris', 'Ranger'],
    'Ano': [2022, 2019, 2021, 2018, 2023, 2020, 2022],
    'Preco': [120000, 90000, 250000, 45000, 85000, 95000, 180000]
    }
    df_carros = pd.DataFrame(data_carros)
    df_toyota = df_carros[df_carros['Marca']== 'Toyota']
    df_toyota_novos = df_carros[(df_carros['Marca']=='Toyota') & (df_carros['Ano'] > 2020)]
    print(df_toyota)
    print(df_toyota_novos)

    df_ford_ou_barato = df_carros[(df_carros['Marca'] == 'Ford') | (df_carros['Preco'] < 50000)]
    print(df_ford_ou_barato)
    
def ex6():
    estoque_data = {
        'Categoria': ['Eletrônicos', 'Móveis', 'Eletrônicos', 'Móveis', 'Acessórios'],
        'Produto': ['Celular', 'Cadeira', 'Laptop', 'Mesa', 'Capa'],
        'Quantidade': [50, 20, 15, 10, 100],
        'Preco': [2000, 350, 5000, 800, 50]
    }
    df_estoque = pd.DataFrame(estoque_data)
    df_alfab = df_estoque.sort_values(by='Categoria', ascending=True)
    print(df_alfab)
    df_alfab_quant = df_estoque.sort_values(by=['Categoria','Quantidade'], ascending=[True,False])
    print()
    print(df_alfab_quant)

def ex7():
    datas = pd.date_range(start='2024-01-01', periods=30)
    precos = np.random.randint(100, 200, size=30)
    df_precos = pd.DataFrame({"Preco": precos}, index = datas)
    df_precos['Media Movel'] = df_precos['Preco'].rolling(window = 7).mean()
    print(df_precos)

def ex8():
    estoque_data = {
        'Categoria': ['Eletrônicos', 'Móveis', 'Eletrônicos', 'Móveis', 'Acessórios'],
        'Produto': ['Celular', 'Cadeira', 'Laptop', 'Mesa', 'Capa'],
        'Quantidade': [50, 20, 15, 10, 100],
        'Preco': [2000, 350, 5000, 800, 50]
    }
    df_estoque = pd.DataFrame(estoque_data)
    df_estoque["Total"] = df_estoque['Preco'] * df_estoque['Quantidade']
    df_resumo = df_estoque.groupby('Categoria')['Total'].sum().reset_index()
    print(df_resumo)

if __name__ == "__main__":
    ex1() #altere para o desejado