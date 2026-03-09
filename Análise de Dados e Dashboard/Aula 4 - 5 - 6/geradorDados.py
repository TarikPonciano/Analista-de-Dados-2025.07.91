"""
GERADOR SIMPLIFICADO DE DADOS CLÍNICOS
Foco em problemas comuns sem complexidades desnecessárias
"""
import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# Configuração
np.random.seed(42)
random.seed(42)

# ============================================================================
# LISTAS SIMPLIFICADAS
# ============================================================================

# Nomes completos prontos (sem problemas de junção)
nomes = [
    "Ana", "Bruno", "Carlos", "Daniel", "Eduardo", "Fernanda", "Gabriel", "Helena",
    "Igor", "Juliana", "Lucas", "Mariana", "Nicolas", "Olivia", "Paulo",
    "Rafaela", "Samuel", "Tatiane", "Victor", "Yasmin",
    "André", "Beatriz", "Caio", "Débora", "Elisa", "Felipe", "Giovana", "Hugo",
    "Isabela", "João"
]

sobrenomes = [
    "Silva", "Santos", "Oliveira", "Pereira", "Costa", "Rodrigues", "Alves",
    "Lima", "Gomes", "Ribeiro", "Martins", "Araujo", "Rocha", "Teixeira",
    "Fernandes", "Batista", "Nogueira", "Freitas", "Pacheco", "Farias"
]

# Gera nomes completos únicos
NOMES_COMPLETOS = sorted({
    f"{nome} {sobrenome}"
    for nome in nomes
    for sobrenome in sobrenomes
})

# Especialidades médicas
ESPECIALIDADES = ['CARDIOLOGIA', 'DERMATOLOGIA', 'PEDIATRIA', 'ORTOPEDIA', 
                  'GINECOLOGIA', 'CLINICO GERAL', 'NEUROLOGIA', 'OFTALMOLOGIA']

# ============================================================================
# FUNÇÕES SIMPLIFICADAS DE GERAÇÃO
# ============================================================================

def gerar_nome_simples():
    """Gera nome com problemas básicos de formatação"""
    nome = random.choice(NOMES_COMPLETOS)
    
    # Aplicar problemas simples em 30% dos casos
    if random.random() < 0.3:
        tipo_problema = random.choice(['maiusculas', 'minusculas', 'espacos'])
        
        if tipo_problema == 'maiusculas':
            return nome.upper()  # MARIA SILVA
        elif tipo_problema == 'minusculas':
            return nome.lower()  # maria silva
        elif tipo_problema == 'espacos':
            return f"  {nome}  "  #   Maria Silva  
    
    return nome  # 70% normal

def gerar_idade_simples():
    """Gera idade com problemas muito simples"""
    if random.random() < 0.9:  # 90% idades normais
        idade = random.randint(1, 90)
        # 20% das normais como string
        if random.random() < 0.2:
            return str(idade)
        return idade
    else:  # 10% problemas simples
        problemas = ['', ' ', 'N/A']
        return random.choice(problemas)

def gerar_sexo_simples():
    """Gera sexo com variações simples"""
    opcoes = ['M', 'F', 'Masculino', 'Feminino', ' ', '']
    pesos = [0.35, 0.35, 0.1, 0.1, 0.05, 0.05]
    return random.choices(opcoes, weights=pesos, k=1)[0]

def gerar_data_simples():
    """Gera data apenas em formatos válidos"""
    data = datetime(2025, 1, 1) + timedelta(days=random.randint(0, 365))
    
    # Apenas dois formatos válidos
    if random.random() < 0.7:  # 70% formato BR
        return data.strftime('%d/%m/%Y')
    else:  # 30% formato US
        return data.strftime('%Y-%m-%d')

def gerar_especialidade_simples():
    """Gera especialidade com problemas simples"""
    if random.random() < 0.85:  # 85% normal
        especialidade = random.choice(ESPECIALIDADES)
        
        # 20% chance de problemas leves
        if random.random() < 0.2:
            problemas = [
                f" {especialidade} ",  # Espaços extras
                especialidade.lower(),  # Minúsculas
                especialidade.replace(' ', '_'),  # Com underscore
            ]
            return random.choice(problemas)
        return especialidade
    else:  # 15% problemas
        problemas = ['', ' ', None]
        return random.choice(problemas)

def gerar_valor_simples(especialidade):
    """Gera valor baseado na especialidade"""
    # Valores base por especialidade (mínimo, máximo)
    valores_base = {
        'CARDIOLOGIA': (300, 500),
        'DERMATOLOGIA': (200, 350),
        'PEDIATRIA': (150, 250),
        'ORTOPEDIA': (250, 400),
        'GINECOLOGIA': (180, 320),
        'CLINICO GERAL': (120, 200),
        'NEUROLOGIA': (350, 600),
        'OFTALMOLOGIA': (180, 350)
    }
    
    # Encontrar especialidade correspondente (ignorando formatação)
    especialidade_normalizada = str(especialidade).upper().strip()
    for esp in valores_base:
        if esp in especialidade_normalizada:
            min_val, max_val = valores_base[esp]
            break
    else:
        min_val, max_val = (100, 400)  # Valor padrão
    
    valor = random.randint(min_val, max_val) + round(random.random(), 2)
    return round(valor, 2)

