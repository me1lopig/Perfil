import streamlit as st
import pandas as pd
import altair as alt
from io import BytesIO

st.set_page_config(page_title="Distancia vs Altura", layout="centered")

st.title("Gráfico de Distancia vs Altura")

st.write("Completa la tabla a continuación con los datos. Puedes agregar más filas.")

data = pd.DataFrame({
    'Tipo': [''],
    'Distancia': [None],
    'Altura': [None]
})

data_editable = st.data_editor(data, width='stretch', num_rows="dynamic")

if not data_editable.empty:
    df = data_editable.dropna(subset=['Distancia', 'Altura']).copy()
    try:
        df['Distancia'] = pd.to_numeric(df['Distancia'], errors='coerce')
        df['Altura'] = pd.to_numeric(df['Altura'], errors='coerce')
        df = df.dropna(subset=['Distancia', 'Altura'])
        df = df.sort_values(by='Distancia', ascending=True)
    except Exception:
        st.warning("Verifica que los campos Distancia y Altura sean numéricos")
        df = pd.DataFrame()    
    
    if not df.empty:
        # Botón de descarga en formato XLSX
        buffer = BytesIO()
        with pd.ExcelWriter(buffer, engine='openpyxl') as writer:
            df.to_excel(writer, index=False, sheet_name='Datos')
        buffer.seek(0)
        
        st.download_button(
            label="📥 Descargar datos en Excel (.xlsx)",
            data=buffer,
            file_name="distancia_altura.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
        
        # Calcular el rango común para ambos ejes
        min_val = min(df['Distancia'].min(), df['Altura'].min())
        max_val = max(df['Distancia'].max(), df['Altura'].max())
        
        # Agregar un pequeño margen (5%)
        rango = max_val - min_val
        margen = rango * 0.05
        min_val = min_val - margen
        max_val = max_val + margen
        
        chart = alt.Chart(df).mark_line(point=True, size=3).encode(
            x=alt.X('Distancia:Q', 
                    title='Distancia', 
                    scale=alt.Scale(domain=[min_val, max_val])),
            y=alt.Y('Altura:Q', 
                    title='Altura', 
                    scale=alt.Scale(domain=[min_val, max_val])),
            tooltip=['Tipo', 'Distancia', 'Altura']
        ).properties(
            width=600,
            height=600,
            title="Relación entre Distancia y Altura (Escalas 1:1)"
        ).configure_legend(
            disable=True
        )
        
        # NO usar use_container_width para mantener proporción exacta
        st.altair_chart(chart, use_container_width=False)
    else:
        st.warning("Agrega valores numéricos en Distancia y Altura para visualizar el gráfico.")
else:
    st.warning("Agrega valores en Distancia y Altura para visualizar el gráfico.")
