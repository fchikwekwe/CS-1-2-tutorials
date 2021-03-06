import random
from termcolor import colored


def get_vocab_list(vocab_file):
    # imports the list of vocabulary words from external file
    vocab = open(vocab_file, "r").readlines()
    vocab_words = []
    for word in vocab:
        new_word = word.rstrip('\n')
        vocab_words.append(new_word)
    return vocab_words

def get_definition_list(definition_file):
    # imports the list of definition from external file
    definitions = open(definition_file, "r").readlines()
    all_definitions = []

    for definition in definitions:
        new_definition = definition.rstrip('\n')
        all_definitions.append(new_definition)
    return all_definitions

def print_definitions(definition_list):
    # printing off definition list for use in the game
    print("-------------------------\n Here are your definitions: \n")
    for definition in definition_list:
        print("{}: {}".format(definition_list.index(definition), definition))
    print("-------------------------")

def choose_definition(vocab_list, random_index, definition_choice, definition_list):
    # compare random word index to definition index
    while True:
        # pick a random word from the list
        random_word = random.choice(vocab_list)
        # get the index of that random word to compare laters
        random_index = vocab_list.index(random_word)
        print(colored("Enter 'Q' at anytime to quit the game.", "magenta"))
        print(colored("Enter 'P' at anytime to print the definitions again", "yellow"))
        definition_choice = input("Enter the number of the definition of {}: ".format(random_word))

        # check if the player wants to exit the game
        if definition_choice.lower() == 'q':
            print("Thanks for playing!")
            break
        elif definition_choice.lower() == 'p':
            print_definitions(definition_list)
            continue
        # check if the input is a number
        elif definition_choice.isdigit() != True:
            print(colored("Please enter a number next time!", "cyan"))
            definition_choice = -1
        # check if the index is within range
        elif int(definition_choice) > len(definition_list) - 1:
            print(colored("Please pick a number on the list!", "cyan"))
            definition_choice = -1
        else:
            pass

        # check if the player has guessed correctly or not
        if random_index == int(definition_choice):
            print(colored("Great job! Let's try another one!", "green"))
        else:
            print(colored("""
            That was not correct! The correct definition was:

            {}

            Let's try again with a new word.""", "red").format(definition_list[int(definition_choice)]))


if __name__ in '__main__':
    # set vocab_file equal to the file we want to import
    vocab_file = "vocab.txt"
    # set definition_file equal to the definitions file we want to import
    definition_file = "vocab_definitions.txt"

    vocab_list = get_vocab_list(vocab_file)
    definition_list = get_definition_list(definition_file)

    print_definitions(definition_list)
    # set random_index and definition_choice equal to a number that is not in the index
    choose_definition(vocab_list, -2, -1, definition_list)
