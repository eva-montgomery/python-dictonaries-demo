# Word Summary
# Write a word_histogram program that asks the user for a sentence as its input, 
# and prints a dictionary containing the tally of how many times each word in the 
# alphabet was used in the text. For example:

# $ python3 word_histogram.py
# Please enter a sentence: To be or not to be
# {'to': 2, 'be': 2, 'or': 1, 'not': 1}

user_input = input("Please enter a sentence: ")

def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts 

print(word_count(user_input))

