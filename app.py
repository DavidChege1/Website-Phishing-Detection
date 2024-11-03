import streamlit as st
import pandas as pd
import numpy as np
import pickle
import plotly.express as px

# Set page configuration
st.set_page_config(page_title="Phishing Website Classifier", layout="wide")

# Title and description
st.title("Phishing Website Classifier")
st.write("This app uses machine learning to classify websites as legitimate or phishing based on various features.")

# Load the saved model and scaler
@st.cache_resource
def load_model():
    try:
        with open('phishing_model.pkl', 'rb') as file:
            model = pickle.load(file)
        with open('scaler.pkl', 'rb') as file:
            scaler = pickle.load(file)
        with open('feature_names.pkl', 'rb') as file:
            feature_names = pickle.load(file)
        return model, scaler, feature_names
    except FileNotFoundError:
        st.error("Model files not found. Please ensure you've run the training script first.")
        st.stop()

model, scaler, feature_names = load_model()

# Sidebar for user input
st.sidebar.header("Website Features")

user_input = {}
user_input['HasTitle'] = st.sidebar.selectbox('HasTitle', [0, 1], format_func=lambda x: 'Yes' if x == 1 else 'No')
user_input['HasFavicon'] = st.sidebar.selectbox('HasFavicon', [0, 1], format_func=lambda x: 'Yes' if x == 1 else 'No')
user_input['IsResponsive'] = st.sidebar.selectbox('IsResponsive', [0, 1], format_func=lambda x: 'Yes' if x == 1 else 'No')
user_input['NoOfURLRedirect'] = st.sidebar.selectbox('NoOfURLRedirect', [0, 1], format_func=lambda x: 'Yes' if x == 1 else 'No')
user_input['NoOfSelfRedirect'] = st.sidebar.selectbox('NoOfSelfRedirect', [0, 1], format_func=lambda x: 'Yes' if x == 1 else 'No')
user_input['HasExternalFormSubmit'] = st.sidebar.selectbox('HasExternalFormSubmit', [0, 1], format_func=lambda x: 'Yes' if x == 1 else 'No')
user_input['HasSocialNet'] = st.sidebar.selectbox('HasSocialNet', [0, 1], format_func=lambda x: 'Valid' if x == 1 else 'Invalid')
user_input['HasHiddenFields'] = st.sidebar.selectbox('HasHiddenFields', [0, 1], format_func=lambda x: 'Present' if x == 1 else 'Absent')
user_input['Bank'] = st.sidebar.selectbox('Bank', [0, 1], format_func=lambda x: 'Yes' if x == 1 else 'No')
user_input['Pay'] = st.sidebar.selectbox('Pay', [0, 1], format_func=lambda x: 'Present' if x == 1 else 'Absent')
user_input['Crypto'] = st.sidebar.selectbox('Crypto', [0, 1], format_func=lambda x: 'Present' if x == 1 else 'Absent')
user_input['HasCopyrightInfo'] = st.sidebar.selectbox('HasCopyrightInfo', [0, 1], format_func=lambda x: 'Present' if x == 1 else 'Absent')

# Make prediction
if st.sidebar.button('Classify Website'):
    # Convert user input to DataFrame
    input_df = pd.DataFrame([user_input])
    
    # Ensure columns are in the correct order
    input_df = input_df[feature_names]
    
    # Scale the input
    input_scaled = scaler.transform(input_df)
    
    # Make prediction
    prediction = model.predict(input_scaled)
    probability = model.predict_proba(input_scaled)
    
    # Display result
    st.header('Classification Result')
    if prediction[0] == 1:
        st.error('⚠️ This website is likely a PHISHING website!')
    else:
        st.success('✅ This website appears to be LEGITIMATE.')
    
    # Display probability
    st.write(f'Confidence: {probability[0][prediction[0]]:.2%}')
    
    # Create probability chart
    prob_df = pd.DataFrame({
        'Category': ['Legitimate', 'Phishing'],
        'Probability': probability[0]
    })
    fig = px.bar(prob_df, x='Category', y='Probability',
                 color='Category',
                 color_discrete_map={'Legitimate': 'green', 'Phishing': 'red'})
    st.plotly_chart(fig)

# Display feature importance
st.header('Feature Importance')
importance_df = pd.DataFrame({
    'Feature': feature_names,
    'Importance': abs(model.coef_[0])
}).sort_values('Importance', ascending=False)
fig = px.bar(importance_df, x='Feature', y='Importance')
st.plotly_chart(fig)

# Add explanations
st.header('How it Works')
st.write("""
This classifier uses a pre-trained logistic regression model to determine if a website is legitimate or potentially dangerous (phishing).
It analyzes various features of the website and makes predictions based on patterns learned from training data.
""")

# Add disclaimer
st.warning("""
Disclaimer: This is a demonstration model and should not be used as the sole method for determining website legitimacy.
Always use multiple security measures and exercise caution when visiting unknown websites.
""")