import sys

phrase = list(sys.argv)
print(phrase)
phrase.remove(phrase[0])
print(phrase)
new_phrase = ' '.join(phrase)

cow = open("cowsay_art.py", "r")

for
