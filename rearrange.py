import random
import sys

#command line argument
words = list(sys.argv)
# remove the file name from the list
words.remove(words[0])

def rearrange_words(words):
    random.shuffle(words)
    print(words)


if __name__ in '__main__':
    print(words)
    rearrange_words(words)
