import streamlit as st
import random
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Double Analyzer", layout="centered")

st.title("🎲 Double Analyzer - Previsão de Padrões")
st.markdown("Simulador para analisar jogadas e prever possíveis tendências de cor.")

# Cores possíveis
cores = ['vermelho', 'preto', 'branco']
cor_cores = {'vermelho': 'red', 'preto': 'black', 'branco': 'gray'}
num_cores = {'vermelho': 1, 'preto': 0, 'branco': 2}

# Simular jogadas
qtd = st.slider("Quantidade de jogadas simuladas", 20, 100, 50)
simular = st.button("🎰 Gerar jogadas")

if simular:
    historico = [random.choices(cores, weights=[47, 47, 6])[0] for _ in range(qtd)]

    df = pd.DataFrame({
        'Index': list(range(1, len(historico)+1)),
        'Cor': historico,
        'Valor': [num_cores[c] for c in historico]
    })

    st.subheader("📊 Histórico de jogadas")
    st.dataframe(df[['Index', 'Cor']].set_index('Index'))

    # Gráfico
    st.subheader("📈 Gráfico de sequência")
    fig, ax = plt.subplots()
    ax.plot(df['Index'], df['Valor'], marker='o', linestyle='-')
    ax.set_yticks([0, 1, 2])
    ax.set_yticklabels(['Preto', 'Vermelho', 'Branco'])
    ax.set_xlabel("Jogada")
    ax.set_ylabel("Cor")
    ax.grid(True)
    st.pyplot(fig)

    # Análise simples
    ultimas = historico[-5:]
    st.subheader("🧠 Análise dos últimos 5 resultados:")
    st.write("Últimas jogadas:", ultimas)

    if ultimas.count('vermelho') >= 4:
        st.warning("⚠️ Tendência de VERMELHO! Possível inversão para PRETO.")
    elif ultimas.count('preto') >= 4:
        st.warning("⚠️ Tendência de PRETO! Possível inversão para VERMELHO.")
    elif 'branco' in ultimas:
        st.info("⚪ Saiu BRANCO recentemente. Padrões podem mudar.")
    else:
        st.success("🔄 Sem padrão dominante detectado.")
