import pickle
import pandas as pd
import streamlit as st

# Load the trained pipeline
with open("../models/full_pipeline.pkl", "rb") as file:
    pipeline = pickle.load(file)

# Streamlit UI
st.title("Price My Car")
st.subheader("Car Price Prediction 🚗💰")
st.markdown("Enter the car details below to get an estimated price.")

# Define make-model mapping
MODEL_MAPPING = {
    "Chevrolet": ["Silverado"],
    "Toyota": ["Camry"],
    "Nissan": ["Altima"],
    "Honda": ["Civic"],
    "Ford": ["F-150"]
}

# User Input Fields
make = st.selectbox(
    "Car Brand",
    options=["Chevrolet", "Toyota", "Nissan", "Honda", "Ford"]
)

model_name = st.selectbox(
    "Car Model",
    options=MODEL_MAPPING[make]
)

year = st.number_input(
    "Year",
    min_value=2010,
    max_value=2020,
    value=2015
)

mileage = st.number_input(
    "Mileage",
    min_value=10100,
    max_value=150000,
    value=50000
)

condition = st.selectbox(
    "Car Condition",
    options=["New", "Used", "Certified"]
)

# Predict Button
if st.button("Predict Price"):
    try:
        # Create DataFrame for the model
        input_df = pd.DataFrame([[make, model_name, year, mileage, condition]], 
                              columns=["Make", "Model", "Year", "Mileage", "Condition"])
        
        # Make Prediction
        prediction = pipeline.predict(input_df)[0]
        
        # Display Result
        st.success(f"Estimated Price: ${prediction:,.2f}")
    
    except Exception as e:
        st.error(f"Error: {e}")