from data_structures.hashtable import Hashtable
import re


def first_repeated_word(string):
    table = Hashtable()
    filtered = re.sub(r'^\W+|$\W+', ' ', string)
    words = re.findall(r"\b[a-zA-Z]\w+\b", filtered)
    print(words)
    for word in words:
        lower_word = str(word).lower()
        print(lower_word)
        if table.contains(lower_word):
            return lower_word
        if not table.contains(lower_word):
            table.set(lower_word, 1)
    if words == None:
        return None




story = "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only..."

first_repeated_word(story)


r"\b[a-zA-Z]\w+\b"



