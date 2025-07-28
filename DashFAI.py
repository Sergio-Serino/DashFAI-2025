


import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

#Impresão do Logo do Centro Universitário Assunção no topo esquerdo da página

st.image("Logo_FAI.png", width=250)


st.set_page_config(layout="wide") # Opcional: para usar a largura total da tela



###

# Leitura do Banco de Dados
caminho_arquivo = 'C:/Users/sseri/Downloads/Tabela_Dados.xlsx'
df = pd.read_excel(caminho_arquivo, engine='openpyxl')


data = df['Localizacao'].value_counts().reset_index()
data.columns = ['Localizacao', 'Quantidade']

# Filtros 
st.sidebar.header("Selecione os Filtros")

# Filtro por ano mínimo usando select_slider

# Converter para datetime
df['Inicio_atividade'] = pd.to_datetime(df['Inicio_atividade'], errors='coerce')
df['Ano'] = df['Inicio_atividade'].dt.year

ano_minimo = int(df['Ano'].min())
ano_maximo = int(df['Ano'].max())
ano_inicio = st.sidebar.select_slider("Ano mínimo de Início de Atividade:", options=sorted(df['Ano'].dropna().unique()), value=ano_minimo)
df = df[df['Ano'] >= ano_inicio]

# Filtro de Localização
Filtro_Local = st.sidebar.multiselect("Escolha a Localização:", df['Localizacao'].unique())
if Filtro_Local:
    df = df[df['Localizacao'].isin(Filtro_Local)]

# Filtro de Ramo de Atividade
Filtro_Ramo = st.sidebar.multiselect("Escolha o Ramo de Atividade:", df['Ramo_atividade'].unique())
if Filtro_Ramo:
    df = df[df['Ramo_atividade'].isin(Filtro_Ramo)]

# Filtro de Porte das Empresas
Filtro_Porte = st.sidebar.multiselect("Escolha o Porte das Empresas:", df['Porte_empresa'].unique())
if Filtro_Porte:
    df = df[df['Porte_empresa'].isin(Filtro_Porte)]

# Filtro de Regime Tributário das Empresas
Filtro_Tributario = st.sidebar.multiselect("Escolha o Regime Tributário:", df['Regime_tributario'].unique())
if Filtro_Tributario:
    df = df[df['Regime_tributario'].isin(Filtro_Tributario)]

# Filtro de Natureza Jurídica das Empresas
Filtro_Juridico = st.sidebar.multiselect("Escolha o Natureza Jurídica:", df['Natureza_Juridica'].unique())
if Filtro_Juridico:
    df = df[df['Natureza_Juridica'].isin(Filtro_Juridico)]

# Filtro de Tipo de Contabilidade das Empresas
Filtro_Contabilidade = st.sidebar.multiselect("Escolha o Tipo de Contabilidade:", df['Tipo_contabilidade'].unique())
if Filtro_Juridico:
    df = df[df['Tipo_contabilidade'].isin(Filtro_Contabilidade)]


num_empresas = df.shape[0]

st.markdown(
    f"<h4 style='text-align: center;'>Dados de {num_empresas} Empresas no Entorno do Centro Universitário Assunção em 2025</h3>",
    unsafe_allow_html=True
)



col1_row1, col2_row1, col3_row1 = st.columns([10, 10, 10])
with col1_row1:
    # st.subheader("Gráfico 1 (Coluna 1, Linha 1 - Gráfico de Rosca)")
    # Gráfico de rosca com Plotly Express

    # contando os dados acumulados e renomeando as colunas q foram separadas
    data = df['Localizacao'].value_counts().reset_index()
    data.columns = ['Localizacao', 'Quantidade']
    df_donut = data
    
    fig = px.pie(df_donut, values='Quantidade', names='Localizacao',
                 title='Localização', hole=0.5)
    fig.update_layout(legend_itemclick=False, legend_itemdoubleclick=False)
    fig.update_traces(textinfo='value')

    st.plotly_chart(fig, use_container_width=True)

