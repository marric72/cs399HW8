# Heather Marriott
# HW9 - Find Outliers
from wv import Model
from scipy.stats import zscore
import numpy as np   #TODO: look for a way to remove this

model = Model("models/glove_short.txt") #model selected because it is smallest file and worked
while True: 
    line=input('Enter at least 3 comma seperated words: ')
    words=line.split(',')
    scores=[]
    if len(words) < 3:
        print("Error: you did not enter 3 words with commas in between.")
        continue
    for word in words:
        W = model.find_word(word)
        if W == None:
            print(f"Word not found in model: {word}")
            import sys
            sys.exit(1) #exit program, a break would only exit for loop
        scores.append(W.norm()) #TODO: how can I use similarity ???
    z_scores = zscore(scores)
    threshold = 1
    outliers_indices = np.where(np.abs(z_scores) > threshold)[0]
    wordCopy=words.copy()
    for o in outliers_indices:
        words.remove(wordCopy[o])  #remove outliers
    print('With outliers removed, your list looks like this:', ", ".join(words))    
