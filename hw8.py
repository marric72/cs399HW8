import streamlit as st
import pandas as pd
import numpy as np
from requests import get


st.set_page_config(
    page_title="Currency Convert",
    page_icon="💰️",
)



#Write text to the screen with HTML markup
title = '<p style="font-family:Courier; color:Blue; font-size: 30px;">CS399 AI Example - Find Outliers</p>'
st.markdown(title, unsafe_allow_html=True)
st.image("money.png", caption='Save your Money')
title = '<p style="font-family:Courier; color:White; font-size: 20px;">Exchange Rates </p>'
st.markdown(title, unsafe_allow_html=True)

st.write("Pulling data from: https://api.exchangerate-api.com/v4/latest/USD")
url = 'https://api.exchangerate-api.com/v4/latest/USD'
result=get(url, timeout=3).json()

# Convert rates data to DataFrame
df = pd.DataFrame(result.get("rates"), index=["Rates"])

# Display multi-select for choosing columns
selected_columns = st.multiselect(
    'Select columns to display:',
    list(df.columns),
    default=['USD', 'EUR', 'GBP']  # Default columns to display
)

# Filter DataFrame based on selected columns
filtered_df = df[selected_columns]

# Display the filtered DataFrame
st.title("All the Data")
st.write(filtered_df)

