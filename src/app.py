import pickle
import pandas as pd
import streamlit as st

# Load the trained pipeline
with open("../models/full_pipeline.pkl", "rb") as file:
    pipeline = pickle.load(file)

# Streamlit UI
st.title("Car Price Prediction 🚗💰")

st.markdown("Enter the car details below to get an estimated price.")

# User Input Fields
make = st.text_input("Car Make", "Toyota")
model_name = st.text_input("Car Model", "Corolla")
year = st.number_input("Year", min_value=1980, max_value=2025, value=2015)
mileage = st.number_input("Mileage", min_value=0, value=50000)
condition = st.selectbox("Car Condition", ["New", "Used", "Certified"])

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
