import pickle
import numpy as np
import streamlit as st

# Cargar el modelo
model_path = 'models/Price_model_flask.sav'
with open(model_path, 'rb') as file:
    modelo = pickle.load(file)

# Opciones disponibles
marcas = ['Toyota', 'Chevrolet', 'Ford', 'Honda', 'Nissan']
modelos = ['Altima', 'Camry', 'Silverado', 'F-150', 'Civic']
anos = list(range(2010, 2023))
estados = ['Excellent', 'Good', 'Fair']

# Interfaz de usuario con Streamlit
st.title("Predicción de Precios de Autos")

# Inputs del usuario
marca = st.selectbox("Marca", marcas)
modelo_auto = st.selectbox("Modelo", modelos)
ano = st.selectbox("Año", anos)
kilometraje = st.number_input("Kilometraje", min_value=10000, max_value=150000, step=5000)
estado = st.selectbox("Estado", estados)

# Botón de predicción
if st.button("Predecir Precio"):
    try:
        # Transformación de entrada
        entrada = np.array([[marca, modelo_auto, ano, kilometraje, estado]])
        precio_predicho = modelo.predict(entrada)[0]

        st.success(f"El precio estimado del auto es: ${precio_predicho:,.2f}")
    except Exception as e:
        st.error(f"Error en la predicción: {e}")
