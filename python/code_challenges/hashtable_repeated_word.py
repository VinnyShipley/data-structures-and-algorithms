from data_structures.hashtable import Hashtable
import re


def first_repeated_word(string):

    table = Hashtable()
    filtered = re.sub(r'[.|,|?|!]', '', string)
    words = filtered.lower().split()

    for word in words:

        if table.contains(word):
            return word

        if not table.contains(word):
            table.set(word, 1)


    return None







