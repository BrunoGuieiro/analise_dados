import streamlit as st
import pandas as pd
import numpy as np

st.title("Notas 3 Etapa")

st.subheader("3A1")

nome = st.text_input("Digite o seu nome: ")

st.write("Olá,", nome, "bem-vindo ao Colegio Cotemig")

st.write("------------------------------------------------------------------")

df = pd.DataFrame({'disciplina': ["Python", "Matematica", "Portugues"], 'nota': [10,5,0]})

df

st.write("A Eliza esta brava, estude mais portugues")

st.write("----------------------------------------------------------------")

selecao = st.selectbox("Selecione o que estudar: ", ["Portugues", "Matematica", "Python"])

st.write("Voce selecionou", selecao)