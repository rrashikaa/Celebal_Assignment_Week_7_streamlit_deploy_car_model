import pandas as pd
import pickle
import streamlit as st
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

st.set_page_config(page_title="Car Price Predictor", layout="centered")

car_img = Image.open("car_image.jpg")
st.image(car_img, use_container_width=True)

car_data = pd.read_csv(r"Cleaned Car.csv")

model = pickle.load(open(r"LinearRegressionModel.pkl", "rb"))

st.title("🚗 Used Car Price Predictor")

st.sidebar.header("Enter Car Details:")

companies = sorted(car_data['company'].unique())
selected_company = st.sidebar.selectbox("Select Company", companies)

car_models = sorted(car_data[car_data['company'] == selected_company]['name'].unique())
selected_model = st.sidebar.selectbox("Select Car Model", car_models)

years = sorted(car_data['year'].unique(), reverse=True)
selected_year = st.sidebar.selectbox("Select Year of Purchase", years)

fuel_types = sorted(car_data['fuel_type'].unique())
selected_fuel = st.sidebar.selectbox("Select Fuel Type", fuel_types)

driven = st.sidebar.number_input("Enter Kilometers Driven", min_value=0, step=1000)

if st.sidebar.button("Predict Price"):
    input_df = pd.DataFrame([[selected_model, selected_company, selected_year, driven, selected_fuel]],
                            columns=['name', 'company', 'year', 'kms_driven', 'fuel_type'])
    
    prediction = model.predict(input_df)[0]
    st.success(f"💰 Estimated Resale Price: ₹ {int(prediction):,}")

st.subheader(" Visual Insights")

if st.checkbox("Show Average Price by Year"):
    avg_price_by_year = car_data.groupby('year')['Price'].mean().sort_index()
    st.line_chart(avg_price_by_year)

if st.checkbox("Show Price vs KMs Driven for selected model"):
    model_data = car_data[car_data['name'] == selected_model]
    if not model_data.empty:
        model_data_sorted = model_data.sort_values('kms_driven')
        st.line_chart(model_data_sorted[['kms_driven', 'Price']].set_index('kms_driven'))
    else:
        st.info("No data available for this model to display the chart.")


st.markdown("---")
st.markdown("Created by **Rashika Goyal**")