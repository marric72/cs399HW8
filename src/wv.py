"""
    Word and Model classes for word vectors.
    Loads the model into memory, but does not normalize the vectors.
    Loading even a model with just 100_000 words takes about 5 seconds.
    Author: Wolf Paulus, https://wolfpaulus.com
"""
#from typing import Self  #?????????????? can't import Self from typing unless python 3.11 or later
from math import sqrt
from time import process_time


class Word:
    """ Represents a word and its vector"""
    def __init__(self, text: str, vector: list[float]) -> None:
        self.text = text
        self.vector = vector

    def __repr__(self) -> str:
        vector_preview = ', '.join(map(str, self.vector[:2]))
        return f"{self.text} [{vector_preview}, ...]"

    def norm(self) -> float:
        return sqrt(sum([x * x for x in self.vector]))

    def normalize(self) -> None:
        length = self.norm()
        self.vector = [x / length for x in self.vector]

    def similarity(self, w) -> float:
        sim=self*w #for debugging move to variable to examin/print
        return sim

    def __add__(self, w):
        return Word("", [x + y for x, y in zip(self.vector, w.vector)])

    def __sub__(self, w):
        return Word("", [x - y for x, y in zip(self.vector, w.vector)])

    def __mul__(self, w) -> float:
        return sum([x * y for x, y in zip(self.vector, w.vector)])


class Model(list):
    """ Represents a model, a list of words"""
    features = 300

    def __init__(self, inp_file_name: str) -> None:
        super().__init__()
        print(f"Loading model from {inp_file_name} ...")
        t0 = process_time()
        num=0
        length=0
        with open(inp_file_name, mode="r", encoding="utf8") as inp_file:
            for line in inp_file:
                sa = line.split()
                if len(sa) > length:
                    length=len(sa)
                    print(f"new vector length {length}")
                num=num+1
                self.append(Word(sa[0], [float(x) for x in sa[1:]]))
        print(f"Loaded in {process_time() - t0} secs")
        print(f"Number of words: {num}")
        

    def find_word(self, text: str) -> Word | None:
        for w in self:
            if w.text == text:
                return w

    def find_similar_words(self, word: Word, n: int = 10) -> list[Word]:
        print(f"find similar words to {word}")
        similar = sorted(self, key=lambda w: w.similarity(word), reverse=True)[:n]
        return similar

    def __repr__(self) -> str:
        return f"Model({len(self)} words)"

    def __getitem__(self, text: str) -> Word:
        return self.find_word(text)

    def __contains__(self, text: str) -> bool:
        return self.find_word(text) is not None


if __name__ == "__main__":
    model = Model("models/glove_short.txt")
