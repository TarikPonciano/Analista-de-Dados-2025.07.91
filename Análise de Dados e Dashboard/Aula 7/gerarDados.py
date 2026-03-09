import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# Reprodutibilidade
np.random.seed(42)

# Parâmetros da base
num_registros = 5000

datas = pd.date_range(start='2024-01-01', end='2024-12-31', freq='D')

lojas = ['Loja Centro', 'Loja Norte', 'Loja Sul', 'Loja Leste', 'Loja Oeste', 'Loja Premium']

produtos = ['Camiseta Básica', 'Camiseta Premium', 'Calça Jeans', 'Calça Social',
            'Tênis Esportivo', 'Tênis Casual', 'Boné', 'Chapéu', 'Jaqueta de Couro',
            'Jaqueta Esportiva', 'Vestido', 'Suéter', 'Shorts', 'Meias', 'Óculos de Sol']
categorias = {
    'Camiseta Básica': 'Vestuário Básico',
    'Camiseta Premium': 'Vestuário Premium',
    'Calça Jeans': 'Vestuário Casual',
    'Calça Social': 'Vestuário Formal',
    'Tênis Esportivo': 'Calçados Esportivos',
    'Tênis Casual': 'Calçados Casual',
    'Boné': 'Acessórios',
    'Chapéu': 'Acessórios Premium',
    'Jaqueta de Couro': 'Vestuário Premium',
    'Jaqueta Esportiva': 'Vestuário Esportivo',
    'Vestido': 'Vestuário Feminino',
    'Suéter': 'Vestuário Inverno',
    'Shorts': 'Vestuário Verão',
    'Meias': 'Acessórios',
    'Óculos de Sol': 'Acessórios Premium'
}

# CORRIGIDO: Probabilidades que somam 1
prob_produtos = [0.10, 0.04, 0.08, 0.05, 0.07, 0.07, 0.06, 0.03, 0.04, 0.06, 0.07, 0.06, 0.08, 0.08, 0.07]
print(f"Soma das probabilidades dos produtos: {sum(prob_produtos)}")

# CORRIGIDO: Probabilidades que somam 1
prob_lojas = [0.20, 0.15, 0.15, 0.15, 0.15, 0.20]
print(f"Soma das probabilidades das lojas: {sum(prob_lojas)}")

# Geração dos dados com padrões temporais
data = {
    'data': np.random.choice(datas, num_registros),
    'loja': np.random.choice(lojas, num_registros),
    'produto': np.random.choice(produtos, num_registros),
}

df = pd.DataFrame(data)

# Adicionar categoria apenas
df['categoria'] = df['produto'].map(categorias)

# Padrões sazonais específicos
def gerar_padrao_sazonal(data):
    mes = data.month
    dia_semana = data.dayofweek
    
    # Padrões mensais
    if mes in [12, 1]:  # Natal e Ano Novo
        multiplicador = np.random.uniform(1.3, 2.0)
    elif mes in [6, 7]:  # Férias de inverno
        multiplicador = np.random.uniform(1.2, 1.5)
    elif mes in [11]:  # Black Friday
        multiplicador = np.random.uniform(1.4, 2.2)
    elif mes in [4, 5]:  # Dia das mães
        multiplicador = np.random.uniform(1.1, 1.4)
    else:
        multiplicador = np.random.uniform(0.8, 1.2)
    
    # Padrões semanais
    if dia_semana == 5:  # Sábado
        multiplicador *= np.random.uniform(1.2, 1.8)
    elif dia_semana == 4:  # Sexta-feira
        multiplicador *= np.random.uniform(1.1, 1.4)
    elif dia_semana == 0:  # Segunda-feira
        multiplicador *= np.random.uniform(0.7, 0.9)
    
    return multiplicador

# Gerar quantidades com padrões complexos
quantidades = []
for idx, row in df.iterrows():
    produto = row['produto']
    data_venda = row['data']
    
    multiplicador = gerar_padrao_sazonal(data_venda)
    
    # Base por tipo de produto
    if 'Premium' in produto:
        base = np.random.poisson(lam=1.2)
        if np.random.random() < 0.02:  # 2% chance de outlier alto
            base = np.random.randint(5, 15)
    elif 'Básic' in produto or 'Meias' in produto:
        base = np.random.negative_binomial(6, 0.4) + 2
    elif 'Calça' in produto or 'Tênis' in produto:
        base = int(np.clip(np.random.normal(2.5, 1.5), 1, 8))
    else:
        base = np.random.randint(1, 4)
    
    qtd = int(max(1, base * multiplicador))
    quantidades.append(qtd)

df['quantidade'] = quantidades

