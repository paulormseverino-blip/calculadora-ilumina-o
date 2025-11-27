import streamlit as st

st.title("Calculadora de Arquitetura 🏠")

# --- ZONA DE ENTRADA ---
col1, col2 = st.columns(2)

with col1:
    st.header("O Cômodo")
    largura = st.number_input("Largura (m)", min_value=0.0)
    comprimento = st.number_input("Comprimento (m)", min_value=0.0)

with col2:
    st.header("A Janela")
    janela_l = st.number_input("Largura Janela (m)", min_value=0.0)
    janela_a = st.number_input("Altura Janela (m)", min_value=0.0)

# --- O PORTEIRO (Botão) ---
if st.button("Calcular Agora"):
    
    area_piso = largura * comprimento
    area_janela = janela_l * janela_a
    
    if area_piso > 0:
        porcentagem = (area_janela / area_piso) * 100
        
        st.success("Cálculo realizado!")
        
        col_res1, col_res2 = st.columns(2)
        col_res1.metric("Área do Piso", f"{area_piso:.2f} m²")
        col_res2.metric("Ventilação", f"{porcentagem:.2f} %")
        
    else:
        st.error("Insira as medidas do cômodo.")