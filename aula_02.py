import streamlit as st

# titulo da pagina

st.title("Elementos Interativos de Layout")

# barra lateral

st.sidebar.header(('Opções da Aplicação'))
nome = st.sidebar.text_input(label='Digite o seu nome')
st.sidebar.write(f'Ola {nome}!')

# Colunas para organizar o conteudo principal

colunas = st.columns(2)

with colunas[0]:
    st.header('interações simples')
    if st.button('clique'):
        st.success('você clicou no botão')

    valor_slider = st.slider(
        label='selecione um valor',
        min_value=0,
        max_value=100,
        value=50
    )
    st.write(f'O valor selecionado no slider foi {valor_slider}')

with colunas[1]:
    st.header('Informações e imagens')
    st.info('Esta é uma mensagem informativa')

    # Pode usar uma url para colocar uma imagem ou de um caminho local
    st.image(
        image=(
            'https://tse2.mm.bing.net/th/id/OIP.AR-2Upm6CRA5R5_hRE_rQQHaEP'
            '?rs=1&pid=ImgDetMain&o=7&rm=3'
        ),
        caption='Flor com gotas de orvalho',
        width="stretch",
    )
    st.warning('Atenção este e um aviso')

# entrada do numero de exibição

numero = st.number_input(
    label='Digite um numero de 1 a 100',
    min_value=0,
    max_value=100,
)

st.write(f'Você digitou o numero {numero}')
