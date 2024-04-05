import streamlit as st
from scipy.stats import zscore

# Get user input
user_input = st.text_input('Enter comma-separated numbers')

# Convert user input to list of numbers
numbers = [float(num.strip()) for num in user_input.split(',') if num.strip()]

# Calculate z-scores
z_scores = zscore(numbers)

# Display z-scores
st.write('Z-scores:', z_scores)

