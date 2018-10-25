import random

vocab = open("vocab.txt", "r").readlines()
# print(vocab)
vocab_list = []
def clean_list(vocab, vocab_list):
    for word in vocab:
        new_word = word.rstrip('\n')
        print(new_word)
        vocab_list.append(new_word)
    # print(vocab_list)

random.choice(vocab_list)

# psuedocode
# flash a word
# get player input on definition
# show player the correct definition