with col2_row1:
    # st.subheader("Gráfico 2 (Coluna 2, Linha 1 - Barras Horizontais)")
    # Gráfico de barras horizontais com Plotly Express

    data = df['Ramo_atividade'].value_counts().reset_index()
    data.columns = ['Ramo_atividade', 'Quantidade']
    data_horizontal_bar_2 = data

    df_horizontal_bar_2 = pd.DataFrame(data_horizontal_bar_2)
    fig = px.bar(df_horizontal_bar_2, x='Quantidade', y='Ramo_atividade', orientation='h',
                 title='Ramo de Atividade')
    fig.update_layout(yaxis_title=None)

    fig.update_traces(text=df_horizontal_bar_2['Quantidade'], # Define qual coluna será o texto
                  textposition='outside') # Posição do texto: 'inside' ou 'outside'
    
    # --- ADIÇÃO CRÍTICA: Ajustar o alcance do eixo X para evitar truncamento ---
    # Calcule o valor máximo da 'Quantidade'
    max_quantidade = df_horizontal_bar_2['Quantidade'].max()

    # Aumente o limite superior do eixo X um pouco (ex: 10% a mais)
    # Isso cria um espaço extra à direita da barra mais longa para o número
    fig.update_layout(xaxis_range=[0, max_quantidade * 1.20]) # Aumenta 10% no eixo X
    # -------------------------------------------------------------------------

    st.plotly_chart(fig, use_container_width=True)

with col3_row1:
    # st.subheader("Gráfico 3 (Coluna 3, Linha 1 - Barras Horizontais)")
    # Gráfico de barras horizontais

    data = df['Porte_empresa'].value_counts().reset_index()
    data.columns = ['Porte_empresa', 'Quantidade']
    df_bar_3 = data

    fig = px.bar(df_bar_3, x='Quantidade', y='Porte_empresa', orientation='h',
                 title='Porte da Empresa')
    fig.update_layout(yaxis_title=None)

    fig.update_traces(text=df_bar_3['Quantidade'], # Define qual coluna será o texto
                  textposition='outside') # Posição do texto: 'inside' ou 'outside'
    
    # --- ADIÇÃO CRÍTICA: Ajustar o alcance do eixo X para evitar truncamento ---
    # Calcule o valor máximo da 'Quantidade'
    max_quantidade = df_bar_3['Quantidade'].max()

    # Aumente o limite superior do eixo X um pouco (ex: 10% a mais)
    # Isso cria um espaço extra à direita da barra mais longa para o número
    fig.update_layout(xaxis_range=[0, max_quantidade * 1.30]) # Aumenta 10% no eixo X
    # -------------------------------------------------------------------------

    st.plotly_chart(fig, use_container_width=True)

###

col1_row2, col2_row2, col3_row2 = st.columns([1, 3, 1])
with col1_row2:
   #  st.subheader("Gráfico 4 (Coluna 1, Linha 2 - Barras Horizontais)")
    # Gráfico de barras horizontais

    data = df['Regime_tributario'].value_counts().reset_index()
    data.columns = ['Regime_tributario', 'Quantidade']    
    df_bar_4 = data

    fig = px.bar(df_bar_4, x='Quantidade', y='Regime_tributario', orientation='h',
                 title='Regime Tributário')
    fig.update_layout(yaxis_title=None)

    fig.update_traces(text=df_bar_4['Quantidade'], # Define qual coluna será o texto
                  textposition='outside') # Posição do texto: 'inside' ou 'outside'
    
    # --- ADIÇÃO CRÍTICA: Ajustar o alcance do eixo X para evitar truncamento ---
    # Calcule o valor máximo da 'Quantidade'
    max_quantidade = df_bar_4['Quantidade'].max()

    # Aumente o limite superior do eixo X um pouco (ex: 10% a mais)
    # Isso cria um espaço extra à direita da barra mais longa para o número
    fig.update_layout(xaxis_range=[0, max_quantidade * 1.50]) # Aumenta 10% no eixo X
    # -------------------------------------------------------------------------

    st.plotly_chart(fig, use_container_width=True)

