import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Configurar semente para reprodutibilidade
np.random.seed(42)
random.seed(42)

# Definir parâmetros
n_vendas = 200

# Listas de dados fictícios
clientes = ['Ana Silva', 'Bruno Oliveira', 'Carla Santos', 'Daniel Costa', 'Elena Pereira',
           'Fernando Alves', 'Gabriela Lima', 'Henrique Souza', 'Isabela Rocha', 'João Mendes',
           'Karina Ferreira', 'Leonardo Martins', 'Mariana Barbosa', 'Nicolas Ramos', 'Olivia Castro',
           'Paulo Cardoso', 'Quintino Dias', 'Raquel Teixeira', 'Samuel Gomes', 'Tatiane Moreira']

produtos = {
    'Smartphone': {'preco_min': 1200, 'preco_max': 4500},
    'Notebook': {'preco_min': 2500, 'preco_max': 8000},
    'Tablet': {'preco_min': 800, 'preco_max': 2500},
    'Fone de Ouvido': {'preco_min': 80, 'preco_max': 800},
    'Monitor': {'preco_min': 600, 'preco_max': 2000},
    'Teclado': {'preco_min': 50, 'preco_max': 300},
    'Mouse': {'preco_min': 30, 'preco_max': 200},
    'Impressora': {'preco_min': 400, 'preco_max': 1500},
    'Câmera': {'preco_min': 900, 'preco_max': 3500},
    'Console de Games': {'preco_min': 2000, 'preco_max': 5000}
}

lojas = ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Porto Alegre', 'Curitiba',
         'Brasília', 'Salvador', 'Fortaleza', 'Recife', 'Manaus']

vendedores = ['Carlos Almeida', 'Mariana Costa', 'Roberto Santos', 'Fernanda Lima', 
              'Ricardo Oliveira', 'Juliana Pereira', 'Lucas Mendes', 'Patrícia Souza',
              'Marcos Silva', 'Amanda Rodrigues']

# Função para gerar data aleatória no último ano
def gerar_data_aleatoria():
    data_inicio = datetime(2023, 1, 1)
    data_fim = datetime(2023, 12, 31)
    diferenca = data_fim - data_inicio
    dias_aleatorios = random.randint(0, diferenca.days)
    return data_inicio + timedelta(days=dias_aleatorios)

# Criar lista de dados
dados = []

for i in range(1, n_vendas + 1):
    # Informações básicas da venda
    id_venda = i
    data_venda = gerar_data_aleatoria()
    
    # Cliente
    cliente = random.choice(clientes)
    idade_cliente = random.randint(18, 70)
    
    # Loja e vendedor
    loja = random.choice(lojas)
    vendedor = random.choice(vendedores)
    
    # Produto
    produto_nome = random.choice(list(produtos.keys()))
    produto_info = produtos[produto_nome]
    preco_unitario = round(random.uniform(produto_info['preco_min'], produto_info['preco_max']), 2)
    
    # Quantidade (mais chances de ser 1, mas pode ser até 5)
    quantidade_options = [1, 1, 1, 1, 1, 1, 2, 2, 3, 4, 5]  # Distribuição para favorecer 1
    quantidade = random.choice(quantidade_options)
    
    # Adicionar à lista
    dados.append({
        'id_venda': id_venda,
        'data': data_venda.strftime('%Y-%m-%d'),
        'cliente': cliente,
        'idade': idade_cliente,
        'vendedor': vendedor,
        'loja': loja,
        'produto': produto_nome,
        'quantidade': quantidade,
        'preco_unitario': preco_unitario
    })

# Criar DataFrame
df = pd.DataFrame(dados)

# Salvar como CSV
df.to_excel('vendas.xlsx', index=False)

print("✅ Dataset criado com sucesso!")
print(f"📊 Total de vendas: {len(df)}")
print(f"📅 Período: {df['data'].min()} a {df['data'].max()}")
print(f"🏪 Lojas: {df['loja'].nunique()}")
print(f"👥 Vendedores: {df['vendedor'].nunique()}")
print(f"🛍️ Produtos: {df['produto'].nunique()}")
print(f"👤 Clientes únicos: {df['cliente'].nunique()}")
print("\n📋 Amostra dos dados:")
print(df.head(10))
print("\n📈 Estatísticas descritivas:")
print(df[['quantidade', 'preco_unitario']].describe())

# Criar também um arquivo Excel para referência
with pd.ExcelWriter('dados_vendas.xlsx', engine='openpyxl') as writer:
    # Planilha principal
    df.to_excel(writer, sheet_name='Vendas', index=False)
    
    # Planilha de resumo
    resumo = {
        'Métrica': [
            'Total de Vendas',
            'Período Inicial',
            'Período Final',
            'Número de Lojas',
            'Número de Vendedores',
            'Número de Produtos',
            'Número de Clientes Únicos',
            'Quantidade Média por Venda',
            'Preço Unitário Médio',
            'Venda Mais Alta (preço unitário)',
            'Venda Mais Baixa (preço unitário)'
        ],
        'Valor': [
            len(df),
            df['data'].min(),
            df['data'].max(),
            df['loja'].nunique(),
            df['vendedor'].nunique(),
            df['produto'].nunique(),
            df['cliente'].nunique(),
            round(df['quantidade'].mean(), 2),
            round(df['preco_unitario'].mean(), 2),
            round(df['preco_unitario'].max(), 2),
            round(df['preco_unitario'].min(), 2)
        ]
    }
    
    resumo_df = pd.DataFrame(resumo)
    resumo_df.to_excel(writer, sheet_name='Resumo', index=False)
    
    # Planilha com lista de produtos
    produtos_info = []
    for produto, info in produtos.items():
        produtos_vendidos = df[df['produto'] == produto]
        produtos_info.append({
            'Produto': produto,
            'Preço Mínimo': info['preco_min'],
            'Preço Máximo': info['preco_max'],
            'Vendas Realizadas': len(produtos_vendidos),
            'Quantidade Total Vendida': produtos_vendidos['quantidade'].sum(),
            'Faturamento Total': (produtos_vendidos['quantidade'] * produtos_vendidos['preco_unitario']).sum()
        })
    
    produtos_df = pd.DataFrame(produtos_info)
    produtos_df.to_excel(writer, sheet_name='Produtos', index=False)

print(f"\n💾 Arquivos salvos:")
print(f"  1. vendas.csv - Dataset principal para análise")
print(f"  2. dados_vendas.xlsx - Arquivo com múltiplas planilhas para referência")