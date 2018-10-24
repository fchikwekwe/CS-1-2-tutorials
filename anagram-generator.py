import sys
import random

letters = list(sys.argv[1])
# print(letters)

def anagram_gen(letters):
    random.shuffle(letters)
    print(letters)

if __name__ in '__main__':
    anagram_gen(letters)
