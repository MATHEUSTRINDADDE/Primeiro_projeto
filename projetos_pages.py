import streamlit as st
# texte

st.set_page_config(
    page_title="Predição Médica",
    # icone que fica na aba da pagina do chrome
    page_icon="../img/stethoscope.png")

# bartra lateral
st.sidebar.header("Descrição do Projeto")
# st.sidebar.title("teste")
# imprimir texto
st.write("# Bem-Vindo a Predição Médica 🩺")
# lembre '\n' vai para proxima linha
st.write("\n\n")

# pegando imagem para colcoar na pagina
st.image('../img/health_insurance_img.jpg')
st.write("\n\n")


# colocação de texto na pagina 
# usando o markdown ja para se acostumar ele é emlhor que o write
st.markdown(
    """
    A previsão do seguro médico é crucial na área da saúde, pois prevê custos médicos e ajuda as organizações de saúde a se prepararem para as despesas.
    Ao analisar fatores como dados demográficos, histórico médico e estilo de vida, as seguradoras podem definir taxas de prêmio precisas
    e alocar recursos de forma eficaz. Isto também ajuda os indivíduos de alto risco a receberem os recursos e o apoio necessários.
    No geral, a previsão do seguro médico é uma ferramenta valiosa tanto para os pacientes como para os prestadores de um sistema de saúde sustentável.

    Este aplicativo tem como objetivo prever o custo do seguro usando recursos de entrada como:
    - idade
    - IMC
    - Número de filhos
    - Status de fumante
    """
)

# botaão verde sucess retorna botao verde
# caixabox verde
st.success("Por favor **vá para as próximas páginas** para obter as previsões.")


