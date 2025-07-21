🚗 Car Price Predictor

This is a Machine Learning web application that predicts the price of a used car based on user input such as brand, year, fuel type, engine, and transmission. The app is built using Streamlit and deployed on Streamlit Cloud.

### 🔗 Live App
👉 [Click here to try it out!](https://celebalassignmentweek7appdeploycarmodel-ggv3gvfeb7vavkiq2il4st.streamlit.app)

---

## Features

- 💡Predict car prices instantly
- 🖥️Interactive user interface using Streamlit
- 📊Visual insights from the dataset
- 🎯Clean and minimal design

---

## 📁 Project Structure

 Car_Price_Predictor

├── app.py  # Streamlit app code

├── quikr_car.csv  # Raw dataset used for training

├── car_price_model.pkl  # Trained ML model

├── car_price_predictor.ipynb  # Notebook for EDA and model building

├── requirements.txt  # Python dependencies

└── README.md  # This file

## Tech Stack

- Python
- Pandas & NumPy
- Scikit-learn
- Matplotlib
- Streamlit

---

## How to Run Locally

1. **Clone the repository**

 git clone https://github.com/rrashikaa/Celebal_Assignment_Week_7_streamlit_deploy_car_model.git

 cd Celebal_Assignment_Week_7_streamlit_deploy_car_model

2. Create a virtual environment

python -m venv venv

source venv/bin/activate   # On Windows: venv\Scripts\activate

3. Install dependencies

pip install -r requirements.txt

4. Run the Streamlit app

streamlit run app.py


# Dataset
The dataset used in this project is scraped from Quikr and cleaned for model training.

Dataset link: https://www.kaggle.com/datasets/abhikalpsrivastava15/quikr-cars-dataset
