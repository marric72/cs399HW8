import streamlit as st
import numpy as np
from wv import Model
from scipy.stats import zscore


st.set_page_config(
    page_title="AI Test",
    page_icon="🌹",
)

#Write text to the screen with HTML markup
title = '<p style="font-family:Courier; color:Blue; font-size: 30px;">CS399 AI Example - Find Outliers</p>'
st.markdown(title, unsafe_allow_html=True)
st.image("yellowRose.png", caption='Relax')
title = '<p style="font-family:Courier; color:White; font-size: 20px;">Based on Pre-trained vectors a shorter version glove_short.txt </p>'
st.markdown(title, unsafe_allow_html=True)
# Create a text input widget
user_input = st.text_input('Enter a comma seperated list of 3 or more words:')

user_input=user_input.replace(" ","") 
user_input=user_input.lower()
words=user_input.split(',')
if len(words) < 3:
    st.write("Waiting 3 words with commas in between")
else:
    scores_set = 0
    # Display the input value
    st.write('You entered:', user_input)
    model = Model("models/glove_shorter.txt") 
    found_words = [model.find_word(word) for word in words]  #see if there are any words not in the model
    #get the index for any words that were not in the model so you can print a message 
    missing_indices = [i for i, word in enumerate(words) if found_words[i] is None] 

    if missing_indices: #print words so the user can be aware of what caused the program to exit
        missing_words = [words[i] for i in missing_indices]
        print(f"Words not found in model: {missing_words}")
        st.write(f"Words not found in model: {missing_words}")
        
    elif len(words) < 3: 
        print("Error: you did not enter 3 words with commas in between. Try again.")
        st.write(f"Error: you did not enter 3 words with commas in between. Try again.")
    else:    
        st.write("This can take awhile, be patient.")
        scores=[]
        #compare each word's similarity with the other words in the list to create a score
        for x in range(0, len(words)):
            scoreTotal=0
            for y in range(0, len(words)):
                if x == y:
                    continue # do not compare word with itself
                word1 = model.find_word(words[x])
                word2 = model.find_word(words[y])
                    
                scoreTotal += word1.similarity(word2)
            scores.append(scoreTotal)
            scores = zscore(scores) #zscore will compute relative Z-score for input
            
        threshold = 1 #trial and error for find a value that worked
        outliers_indices = np.where(np.abs(scores) >threshold)[0]
        wordCopy = words.copy() 
        for o in outliers_indices:
            words.remove(wordCopy[o])  #remove outliers
        scores_set = 1
        if scores_set == 1:
            print('With outliers removed, your list looks like this:', ", ".join(words))   
            st.write('With outliers removed, your list looks like this:', ", ".join(words))
            st.image("redRose.png", caption='Breath') 