with col2_row2:
    # st.subheader("Gráfico 5 (Coluna 2, Linha 2 - Barras Horizontais)")
    # Gráfico de barras horizontais

    data = df['Natureza_Juridica'].value_counts().reset_index()
    data.columns = ['Natureza_Juridica', 'Quantidade']
    df_bar_5 = data

    fig = px.bar(df_bar_5, x='Quantidade', y='Natureza_Juridica', orientation='h',
                 title='Natureza Jurídica')
    fig.update_layout(yaxis_title=None)

    fig.update_traces(text=df_bar_5['Quantidade'], # Define qual coluna será o texto
                  textposition='outside') # Posição do texto: 'inside' ou 'outside'
    
    # --- ADIÇÃO CRÍTICA: Ajustar o alcance do eixo X para evitar truncamento ---
    # Calcule o valor máximo da 'Quantidade'
    max_quantidade = df_bar_5['Quantidade'].max()

    # Aumente o limite superior do eixo X um pouco (ex: 10% a mais)
    # Isso cria um espaço extra à direita da barra mais longa para o número
    fig.update_layout(xaxis_range=[0, max_quantidade * 1.30]) # Aumenta 10% no eixo X
    # -------------------------------------------------------------------------

    st.plotly_chart(fig, use_container_width=True)

with col3_row2:
    # st.subheader("Gráfico 6 (Coluna 3, Linha 2 - Barras Horizontais)")
    # Espaço vazio
    data = df['Tipo_contabilidade'].value_counts().reset_index()
    data.columns = ['Tipo_contabilidade', 'Quantidade']
    df_bar_5 = data

    fig = px.bar(df_bar_5, x='Quantidade', y='Tipo_contabilidade', orientation='h',
                 title='Tipo de Contabilidade')
    fig.update_layout(yaxis_title=None)

    fig.update_traces(text=df_bar_5['Quantidade'], # Define qual coluna será o texto
                  textposition='outside') # Posição do texto: 'inside' ou 'outside'
    
# --- ADIÇÃO CRÍTICA: Ajustar o alcance do eixo X para evitar truncamento ---
    # Calcule o valor máximo da 'Quantidade'
    max_quantidade = df_bar_5['Quantidade'].max()

    # Aumente o limite superior do eixo X um pouco (ex: 10% a mais)
    # Isso cria um espaço extra à direita da barra mais longa para o número
    fig.update_layout(xaxis_range=[0, max_quantidade * 1.50]) # Aumenta 10% no eixo X
    # -------------------------------------------------------------------------

    st.plotly_chart(fig, use_container_width=True)
 

###

col1_row3, col2_row3, col3_row3 = st.columns([1, 80, 1])
with col1_row3:
    # st.subheader("Gráfico 7 (Coluna 1, Linha 3 - Gráfico de Linha)") # Updated subheader
    st.subheader(" ")

with col2_row3:
    # st.subheader("Gráfico 7 (Coluna 1, Linha 3 - Gráfico de Linha)") # Updated subheader
    # Transformado em gráfico de linha

    
    df['Ano'] = pd.to_datetime(df['Inicio_atividade']).dt.year
    data = df['Ano'].value_counts().reset_index()
    data.sort_values(by='Ano', ascending=True, inplace = True)
    data.columns = ['Ano', 'Quantidade']
    df_line_7 = data
    
    # For a line chart, one axis should typically be quantitative and represent a trend
    # Here, 'Departamento' is categorical, so the line will connect points based on their order in the DataFrame.
    fig = px.line(df_line_7, x='Ano', y='Quantidade',
                 title='Início das Atividades',
                 markers=True) # Added markers to show individual data points
    st.plotly_chart(fig, use_container_width=True)

with col3_row3:
    # st.subheader("Gráfico 9 (Coluna 3, Linha 3 - Barras Horizontais)")
    # Novo gráfico de barras horizontais
    st.subheader(" ")
   
