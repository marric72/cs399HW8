# Heather Marriott
# HW9 - Find Outliers
# Repo - https://github.com/marric72/cs399HW8
#
# Why I selected the model:
# I selected a model for it's small size because I wanted to publish on 
# streamlit community.
# Model started as glove_short.txt file from Prof. but I removed duplicates
# ex. Cat and cat appeared
# so I removed Cat.  Removed non-word lines example: , and .
# to get under the GitHub file limits.  Sadly streamlist community still does notlike
# the GUI application version of the homework (see hw8.py in repo)  
#
#  Lines of Code: more than 20 (I would rather take point deduction than
#                               remove any code)
#
#to-do: 
#docstrings and comments
# less than 20 lines
# update streamlit app
# check pycharm for warnings
from wv import Model
from scipy.stats import zscore
#import numpy as np

def Sim_Check(model:Model, words : [str])->[str]:
    """ Given a list of words, remove outliers and return"""
    found_words = [model.find_word(word) for word in words]  #see if there are any words not in the model
    #get the index for any words that were not in the model so you can print a message 
    missing_indices = [i for i, word in enumerate(words) if found_words[i] is None] 

    if missing_indices: #print words so the user can be aware of what caused the program to exit
        missing_words = [words[i] for i in missing_indices]
        print(f"Words not found in model: {missing_words}")
        return None

    scores=[]
    
    #compare each word's similarity with the other words in the list to create a score
    for x in range(0, len(words)):
        scoreTotal=0
        for y in range(0, len(words)):
            if x == y:
                continue # do not compare word with itself
            word1 = model.find_word(words[x])
            word2 = model.find_word(words[y])
            print(f"word1={word1}")
            print(f"word2={word2}")
            scoreTotal += word1.similarity(word2) 
            print(f"scoreTotal={scoreTotal}")
        scores.append(scoreTotal)
    
    print(f"scores = {scores}")

    #normalize scores vector 
    #min_score = min(scores)
    #max_score = max(scores)
    #if min_score == max_score:
    #    max_score,min_score=1,0 #prevent division by 0 in next line ex.cat,cat,cat
    #normalized_scores = [(x - min_score) / (max_score - min_score) for x in scores]
    #print(f"normalized_score= {normalized_scores}")

    #the assignment asked for zscore, and it works with the line below.
    #but I wanted to use the normalized_scores instead becasue they 
    #were in the range of 1-0 which matched what we learned in class
    #where close to 1 means similar and close to 0 means different.
    #
    #zscore returned a wider range of numbers including negative numbers so
    #I decided not to use that. 
    scores = zscore(scores) #zscore will compute relative Z-score for input
    print(f"after zscore scores = {scores}")
    #if your list is all the same items, ex. apple, apple, apple then you
    #will get [nan nan nan] zscores and everything is removed from list
    if all(element == words[0] for element in words):
        print("all your words are the same.  No outliers")
    else:
        #closer to 1 is more similar vectors, closer to 0 is less similar
        threshold = .7 #trial and error for find a value that worked
        new_list = []
        for x in range(0, len(words)):
            if scores[x] > threshold:
                new_list.append(words[x])
        print(f'With outliers removed, your list looks like this: {new_list}')
        
    line = input('Enter at least 3 comma seperated words: (STOP to exit)')

def Load_Model()->Model:
    """Load the model data"""
    model = Model("models/glove_shorter.txt") 
    return model

def Get_User_Words(num  : int = 3) -> [str]:
    """Read in words from user.  If < num (3), re-prompt"""
    done = False
    while True:
        line=input(f'Enter at least {num} comma seperated words: (STOP to exit)')
        if line == 'STOP': 
            return None
        else:
            line=line.replace(" ","")  #remove spaces so it works with "cat,dog,robot" or "cat, dog, robot"
            words=line.split(',')
            if len(words) < num :
                print(f"Less than {num} words entered. Try again.")
            else:
                return words

if __name__ == "__main__":
    words = Get_User_Words(3)
    model = Load_Model()
    print(f"model={model} and words={words}")
    while model != None and words != None: 
        new_list = Sim_Check(model, words)
        words = Get_User_Words()
        
