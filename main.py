# Heather Marriott
# HW9 - Find Outliers
#
# Why I selected the model:
# I selected a model for it's small size because I wanted to publish on 
# streamlit community.
# Model started as glove_short.txt file from Prof. but I removed duplicates ex. Cat and cat appeared
# so I removed Cat.  Removed non-word lines example: , and .
# to get under the GitHub file limits so I did not need Large File Storage for streamlit app
#
#  Lines of Code: 41 - 6(blank lines) = 37 (I would rather take point deduction than remove any code)
#  Lines of Comments:
#to-do: 
#docstrings and comments
# less than 20 lines
# update streamlit app
#check pycharm for warnings
#remove numpy include
#to-do fix loader.py to add normalize function

from wv import Model
from scipy.stats import zscore
import numpy as np

model = Model("models/glove_shorter.txt") 
line=input('Enter at least 3 comma seperated words: (STOP to exit)')
while line != 'STOP': 
    line=line.replace(" ","")  #remove spaces so it works with "cat,dog,robot" or "cat, dog, robot"
    words=line.split(',')
    found_words = [model.find_word(word) for word in words]  #see if there are any words not in the model
    #get the index for any words that were not in the model so you can print a message 
    missing_indices = [i for i, word in enumerate(words) if found_words[i] is None] 

    if missing_indices: #print words so the user can be aware of what caused the program to exit
        missing_words = [words[i] for i in missing_indices]
        print(f"Words not found in model: {missing_words}")
        break
    
    if len(words) < 3: 
        print("Error: you did not enter 3 words with commas in between. Try again.")
        continue
        
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
    print('With outliers removed, your list looks like this:', ", ".join(words))   
    line = input('Enter at least 3 comma seperated words: (STOP to exit)')
