
import sys

word = sys.argv[1]

def string_reverse(word):
    word_list = list(word)
    print(word_list)
    word_list.reverse()
    print(word_list)
    new_word = ''.join(word_list)
    print(new_word)

if __name__ in '__main__':
    string_reverse(word)
