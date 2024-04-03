# Heather Marriott
# HW9 - Find Outliers
#
# Why I selected the model:
# I selected a model for it's small size because I wanted to publish on 
# streamlit community.
# Model started as Wikipedia model but I removed duplicates ex. Cat and cat appeared
# so I removed Cat.  Removed non-word lines example: , and .
# to get under the GitHub file limits so I did not need Large File Storage.
#
#to-do: smaller model file
#docstrings and comments
#stop at stop
# less than 20 lines
# update streamlit app
#check pycharm for warnings
from wv import Model
from scipy.stats import zscore
import numpy as np

model = Model("models/glove_shorter.txt") 
#model = Model("models/outfileWiki.txt")
line=input('Enter at least 3 comma seperated words: (STOP to exit)')
while line != 'STOP': 
    line=line.replace(" ","")
    words=line.split(',')
    found_words = [model.find_word(word) for word in words]
    missing_indices = [i for i, word in enumerate(words) if found_words[i] is None]

    if missing_indices:
        missing_words = [words[i] for i in missing_indices]
        print(f"Words not found in model: {missing_words}")
        break
    
    if len(words) < 3:
        print("Error: you did not enter 3 words with commas in between. Try again.g")
        continue

    scores=[]
    for x in range(0, len(words)):
        scoreTotal=0
        for y in range(0, len(words)):
            if x==y:
                continue
            #print(f"x={x} y={y}")
            word1 = model.find_word(words[x])
            word2 = model.find_word(words[y])
            
            print(f"word1={word1} word2={word2}")
            if word1 != None and word2 != None:
                #print(f"calling similarity for {words[x]} and {words[y]}")
                s=word1.similarity(word2)
                #print(f"calling similarity for {words[x]} and {words[y]} s={s}")
                scoreTotal=scoreTotal + s
        scores.append(scoreTotal)
    print(f"scores={scores}")
    scores=zscore(scores)
    print(f"zscores={scores}")
    
    
    #Todo: use z_score somehow  z_scores = zscore(scores)
    #print(f"z_scores={z_scores}")
    threshold = 1
    outliers_indices = np.where(np.abs(scores) >threshold)[0]
    wordCopy=words.copy()
    for o in outliers_indices:
        words.remove(wordCopy[o])  #remove outliers
    print('With outliers removed, your list looks like this:', ", ".join(words))   
    line=input('Enter at least 3 comma seperated words: (STOP to exit)') 
