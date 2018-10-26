import random
import time

def get_vocab_list(vocab_file):
    vocab = open(vocab_file, "r").readlines()
    vocab_words = []

    for word in vocab:
        new_word = word.rstrip('\n')
        vocab_list.append(new_word)

def get_definition_list(definition_file):
    definitions = open(definition_file, "r").readlines()
    definition_list = []

    for definition in definitions:
        new_definition = definition.rstrip('\n')
        definition_list.append(new_definition)

def print_definitions(definition_list):
    print("-------------------------\n Here are your definitions: \n")
    for definition in definition_list:
        print("{}: {}".format(definition_list.index(definition), definition))
    print("-------------------------")

def choose_definition(vocab_list):
definition_choice = input("Enter the number of the definition of {}: ".format(random_word))
choice_index = definition_list[int(definition_choice)]
print(choice_index)

while random_index != int(definition_choice):
    print(random_index)
    definition_choice = input("Enter the number of the definition of {}: ".format(random_word))
    print("That was not correct! The correct definition was :\n{}. \nLet's try again with a new word.".format(definition_list[int(definition_choice)]))

    try:
        time.sleep(4)
    except KeyboardInterrupt:
        pass

    random_word = random.choice(vocab_list)
    print(random_word)
    random_index = vocab_list.index(random_word)

# psuedocode
# flash a word
# get player input on definition
# show player the correct definition

if __name__ in '__main__':
    vocab_file = "vocab.txt"
    definition_file = "vocab_definitions.txt"

    vocab_list = get_vocab_list(vocab_file)
    definition_list = get_definition_list(definition_file)

    print_definitions(definition_list)

    random_word = random.choice(vocab_list)
    print(random_word)
    random_index = vocab_list.index(random_word)
