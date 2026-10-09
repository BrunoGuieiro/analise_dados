import streamlit as st
import pandas as pd
import numpy as np

st.title("Vendas da Padaria")

st.subheader("Cardápio e Preços")

itens = [
    "Pão Francês (kg)",
    "Pão de Queijo (un)",
    "Leite Integral (L)",
    "Queijo Mussarela (g)",
    "Presunto (g)",
    "Café Espesso (un)",
    "Bolo de Cenoura (fatia)",
]
precos = [14.90, 2.50, 5.80, 12.50, 9.80, 6.00, 8.50]

df = pd.DataFrame({"Item": itens, "Preço (R$)": precos})

st.write("Lista de produtos e valores:")
df
selecao = st.selectbox("Selecione um item:", itens)

st.write("Você selecionou:", selecao)
