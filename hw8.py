import streamlit as st
import pandas as pd
import numpy as np
from requests import get


st.set_page_config(
    page_title="AI Test",
    page_icon="💰",
)



#Write text to the screen with HTML markup
title = '<p style="font-family:Courier; color:Blue; font-size: 30px;">CS399 AI Example - Find Outliers</p>'
st.markdown(title, unsafe_allow_html=True)
#st.image("panda.png", caption='Similarity Checking Panda Running on AI')
title = '<p style="font-family:Courier; color:White; font-size: 20px;">Based on Pre-trained vectors using Wikipedia 2017 </p>'
st.markdown(title, unsafe_allow_html=True)

st.write("This can take awhile, so please enjoy the zen garden while you wait.")

# Display the filtered DataFrame
st.title("Outlier Removal")
st.write("Enter at least 3 comma-seperated words")
st.write("panda, cat, dog, car")
st.title("Outliers Removed")
st.write("Enter at least 3 comma-seperated words")
st.write("panda, cat, dog")
