import random
import time

vocab = open("vocab.txt", "r").readlines()
vocab_list = []

for word in vocab:
    new_word = word.rstrip('\n')
    vocab_list.append(new_word)

definitions = open("vocab_definitions.txt", "r").readlines()
definition_list = []

for definition in definitions:
    new_definition = definition.rstrip('\n')
    definition_list.append(new_definition)
# print(definition_list)

print("-------------------------\n Here are your definitions: \n")
for definition in definition_list:
    print("{}: {}".format(definition_list.index(definition), definition))
print("-------------------------")

random_word = random.choice(vocab_list)
print("Enter the number of the definition of {}: ".format(random_word))


# psuedocode
# flash a word
# get player input on definition
# show player the correct definition
