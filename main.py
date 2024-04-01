# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


from wv import Model
from scipy.stats import zscore
import numpy as np

def a_to_b_is_like_c_to(a: str, b: str, c: str)-> str:
    # Use a breakpoint in the code line below to debug your script.
    print(f'Checking: {a} {b} {c}')  # Press ⌘F8 to toggle the breakpoint.
    a = model.find_word(a)
    b = model.find_word(b)
    c = model.find_word(c)
    d = b - a + c
    print(f"d={d} d.text={d.text} a.text={a.text} b.text={b.text}")
    d.normalize()
    print(f"d={d}")

    for w in model.find_similar_words(d, 10):
        print(f"w={w}")
        if w.text not in (a.text, b.text, c.text):
            print(f"w.text={w.text}")
            return f"{a.text} to {b.text} is like {c.text} to {w.text}"

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    model = Model("models/glove_short.txt")
    #model = Model("models/outfileWiki.txt") 
    print(a_to_b_is_like_c_to("Berlin", "Germany", "Paris"))
    # See PyCharm help at https://www.jetbrains.com/help/pycharm/
    while (1):
        line=input('Enter at least 4 words: ')
        words=line.split(' ')
        if len(words) < 4:
            print("Error: you did not enter 4 words with spaces in between.")
        else:
            scores=[]
            for word in words:
                W = model.find_word(word)
                if W == None:
                    print(f"Word not found in model: {word}")
                    import sys
                    sys.exit(1)
                score=W.norm()
                scores.append(score)
                print(f"For word: {W.text} score is {score}")


            z_scores =zscore(scores)
            print("z_scores=", z_scores)
            threshold = 2

            outliers_indices = np.where(np.abs(z_scores) > threshold)[0]

            # Print the indices of outliers
            print("Indices of outliers:", outliers_indices)
            print(type(outliers_indices))
            # Print the values of outliers
            for o in outliers_indices:
                print("Values of outliers:", words[o])

            