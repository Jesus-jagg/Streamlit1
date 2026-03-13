import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Configuración profesional de la página
st.set_page_config(page_title="Concrete Analysis Pro", layout="wide")

# --- ESTILOS PERSONALIZADOS ---
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stButton>button { background-color: #4A90E2; color: white; border-radius: 5px; }
    .sidebar .sidebar-content { background-color: #2c3e50; }
    </style>
    """, unsafe_allow_html=True)

# --- CARGA DE DATOS ---
@st.cache_data
def load_data():
    # Asumimos nombres de columnas limpios para facilitar el análisis
    df = pd.read_csv("concrete_data.csv")
    return df

try:
    df = load_data()
except:
    st.error("Error: Asegúrate de tener el archivo 'concrete_data.csv'.")
    st.stop()

# --- BARRA LATERAL ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/4300/4300058.png", width=100)
    st.title("Panel de Control")
    st.info(f"Autor: Jesus Alonso Garcia Gutierrez")
    menu = st.radio("Secciones", ["🏠 Inicio / Landing", "📊 Panel de Análisis", "🧮 Simulador"])

# --- SECCIÓN 1: LANDING PAGE ---
if menu == "🏠 Inicio / Landing":
    st.title("🏗️ Optimización de Mezclas de Concreto")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("¿Qué estamos analizando?")
        st.write("""
        La resistencia a la compresión es la propiedad más importante del concreto. 
        Este dataset de Kaggle contiene información sobre mezclas que incluyen:
        * **Cemento y Agua:** La base de la reacción química.
        * **Agregados:** Grava y arena que dan cuerpo.
        * **Aditivos:** Ceniza volante y escoria para mejorar durabilidad.
        * **Edad:** El tiempo de curado (días).
        """)
        if st.button("Ir al Panel de Trabajo"):
            st.toast("Cargando herramientas de análisis...")
            
    with col2:
        # Imagen representativa del tema
        st.image("https://images.unsplash.com/photo-1517646281694-22d61d4422c6?auto=format&fit=crop&q=80&w=400", 
                 caption="Resistencia de Materiales")

# --- SECCIÓN 2: PANEL DE TRABAJO ---
elif menu == "📊 Panel de Análisis":
    st.header("📈 Análisis Exploratorio de Datos (EDA)")
    
    # Pestaña de documentación rápida
    with st.expander("❓ Ayuda y Documentación del Dataset"):
        st.write("""
        Cada columna representa kg por m³ de mezcla. El objetivo (Target) es la 
        `concrete_compression_strength` medida en Megapascales (MPa).
        """)

    # Gráfico 1: Correlación
    st.subheader("1. Mapa de Calor de Correlaciones")
    fig1, ax1 = plt.subplots(figsize=(10, 6))
    sns.heatmap(df.corr(), annot=True, cmap="YlGnBu", fmt=".2f", ax=ax1)
    st.pyplot(fig1)
    st.info("💡 **Interpretación:** Busca los valores más cercanos a 1 o -1. Por ejemplo, el cemento suele tener una correlación positiva alta con la resistencia.")

    # Gráfico 2: Relación Cemento vs Resistencia
    st.subheader("2. Relación Cemento vs Resistencia")
    col_a, col_b = st.columns([3, 1])
    
    with col_a:
        fig2 = sns.jointplot(data=df, x='cement', y='concrete_compression_strength', kind="reg", color="#4A90E2")
        st.pyplot(fig2)
        
    with col_b:
        st.markdown("### 📘 Nota Técnica")
        st.write("El cemento es el predictor principal. En este gráfico de dispersión con línea de regresión, observamos cómo aumenta la resistencia a medida que añadimos más cemento.")

    # Gráfico 3: Distribución por Edad
    st.subheader("3. Impacto del Tiempo de Curado")
    fig3, ax3 = plt.subplots(figsize=(10, 4))
    sns.boxplot(x='age', y='concrete_compression_strength', data=df, palette="viridis", ax=ax3)
    plt.xticks(rotation=45)
    st.pyplot(fig3)
    st.success("✅ **Hallazgo:** Se observa que a los 28 días la mayoría de las mezclas alcanzan su resistencia de diseño estándar.")

# --- SECCIÓN 3: SIMULADOR ---
elif menu == "🧮 Simulador":
    st.header("🔮 Predicción de Resistencia")
    st.write("Ingresa los valores de la mezcla para estimar el resultado final.")
    # (Aquí podrías añadir el código del modelo de regresión mostrado anteriormente)
    st.warning("Sección en desarrollo: Integrando modelo Scikit-Learn.")
