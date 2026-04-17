import streamlit as st
import pandas as pd
import sqlite3

st.set_page_config(layout="wide") 

st.title("📊 Painel de Dados")

#=========================================#
#             VARIAVEIS VIEWS             #
#=========================================#

@st.cache_data
def exemplo_head():
    conn = sqlite3.connect('[INSERIR OS DADOS]') 
    query = "SELECT * FROM [INSERIR OS DADOS]"
    df = pd.read_sql(query, conn)
    conn.close()
    return df

df = exemplo_head()

@st.cache_data
def exemplo_diarias():
    conn = sqlite3.connect('[INSERIR OS DADOS]') 
    query = "SELECT * FROM [INSERIR OS DADOS]"
    df = pd.read_sql(query, conn)
    conn.close()
    return df

df2 = exemplo_diarias()

#======================================#
#             LIMPA FILTRO             #
#======================================#

def limpar_filtros():
    st.session_state['key_A']    = "Todas"
    st.session_state['key_B']    = "Todas"
    st.session_state['key_C']    = "Todas"
    st.session_state['key_D']    = "Todas"
    st.session_state['key_E']    = "Todas"

st.sidebar.header("Filtros")

st.sidebar.button("🔄 Limpar filtros",
                  on_click=limpar_filtros,
                  use_container_width=True)
st.sidebar.markdown("---")

#======================================#
#          VARIAVEIS FILTROS           #
#======================================#

datas_unicas = df['[INSERIR OS DADOS]'].dropna().unique().tolist()

filtro_A = sorted(datas_unicas, key=lambda x: pd.to_datetime(x, dayfirst=True))
opcoes_filtro_A = ["Todas"] + filtro_A
A_selecionados = st.sidebar.selectbox(
    "Selecione [INSERIR OS DADOS]", 
    options=opcoes_filtro_A,
    key='key_A'
)

filtro_B = sorted(df['[INSERIR OS DADOS]'].dropna().unique().tolist())
opcoes_filtro_B = ["Todas"] + filtro_B
B_selecionados = st.sidebar.selectbox(
    "Selecione [INSERIR OS DADOS]",
    options=opcoes_filtro_B,
    key='key_B'
)

filtro_C = sorted(df['[INSERIR OS DADOS]'].dropna().unique().tolist())
opcoes_filtro_C = ["Todas"] + filtro_C
C_selecionados = st.sidebar.selectbox(
    "Selecione [INSERIR OS DADOS]",
    options=opcoes_filtro_C,
    key='key_C'
)

filtro_D = sorted(df['[INSERIR OS DADOS]'].dropna().unique().tolist())
opcoes_filtro_D = ["Todas"] + filtro_D
D_selecionados = st.sidebar.selectbox(
    "Selecione [INSERIR OS DADOS]",
    options=opcoes_filtro_D,
    key='key_D'
)

filtro_E = sorted(df['[INSERIR OS DADOS]'].dropna().unique().tolist())
opcoes_filtro_E = ["Todas"] + filtro_E
E_selecionados = st.sidebar.selectbox(
    "Selecione [INSERIR OS DADOS]",
    options=opcoes_filtro_E,
    key='key_E'
)

#======================================#
#          FILTROS LÓGICA              #
#======================================#

df_filtrado = df.copy()
df2_filtrado = df2.copy()

if A_selecionados != "Todas":
    df_filtrado = df_filtrado[df_filtrado["[INSERIR OS DADOS]"] == 
    A_selecionados]
    df2_filtrado = df2_filtrado[df2_filtrado["[INSERIR OS DADOS]"] == 
    A_selecionados]

if B_selecionados != "Todas":
    df_filtrado = df_filtrado[df_filtrado["[INSERIR OS DADOS]"] == B_selecionados]
    df2_filtrado = df2_filtrado[df2_filtrado["[INSERIR OS DADOS]"] == B_selecionados]

if C_selecionados != "Todas":
    df_filtrado = df_filtrado[df_filtrado["[INSERIR OS DADOS]"] == C_selecionados]
    df2_filtrado = df2_filtrado[df2_filtrado["[INSERIR OS DADOS]"] == C_selecionados]

if D_selecionados != "Todas":
    df_filtrado = df_filtrado[df_filtrado["[INSERIR OS DADOS]"] == D_selecionados]
    df2_filtrado = df2_filtrado[df2_filtrado["[INSERIR OS DADOS]"] == D_selecionados]

if E_selecionados != "Todas":
    df_filtrado = df_filtrado[df_filtrado["[INSERIR OS DADOS]"] == 
    E_selecionados]
    df2_filtrado = df2_filtrado[df2_filtrado["[INSERIR OS DADOS]"] == 
    E_selecionados]

#=============================================#
#          EXIBIÇÃO DT PRINCIPAL              #
#=============================================#

st.subheader("[INSERIR OS DADOS]")

st.dataframe(
    df_filtrado, 
    use_container_width=True, 
    hide_index=True,          
    column_config={
        "[INSERIR OS DADOS]": "[INSERIR OS DADOS]",
        "[INSERIR OS DADOS]": "[INSERIR OS DADOS]",
        "[INSERIR OS DADOS]": "[INSERIR OS DADOS]",
        "[INSERIR OS DADOS]": "[INSERIR OS DADOS]",
        "[INSERIR OS DADOS]": "[INSERIR OS DADOS]",
        "[INSERIR OS DADOS]": "[INSERIR OS DADOS]",
        "[INSERIR OS DADOS]": "[INSERIR OS DADOS]",
        "[INSERIR OS DADOS]": "[INSERIR OS DADOS]",
        "[INSERIR OS DADOS]": "[INSERIR OS DADOS]",
        "[INSERIR OS DADOS]": "[INSERIR OS DADOS]",
        "[INSERIR OS DADOS]": "[INSERIR OS DADOS]",
        "[INSERIR OS DADOS]": "[INSERIR OS DADOS]"
    }
)

st.write(f"Exibindo **{len(df_filtrado)}** registros.")

#==============================================#
#          EXIBIÇÃO DT SECUNDARIO              #
#==============================================#

st.markdown("---")

st.subheader("[INSERIR OS DADOS]")

st.dataframe(
    df2_filtrado,
    use_container_width=True, 
    hide_index=True,
    column_config={
        "[INSERIR OS DADOS]": "[INSERIR OS DADOS]",
        "[INSERIR OS DADOS]": "[INSERIR OS DADOS]",
        "[INSERIR OS DADOS]": "[INSERIR OS DADOS]",
        "[INSERIR OS DADOS]": "[INSERIR OS DADOS]",
        "[INSERIR OS DADOS]": "[INSERIR OS DADOS]",
        "[INSERIR OS DADOS]": "[INSERIR OS DADOS]",
        "[INSERIR OS DADOS]": "[INSERIR OS DADOS]"
    }
)

st.write(f"Exibindo **{len(df2_filtrado)}** registros.")