# Gerar preços com variações
precos = []
for idx, row in df.iterrows():
    # Preços base realistas
    base_price = {
        'Camiseta Básica': 49.90,
        'Camiseta Premium': 129.90,
        'Calça Jeans': 189.90,
        'Calça Social': 279.90,
        'Tênis Esportivo': 349.90,
        'Tênis Casual': 229.90,
        'Boné': 69.90,
        'Chapéu': 179.90,
        'Jaqueta de Couro': 799.90,
        'Jaqueta Esportiva': 299.90,
        'Vestido': 239.90,
        'Suéter': 159.90,
        'Shorts': 119.90,
        'Meias': 14.90,
        'Óculos de Sol': 249.90
    }
    
    preco = base_price[row['produto']]
    
    # Variação por loja
    if row['loja'] == 'Loja Premium':
        preco *= np.random.uniform(1.15, 1.35)
    elif row['loja'] == 'Loja Centro':
        preco *= np.random.uniform(1.05, 1.15)
    elif 'Norte' in row['loja'] or 'Sul' in row['loja']:
        preco *= np.random.uniform(0.9, 1.05)
    
    # Promoções sazonais
    mes = row['data'].month
    if row['categoria'] == 'Vestuário Inverno' and mes in [9, 10, 11]:
        preco *= np.random.uniform(1.1, 1.25)
    elif row['categoria'] == 'Vestuário Verão' and mes in [1, 2, 3]:
        preco *= np.random.uniform(1.1, 1.25)
    elif mes == 11 and np.random.random() < 0.3:  # Black Friday
        preco *= np.random.uniform(0.5, 0.7)
    
    # Promoções aleatórias
    if np.random.random() < 0.15:  # 15% dos produtos em promoção
        if np.random.random() < 0.3:  # 30% das promoções são grandes
            preco *= np.random.uniform(0.4, 0.7)
        else:
            preco *= np.random.uniform(0.75, 0.95)
    
    # Variação final
    preco *= np.random.uniform(0.97, 1.03)
    precos.append(round(preco, 2))

df['preco_unitario'] = precos

# Calcular valor total
df['valor_total'] = df['quantidade'] * df['preco_unitario']

# Adicionar outliers extremos controlados
num_outliers = int(num_registros * 0.004)
if num_outliers > 0:
    outlier_indices = np.random.choice(df.index, size=num_outliers, replace=False)
    for idx in outlier_indices:
        # Outliers podem ser positivos (vendas grandes) ou negativos (devoluções grandes)
        tipo = np.random.choice(['grande_venda', 'grande_devolucao'], p=[0.7, 0.3])
        
        if tipo == 'grande_venda':
            df.at[idx, 'quantidade'] = np.random.randint(50, 500)
            df.at[idx, 'preco_unitario'] = np.random.uniform(300, 2000)
        else:
            df.at[idx, 'quantidade'] = -np.random.randint(10, 100)
            df.at[idx, 'preco_unitario'] = np.random.uniform(100, 500)
        
        df.at[idx, 'valor_total'] = df.at[idx, 'quantidade'] * df.at[idx, 'preco_unitario']

# Adicionar padrões específicos por loja
padrao_loja = {
    'Loja Centro': {'multiplicador': 1.3, 'freq_promo': 0.2},
    'Loja Norte': {'multiplicador': 0.9, 'freq_promo': 0.25},
    'Loja Sul': {'multiplicador': 0.95, 'freq_promo': 0.22},
    'Loja Leste': {'multiplicador': 0.85, 'freq_promo': 0.3},
    'Loja Oeste': {'multiplicador': 0.88, 'freq_promo': 0.28},
    'Loja Premium': {'multiplicador': 1.4, 'freq_promo': 0.1}
}

# Aplicar padrões por loja
for idx, row in df.iterrows():
    if np.random.random() < padrao_loja[row['loja']]['freq_promo']:
        df.at[idx, 'valor_total'] *= np.random.uniform(0.7, 0.9)

# Organizar a base
df = df.sort_values('data').reset_index(drop=True)

# Adicionar ID único
df['id_venda'] = range(1000, 1000 + len(df))

# Reordenar colunas (apenas dados brutos para os alunos processarem)
df = df[['id_venda', 'data', 'loja', 'produto', 'categoria', 
         'quantidade', 'preco_unitario', 'valor_total']]

