import pickle
import pandas as pd
import streamlit as st
# criando nova page e subindo arquivo cs para prever todas as linhas

# config da page
st.set_page_config(page_title="Predição em alto volume", 
                   page_icon="img/stethoscope.png")
st.sidebar.header('Arquivo para Prever')
st.title("Predições de Diversos Clientes")

st.markdown("Submeta seu arquivod e cleintes para podermos preve-lo:")

# -- Model -- #
with open('sub_modelo/modelo.pkl', 'rb') as file:
    model = pickle.load(file)

# fazendo o upload/submetendo arquivo em base
data = st.file_uploader('Submissão do arquivo')

if data:
    df_input = pd.read_csv(data)
    modelo = model.predict(df_input)
    # criando coluna com valroes predito
    df_output = df_input.assign(Predito=modelo)

    st.markdown('predições dos clientes')
    st.write(df_output)
    # função de download com a coluna de valores pedito
# nessa função temos que ter o label nome escrito no button
# data, a base colocando para qualtipo de arquivo, no nossoc aso csv 'to.csv'
# preferivel removermos o idnex
# e como é csv vamos colcoar o encoder para utf-/
# devemos por o mime para evitarmos o risco do navegador não interpreta direto o 'to.###(no nossoc aso csv)
# e fazer o doenlaod incorreto do dado
# o mime serve para definir o tipo do arquivo          
    st.download_button(
        label='Download CSV', data=df_output.to_csv(index=False).encode('utf-8'),
        mime='text/csv', file_name='predição_executada.csv'
        )
    
