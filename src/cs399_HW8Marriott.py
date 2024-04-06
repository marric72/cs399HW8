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
# to get under the GitHub file limits.  Sadly streamlist community still does not like
# the GUI application version of the homework (see hw8.py in repo)  
#
#  Lines of Code: more than 20 (I would rather take point deduction than
#                               remove any code)
#
#  To use pytest I found I had to update PYTHONPATH: export PYTHONPATH=..../src
#  then run tests as python3.12 -m pytest       (when I ran just pytest I got ModuleNotFoundError scipy)
#
#to-do: 
#docstrings and comments
# less than 20 lines
# update streamlit app
# check pycharm for warnings
#comment out or remove extra print statement
from wv import Model
from scipy.stats import zscore
import numpy as np

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
            #print(f"word1={word1}")
            #print(f"word2={word2}")
            scoreTotal += word1.similarity(word2) 
            #print(f"scoreTotal={scoreTotal}")
        scores.append(scoreTotal)
    
    #print(f"scores = {scores}")

    #normalize scores vector 
    data_array = np.array(scores)

    # Calculate the minimum and maximum values in the array
    min_value = np.min(data_array)
    max_value = np.max(data_array)

    # Normalize the array between 0 and 1 using min-max scaling
    print(min_value, max_value)
    if (min_value != max_value): #no division by 0
        normalized_data = (data_array - min_value) / (max_value - min_value)
    else:
        normalized_data = (data_array - min_value) 
    print(normalized_data)
    
    #the assignment asked for zscore, I tried below line:
    #scores = zscore(scores) #zscore will compute relative Z-score for input
    #print(f"after zscore scores = {scores}")
    #
    #but the results were not between 0-1 like the lecture showed 
    #zscore returned a wider range of numbers including negative numbers so
    #I decided not to use that. 
    
    scores=normalized_data
   
    #if your list is all the same items, ex. apple, apple, apple then you
    #will get [nan nan nan] zscores and everything is removed from list
    if all(element == words[0] for element in words):
        print("all your words are the same.  No outliers")
        return words
    else:
        #closer to 1 is more similar vectors, closer to 0 is less similar
        threshold = .3 #trial and error for find a value that worked
        new_list = []
        for x in range(0, len(words)):
            if scores[x] > threshold:
                new_list.append(words[x])
        print(f'With outliers removed, your list looks like this: {new_list}')
        return new_list
    
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
    if words != None:
        model = Load_Model()
        print(f"model={model} and words={words}")
        while model != None and words != None: 
            new_list = Sim_Check(model, words)
            if new_list == None: #word not found in model, exit
                break
            words = Get_User_Words()
        