# Função para análise exploratória básica
def analise_exploratoria(df):
    print("="*80)
    print("DADOS DE VENDAS - BASE PARA ANÁLISE TEMPORAL")
    print("="*80)
    
    print("\n1. PRIMEIRAS 10 LINHAS:")
    print("-"*40)
    print(df.head(10).to_string())
    
    print("\n\n2. INFORMAÇÕES GERAIS:")
    print("-"*40)
    print(f"Período: {df['data'].min().date()} a {df['data'].max().date()}")
    print(f"Total de registros: {len(df):,}")
    print(f"Total de lojas: {df['loja'].nunique()}")
    print(f"Total de produtos: {df['produto'].nunique()}")
    print(f"Valor total: R$ {df['valor_total'].sum():,.2f}")
    
    print("\n\n3. ESTATÍSTICAS BÁSICAS:")
    print("-"*40)
    stats_df = df[['quantidade', 'preco_unitario', 'valor_total']].describe()
    print(stats_df.to_string())
    
    # Verificar distribuição
    print("\n\n4. DISTRIBUIÇÃO DOS DADOS:")
    print("-"*40)
    print("Distribuição por loja:")
    dist_loja = df['loja'].value_counts(normalize=True) * 100
    for loja, perc in dist_loja.items():
        print(f"  {loja:15s}: {perc:5.1f}%")
    
    print("\nDistribuição por produto:")
    dist_produto = df['produto'].value_counts(normalize=True).head(10) * 100
    for produto, perc in dist_produto.items():
        print(f"  {produto:20s}: {perc:5.1f}%")

# Executar análise exploratória
analise_exploratoria(df)

# Verificação adicional
print("\n" + "="*80)
print("VERIFICAÇÃO DAS PROBABILIDADES:")
print("="*80)
print("1. Distribuição real das lojas (deveria seguir as probabilidades):")
for loja in lojas:
    count = (df['loja'] == loja).sum()
    perc = count / len(df) * 100
    print(f"  {loja:15s}: {count:4d} registros ({perc:5.1f}%)")

print("\n2. Distribuição real dos produtos:")
for produto, prob_esperada in zip(produtos, prob_produtos):
    count = (df['produto'] == produto).sum()
    perc = count / len(df) * 100
    print(f"  {produto:20s}: {count:4d} registros ({perc:5.1f}% - esperado: {prob_esperada*100:4.1f}%)")

# Salvar dados
df.to_excel("dados_vendas_brutos_corrigidos.xlsx", index=False)
df.to_csv("dados_vendas_brutos_corrigidos.csv", index=False)

print("\n" + "="*80)
print("ARQUIVOS SALVOS COM SUCESSO!")
print("="*80)
print("1. dados_vendas_brutos_corrigidos.xlsx")
print("2. dados_vendas_brutos_corrigidos.csv")

print("\n" + "="*80)
print("SUGESTÕES DE ATIVIDADES PARA OS ALUNOS:")
print("="*80)
print("1. CRIAR COLUNAS TEMPORAIS da coluna 'data':")
print("   - Extrair: ano, mês, dia, trimestre, semana do ano")
print("   - Identificar: dia da semana, fim de semana, feriados")
print("   - Criar: período do dia (manhã/tarde/noite) se quiserem simular")
print("\n2. ANÁLISES TEMPORAIS com base no valor_total:")
print("   - Faturamento diário, semanal, mensal, trimestral")
print("   - Comparativo entre períodos")
print("   - Identificação de sazonalidade e tendências")
print("\n3. OUTRAS ANÁLISES:")
print("   - Ranking de produtos/lojas")
print("   - Ticket médio por período")
print("   - Identificação de outliers/anomalias")

# Gráfico de vendas diárias para referência do professor
plt.figure(figsize=(15, 5))
vendas_diarias = df.groupby('data')['valor_total'].sum()
plt.plot(vendas_diarias.index, vendas_diarias.values, linewidth=0.5, color='blue', alpha=0.7)
plt.title('Vendas Diárias - 2024 (Padrões Sazonais Embutidos)', fontsize=14, fontweight='bold')
plt.xlabel('Data')
plt.ylabel('Valor Total (R$)')
plt.grid(True, alpha=0.3)

# Destacar alguns padrões
# Natal/Ano Novo
plt.axvspan(pd.Timestamp('2024-12-15'), pd.Timestamp('2024-12-31'), alpha=0.2, color='red', label='Natal/Ano Novo')
plt.axvspan(pd.Timestamp('2024-01-01'), pd.Timestamp('2024-01-10'), alpha=0.2, color='red')

# Black Friday
plt.axvspan(pd.Timestamp('2024-11-20'), pd.Timestamp('2024-11-30'), alpha=0.2, color='green', label='Black Friday')

# Férias de julho
plt.axvspan(pd.Timestamp('2024-07-01'), pd.Timestamp('2024-07-31'), alpha=0.2, color='orange', label='Férias de Julho')

plt.legend()
plt.tight_layout()
plt.savefig('vendas_diarias_padroes_corrigido.png', dpi=150, bbox_inches='tight')
plt.show()

print("\n" + "="*80)
print("GRÁFICO DE REFERÊNCIA SALVO:")
print("="*80)
print("Arquivo: 'vendas_diarias_padroes_corrigido.png'")
print("(Mostra os padrões sazonais embutidos nos dados)")