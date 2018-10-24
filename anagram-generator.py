import sys
import random

words = open("words.txt", "r")
print(words)
letters = list(sys.argv[1])

def anagram_gen(letters):
    making_word = True
    while making_word:
        random.shuffle(letters)
        print(letters)
        new_word = "".join(letters)
        print(new_word)
        if new_word not in words:
            continue
        else:
            break
    return new_letters



if __name__ in '__main__':
    anagram_gen(letters)
