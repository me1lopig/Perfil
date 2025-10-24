# Resumen del Programa: Distancia vs Altura

## ¿Qué hace?

Es una aplicación web interactiva que permite:

1. Ingresar datos de Tipo, Distancia y Altura en una tabla
2. Visualizar la relación entre Distancia y Altura en un gráfico
3. Descargar los datos en formato Excel (.xlsx)

---

## Cómo funciona

### PASO 1: Entrada de datos
- Muestra una tabla editable con 3 columnas
- Puedes agregar o eliminar filas dinámicamente
- Columnas: **Tipo** (texto), **Distancia** (número), **Altura** (número)

### PASO 2: Procesamiento automático
- Elimina filas vacías o con datos incompletos
- Convierte Distancia y Altura a números
- Ordena los datos por Distancia (de menor a mayor)
- Valida que los datos sean numéricos

### PASO 3: Visualización
- Genera un gráfico de línea con puntos marcados
- Eje X: Distancia (escala automática)
- Eje Y: Altura
- Al pasar el mouse muestra: Tipo, Distancia y Altura

### PASO 4: Descarga
- Botón para descargar los datos en Excel
- Archivo: `distancia_altura.xlsx`
- Solo aparece cuando hay datos válidos

---

## Casos de uso

Este programa es útil para:

- Análisis topográfico (distancia horizontal vs elevación)
- Estudios de trayectorias (alcance vs altura)
- Perfiles de terreno
- Datos de experimentos físicos
- Cualquier relación entre dos variables numéricas

---

## Ejemplo práctico

Imagina que mides la altura de una montaña en diferentes puntos:

| Tipo        | Distancia (m) | Altura (m) |
|-------------|----------------|------------|
| Base        | 0              | 100        |
| Punto medio | 5              | 450        |
| Cumbre      | 10             | 800        |

El programa:
1. Ordena automáticamente por distancia
2. Dibuja el perfil de la montaña
3. Te permite descargar los datos para análisis posterior

---

## Tecnologías usadas

- **Streamlit**: Interfaz web interactiva
- **Pandas**: Procesamiento de datos
- **Altair**: Gráficos interactivos
- **OpenPyXL**: Exportación a Excel

---

## Instalación

```bash
pip install streamlit pandas altair openpyxl
```

## Ejecución

```bash
streamlit run app.py
```

La aplicación se abrirá en tu navegador en `http://localhost:8501`

---

## Características principales

✅ Interfaz intuitiva y fácil de usar  
✅ Validación robusta de datos numéricos  
✅ Manejo de errores con try/except  
✅ Ordenamiento automático de datos  
✅ Gráfico interactivo con tooltips  
✅ Escalado inteligente del eje X  
✅ Filas dinámicas para flexibilidad  
✅ Exportación a Excel (.xlsx)  

---

**Creado con ❤️ usando Streamlit**
