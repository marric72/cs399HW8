# Heather Marriott
# HW9 - Find Outliers
from wv import Model
from scipy.stats import zscore
import numpy as np   #TODO: look for a way to remove this

model = Model("models/glove_short.txt") #model selected because it is smallest file and worked
while True: 
    line=input('Enter at least 3 comma seperated words: ')
    line=line.replace(" ","")
    words=line.split(',')
    print(f"words={words}")
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
            if word1 == None :
                print(f"Word not found in model: ***{words[x]}***")
                import sys
                sys.exit(1) #exit program, a break would only exit for loop
            if word2 == None:
                print(f"Word not found in model: ***{words[y]}***")
                import sys
                sys.exit(1) #exit program, a break would only exit for loop
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
