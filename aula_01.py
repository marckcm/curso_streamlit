import streamlit as st

# uv run streamlit run aula_01.py - para executar o script

# Títulos
st.title("Streamlit")

st.header("O que é o Streamlit?")

st.write("""O Streamlit é um framework de código aberto em Python, \
    projetado para criar e compartilhar rapidamente aplicações web \
    interativas, especialmente voltadas para projetos de ciência \
    de dados e aprendizado de máquina. Ele permite que cientistas \
    de dados e engenheiros de machine learning transformem seus \
    códigos em interfaces web funcionais sem a necessidade de \
    conhecimentos em desenvolvimento front-end, como HTML, CSS ou \
    JavaScript. Com o Streamlit, é possível criar aplicações \
    que exibem gráficos, tabelas, widgets interativos e até mesmo \
    realizar previsões de modelos de machine learning. Tudo isso \
    com poucas linhas de código, tornando o processo rápido e acessível.""")

st.subheader("Principais Características")
st.write(""" -Fácil de usar: Não é necessário conhecimento prévio de
desenvolvimento web. Com comandos simples, como st.write() ou st.button(), é
possível adicionar textos, gráficos e interatividade à aplicação.

- Integração com bibliotecas Python: Compatível com ferramentas populares como
Pandas, Matplotlib, Seaborn, Plotly, Keras e PyTorch.

- Interatividade: Permite criar widgets como sliders, caixas de seleção,
botões e gráficos interativos para facilitar a interação do
usuário com os dados.

- Deploy simplificado: Após criar a aplicação, é possível disponibilizá-la na 
web rapidamente, utilizando serviços como o Streamlit Cloud, que gera uma URL 
pública para compartilhamento.""")

st.subheader("Principais atalhos e exemplos markdown")

# Tambem podemos usar o markdown para escrever o texto
st.markdown("""
- Títulos:
# Título 1 🙌
## Título 2
### Título 3
para diferentes níveis de cabeçalho clickup.com.
- Negrito: **texto** ou __texto__ para destacar palavras olhardigital.com.br.
- Itálico: *texto* ou _texto_.
- Listas:
    - Não numeradas:
        * item
        - item
    - Numeradas:
        1. item 🚀
        2. item 🚀
- Links: [emojis para markdown](https://emojipedia.org/) ----
    [converter para markdown](https://markdown-it.github.io/)
- Imagens: ![alt text](URL da imagem).
- Citações: > citação.
- Código inline: `código`.
- Blocos de código: ```linguagem ```.
- Tabelas: usando | e - para separar colunas e linhas (suporte em 
MultiMarkdown e editores avançados), clickup.com.""")
