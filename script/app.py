# trending_app.py

import streamlit as st
import pandas as pd
import joblib

# Load model and encoders
model = joblib.load('C:\\Users\\Dhusyath\\Downloads\\PROJECTS_DA\\PROJECTS_DA\\you tube analysis\\trending_model.pkl')
channel_encoder = joblib.load('C:\\Users\\Dhusyath\\Downloads\\PROJECTS_DA\\PROJECTS_DA\\you tube analysis\\channel_encoder.pkl')
country_encoder = joblib.load('C:\\Users\\Dhusyath\\Downloads\\PROJECTS_DA\\PROJECTS_DA\\you tube analysis\\country_encoder.pkl')
feature_names = joblib.load('C:\\Users\\Dhusyath\\Downloads\\PROJECTS_DA\\PROJECTS_DA\\you tube analysis\\trending_features.pkl')

st.title("📈 YouTube Trending Status Predictor")

# Input form
channel_options = channel_encoder.classes_.tolist()
selected_channel = st.selectbox("Select Channel", channel_options)
encoded_channel = channel_encoder.transform([selected_channel])[0]

category_id = st.number_input("Enter Category ID", min_value=1, max_value=50)

country_options = country_encoder.classes_.tolist()
selected_country = st.selectbox("Select Publish Country", country_options)
encoded_country = country_encoder.transform([selected_country])[0]

# Predict button
if st.button("Predict Trending Status"):
    input_df = pd.DataFrame([{
        "channel_encoded": encoded_channel,
        "category_id": category_id,
        "country_encoded": encoded_country
    }])[feature_names]

    prediction = model.predict(input_df)[0]
    st.success(f"🔥 Prediction: {'Likely to Trend' if prediction == 1 else 'Unlikely to Trend'}")
