import streamlit as st
import pickle
import numpy as np

# Load the trained model
model = pickle.load(open("model.pkl", "rb"))

st.title("🚗 Car Price Prediction App")
st.write("Enter the details of the car to predict its selling price.")

# Input fields
year = st.number_input("Year of Purchase", min_value=2000, max_value=2025, step=1)
present_price = st.number_input("Present Price (in lakhs)", min_value=0.0, format="%.2f")
kms_driven = st.number_input("Kms Driven", min_value=0, step=500)

fuel_type = st.selectbox("Fuel Type", ["Petrol", "Diesel", "CNG"])
seller_type = st.selectbox("Seller Type", ["Dealer", "Individual"])
transmission = st.selectbox("Transmission", ["Manual", "Automatic"])
owner = st.number_input("Number of Previous Owners", min_value=0, max_value=3, step=1)

# Convert categorical inputs to numerical (same encoding as training)
fuel_map = {"Petrol": 2, "Diesel": 0, "CNG": 1}
seller_map = {"Dealer": 0, "Individual": 1}
trans_map = {"Manual": 1, "Automatic": 0}

fuel_encoded = fuel_map[fuel_type]
seller_encoded = seller_map[seller_type]
trans_encoded = trans_map[transmission]

# Prepare input
input_data = np.array([[year, present_price, kms_driven, fuel_encoded,
                        seller_encoded, trans_encoded, owner]])

# Predict button
if st.button("Predict Price"):
    prediction = model.predict(input_data)[0]
    st.success(f"Estimated Selling Price: ₹ {prediction:.2f} Lakhs")
