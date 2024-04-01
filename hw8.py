import streamlit as st
import numpy as np
from wv import Model
from scipy.stats import zscore
import numpy as np

st.set_page_config(
    page_title="AI Test",
    page_icon="🌹",
)

#Write text to the screen with HTML markup
title = '<p style="font-family:Courier; color:Blue; font-size: 30px;">CS399 AI Example - Find Outliers</p>'
st.markdown(title, unsafe_allow_html=True)
st.image("yellowRose.png", caption='Relax')
title = '<p style="font-family:Courier; color:White; font-size: 20px;">Based on Pre-trained vectors using Wikipedia 2017 </p>'
st.markdown(title, unsafe_allow_html=True)
# Create a text input widget
user_input = st.text_input('Enter a comma seperated list of 4 or more words:')


words=user_input.split(',')
scores_set=0
if len(words) < 4:
    st.write("Error: you did not enter 4 words with spaces in between.")
else:
    # Display the input value
    st.write('You entered:', user_input)
    model = Model("models/glove_short.txt")
    scores=[]
    for word in words:
        #st.write(f"Word: {word}")
        W = model.find_word(word)
        if W == None:
            st.write(f"Word not found in model: {word}")
            print(f"Word not found in model: {word}")
        else:    
            score=W.norm()
            scores.append(score)
            #st.write(f"Score: {score}")
            print(f"For word: {W.text} score is {score}")
    scores_set=1
    if (scores_set == 1):
        z_scores =zscore(scores)
        print("z_scores=", z_scores)
        threshold = 1

        outliers_indices = np.where(np.abs(z_scores) > threshold)[0]

        # Print the indices of outliers
        print("Indices of outliers:", outliers_indices)
                
        # Print the values of outliers
        for o in outliers_indices:
            st.write("Values of outliers:", words[o])

            

#st.write("This can take awhile, so please enjoy the zen garden while you wait.")
st.image("redRose.png", caption='Breath') 
# Display the filtered DataFrame
