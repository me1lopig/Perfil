import streamlit as st
import pandas as pd
import altair as alt
from io import BytesIO

st.set_page_config(page_title="Perfil Topográfico", layout="centered")

st.title("📊 Generador de Perfiles Topográficos")

st.write("Introduce los puntos del perfil. La distancia es acumulativa.")

# Datos iniciales con ejemplo
data = pd.DataFrame({
    'Punto': [''],
    'Distancia (m)': [None],
    'Altura (m)': [None]
})

data_editable = st.data_editor(data, width='stretch', num_rows="dynamic")

if not data_editable.empty:
    df = data_editable.dropna(subset=['Distancia (m)', 'Altura (m)']).copy()
    try:
        df['Distancia (m)'] = pd.to_numeric(df['Distancia (m)'], errors='coerce')
        df['Altura (m)'] = pd.to_numeric(df['Altura (m)'], errors='coerce')
        df = df.dropna(subset=['Distancia (m)', 'Altura (m)'])
        df = df.sort_values(by='Distancia (m)', ascending=True)
    except Exception:
        st.warning("⚠️ Verifica que Distancia y Altura sean valores numéricos")
        df = pd.DataFrame()    
    
    if not df.empty:
        # Botón de descarga en formato XLSX
        buffer = BytesIO()
        with pd.ExcelWriter(buffer, engine='openpyxl') as writer:
            df.to_excel(writer, index=False, sheet_name='Perfil')
        buffer.seek(0)
        
        st.download_button(
            label="📥 Descargar perfil(.xlsx)",
            data=buffer,
            file_name="perfil_topografico.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
        
        # Calcular el rango combinado para escala 1:1 (permitiendo valores negativos)
        max_distancia = df['Distancia (m)'].max()
        min_distancia = df['Distancia (m)'].min()
        max_altura = df['Altura (m)'].max()
        min_altura = df['Altura (m)'].min()
        
        rango_distancia = max_distancia - min_distancia
        rango_altura = max_altura - min_altura
        rango_max = max(rango_distancia, rango_altura)
        
        margen = rango_max * 0.1
        
        centro_distancia = (max_distancia + min_distancia) / 2
        centro_altura = (max_altura + min_altura) / 2
        
        domain_distancia = [centro_distancia - (rango_max + margen) / 2, 
                           centro_distancia + (rango_max + margen) / 2]
        domain_altura = [centro_altura - (rango_max + margen) / 2, 
                        centro_altura + (rango_max + margen) / 2]
        
        chart_size = 600
        
        # Gráfico del perfil topográfico
        chart = alt.Chart(df).mark_line(point=True, size=3, color='#2E7D32').encode(
            x=alt.X('Distancia (m):Q', title='Distancia Horizontal (m)', 
                    scale=alt.Scale(domain=domain_distancia)),
            y=alt.Y('Altura (m):Q', title='Elevación (m)', 
                    scale=alt.Scale(domain=domain_altura)),
            tooltip=['Punto', 'Distancia (m)', 'Altura (m)']
        ).properties(
            width=chart_size,
            height=chart_size,
            title="Perfil Topográfico (Escala 1:1)"
        ).configure_legend(
            disable=True
        )
        
        st.altair_chart(chart, use_container_width=False)
        
        st.info("ℹ️ Escala 1:1 - Las distancias horizontales y verticales son proporcionales")
        
    else:
        st.warning("⚠️ Agrega valores numéricos en Distancia y Altura para visualizar el perfil.")
else:
    st.warning("⚠️ Agrega puntos del perfil para comenzar.")
