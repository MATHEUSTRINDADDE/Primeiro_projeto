# configurando a pagina que vai ficar a predição
# no streamlit ao criar uma pasta dentro da pasta que esta executando o arquivo python
# ele ja entende que esse arquivo pode ouf azer parte do projeto para ir no site
import numpy as np
import pickle
import pandas as pd
import streamlit as st

# config aba pagina
# quando é multipages esse titulo fica do lado
st.set_page_config(page_title="A predição", 
                   page_icon="../img/stethoscope.png")

# nome na pagina lateral
st.sidebar.header('Predição')
# titulo na pagina
st.title("Sua Predição Médica")

st.markdown(
    "### Vamos **Prever** seu custo de sinistro?"
)

# fazendo os botões para pegar as caracteristicas
age = st.number_input(label="idade",value=20,min_value=18,max_value=100)
bmi = st.number_input("BMI" , value=30.)
children = st.number_input("Filhos", min_value=0, max_value=5)
# caixa de listagem
smoker = st.selectbox("Fuma?", options=["yes",'No'])


# puxando modelo
with open('sub_modelo/modelo.pkl','rb') as model_file:
    model = pickle.load(model_file)


def pred():
    df_input = pd.DataFrame({
    'age': [age],
    'bmi' : [bmi],
    'children' : [children],
    'smoker' : [smoker]        
    }) 

    pred_model = model.predict(df_input)[0].round(2)
    return pred_model

# valdiando para caso de erro
# try executa se nada river errado e caso ter mostrar oq fazer
# usando o except
# lembra que no button o click é true
if st.button("Predição"):
    try:
        modelo =pred()
        st.success(f'Seu Valor de Sinistro é {modelo}$')
    except Exception as error:
        st.error(f"talvez sua planilha esta vazia, {error}") 

