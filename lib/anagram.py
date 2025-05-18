# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word.lower()
        self.word_letters = sorted(self.word)

    def match(self, word_list):
        return [w for w in word_list if sorted(w.lower()) == self.word_letters and w.lower() != self.word]
