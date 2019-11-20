# Letter Summary
# Write a letter_histogram program that asks the user for input, 
# and prints a dictionary containing the tally of how many times each letter in the alphabet was used in the word. 
# For example:

# $ python3 letter_histogram.py
# Please enter a word: banana
# {'a': 3, 'b': 1, 'n': 2}

user_input = input("Give me a word: ")

def letter_histogram(word):
    dictio = {}
    for letter in word:
        keys = dictio.keys()
        if letter in keys:
            dictio[letter] += 1
        else:
            dictio[letter] = 1
    return dictio
print(letter_histogram(user_input))                

letter_histogram(user_input)