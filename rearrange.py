import random
import sys

words = list(sys.argv)
words.remove(words[0])

def rearrange_words(words):
    random.shuffle(words)
    print(words)


if __name__ in '__main__':
    print(words)
    rearrange_words(words)
