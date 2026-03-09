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
st.divider()

nome = st.text_input("Digite seu nome:")
idade = st.number_input("Digite sua idade:", min_value=0, max_value=120)

faixa_etaria = "Menor de Idade"
if idade >= 18:
    faixa_etaria = "Maior de Idade"

botao_entrar = st.button("ENTRAR")

# Exibir na tela o nome e a idade digitados

# Bônus: Exibir um trecho que informa se a pessoa é maior ou menor de idade
if botao_entrar:
    st.divider()
    if nome == "":
        st.write("NOME VAZIO!")
    else:
        st.write(f'''
        Nome: {nome}

        Idade: {idade}

        Faixa Etária: {faixa_etaria}
        ''')

# Rodar no terminal o comando "streamlit run app.py"