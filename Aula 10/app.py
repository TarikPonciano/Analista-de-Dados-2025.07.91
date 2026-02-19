# pip install streamlit

import streamlit as st

# Header 1
st.title("Hello World")

# Text
st.write("Teste")

# Cabeçalhos

st.header("Início de Seção")

st.subheader("Subtítulo de seção")

st.markdown("Texto estilizado")

#Interação

nome = st.text_input("Digite seu nome:")
idade = st.number_input("Digite sua idade:", min_value=0, max_value=120)

# Exibir na tela o nome e a idade digitados

# Bônus: Exibir um trecho que informa se a pessoa é maior ou menor de idade
print(f'''
Nome: {nome}
Idade: {idade}
''')

# Rodar no terminal o comando "streamlit run app.py"