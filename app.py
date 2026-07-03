import streamlit as st
import joblib
import numpy as np

# Load the trained model
import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load("model/house_price_model.pkl")

st.title("🏠 House Price Prediction")

st.write("Enter the house details below:")

crim = st.number_input("Crime Rate", value=0.1)
zn = st.number_input("Residential Land Zone", value=0.0)
indus = st.number_input("Industry Area", value=5.0)
chas = st.number_input("Charles River (0 or 1)", value=0)
nox = st.number_input("Nitric Oxide", value=0.5)
rm = st.number_input("Average Rooms", value=6.0)
age = st.number_input("Age", value=50.0)
dis = st.number_input("Distance to Employment", value=4.0)
rad = st.number_input("Highway Access", value=5)
tax = st.number_input("Tax Rate", value=300)
ptratio = st.number_input("Pupil Teacher Ratio", value=15.0)
b = st.number_input("B", value=390.0)
lstat = st.number_input("Lower Status Population", value=10.0)

if st.button("Predict Price"):
    features = np.array([[crim, zn, indus, chas, nox,
                          rm, age, dis, rad, tax,
                          ptratio, b, lstat]])

    prediction = model.predict(features)

    st.success(f"Predicted House Price: ${prediction[0]:.2f}K")