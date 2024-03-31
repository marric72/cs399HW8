# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


from wv import Model

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
    #model = Model("models/short_model.txt")
    model = Model("models/wiki-news-300d-1M.vec")
    print(a_to_b_is_like_c_to("Berlin", "Germany", "Paris"))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