def gerar_tempo_simples(especialidade):
    """Gera tempo baseado na especialidade"""
    # Tempos base por especialidade (mínimo, máximo em minutos)
    tempos_base = {
        'CARDIOLOGIA': (30, 60),
        'DERMATOLOGIA': (20, 40),
        'PEDIATRIA': (20, 40),
        'ORTOPEDIA': (25, 50),
        'GINECOLOGIA': (25, 45),
        'CLINICO GERAL': (15, 30),
        'NEUROLOGIA': (40, 80),
        'OFTALMOLOGIA': (20, 40)
    }
    
    especialidade_normalizada = str(especialidade).upper().strip()
    for esp in tempos_base:
        if esp in especialidade_normalizada:
            min_tempo, max_tempo = tempos_base[esp]
            break
    else:
        min_tempo, max_tempo = (15, 60)
    
    return random.randint(min_tempo, max_tempo)

def gerar_retorno_simples():
    """Gera retorno com variações simples"""
    opcoes = ['Sim', 'Não', 'SIM', 'NÃO', 'sim', 'não', ' ', '']
    pesos = [0.3, 0.3, 0.1, 0.1, 0.05, 0.05, 0.05, 0.05]
    return random.choices(opcoes, weights=pesos, k=1)[0]

# ============================================================================
# GERAÇÃO DO DATASET
# ============================================================================

def criar_dataset_simples(num_registros=10000):
    """Cria dataset simplificado"""
    print(f"🚀 Gerando {num_registros:,} registros...")
    
    dados = []
    for i in range(num_registros):
        if (i + 1) % 2000 == 0:
            print(f"   ✅ {i+1:,} registros gerados...")
        
        especialidade = gerar_especialidade_simples()
        
        registro = {
            'ID': f"P{i+1:05d}",
            'Nome': gerar_nome_simples(),
            'Idade': gerar_idade_simples(),
            'Sexo': gerar_sexo_simples(),
            'Data_Consulta': gerar_data_simples(),
            'Especialidade': especialidade,
            'Valor': gerar_valor_simples(especialidade),
            'Tempo_Minutos': gerar_tempo_simples(especialidade),
            'Retorno': gerar_retorno_simples()
        }
        dados.append(registro)
    
    # Criar DataFrame
    df = pd.DataFrame(dados)
    
    # Adicionar duplicatas (5%)
    num_duplicatas = int(len(df) * 0.05)
    duplicatas = df.sample(n=num_duplicatas, random_state=42)
    df = pd.concat([df, duplicatas], ignore_index=True)
    
    # Embaralhar
    df = df.sample(frac=1, random_state=42).reset_index(drop=True)
    
    # Atualizar IDs
    df['ID'] = [f"P{i+1:05d}" for i in range(len(df))]
    
    return df

# ============================================================================
# EXECUÇÃO PRINCIPAL
# ============================================================================

if __name__ == "__main__":
    print("="*60)
    print("GERADOR SIMPLIFICADO DE DADOS CLÍNICOS")
    print("="*60)
    print("Foco nos problemas mais comuns:")
    print("  • Nomes: maiúsculas/minúsculas, espaços extras")
    print("  • Idades: strings, vazias, 'N/A'")
    print("  • Sexo: formatos diferentes, vazios")
    print("  • Datas: formatos diferentes (sempre válidas)")
    print("  • Especialidade: nulos, vazias, minúsculas")
    print("  • Retorno: formatos diferentes")
    print("  • Duplicatas: 5% dos registros")
    print("="*60)
    
    # Gerar dataset
    df = criar_dataset_simples(10000)
    
    # Salvar
    df.to_excel('dados_clinica_simplificado.xlsx', index=False, engine='openpyxl')
    
    print(f"\n✅ Dataset salvo com {len(df):,} registros")
    print("📊 Problemas inseridos:")
    
    # Análise rápida
    print("\n📝 ANÁLISE DOS PROBLEMAS:")
    print(f"  1. Nomes com problemas: {sum(df['Nome'].str.isupper() | df['Nome'].str.islower() | df['Nome'].str.startswith(' ')):,}")
    print(f"  2. Idades problemáticas: {sum(df['Idade'].astype(str).str.strip().isin(['', 'N/A'])):,}")
    print(f"  3. Sexo não padronizado: {sum(~df['Sexo'].isin(['M', 'F'])):,}")
    print(f"  4. Especialidades nulas/vazias: {df['Especialidade'].isnull().sum() + (df['Especialidade'] == '').sum():,}")
    print(f"  5. Duplicatas: {int(len(df) * 0.05):,}")
    
    print("\n📄 AMOSTRA DOS DADOS:")
    print(df.head(10).to_string())
    
    print("\n" + "="*60)
    print("PRONTO PARA A ATIVIDADE DE LIMPEZA!")
    print("Arquivo: dados_clinica_simplificado.xlsx")
    print("="*60)