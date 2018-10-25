import random
import sys

#command line argument
words = list(sys.argv)
# remove the file name from the list
words.remove(words[0])
new_words = list()
def rearrange_words(words):
    # this function takes the original list and rearranges the words into a new list
    while len(words) > 0:
        new_word = random.choice(words)
        new_words.append(new_word)
        words.remove(new_word)
    return new_words


if __name__ in '__main__':
    print(" ".join(rearrange_words(words)))
