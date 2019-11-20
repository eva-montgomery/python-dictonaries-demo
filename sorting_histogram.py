# Sorting a histogram
# Given a histogram tally (one returned from either letter_histogram or word_histogram), print the top 3 words or letters.

# $ python3 word_histogram_tally.py

# Please enter a sentence: To be or not to be do be do be do
# The top three words are:
# be: 4
# do: 3
# to: 2

def word_histogram(word):
    histogram = {}
    word_list = word.split()
    for word in word_list:
        if word in histogram:
            histogram[word] = histogram[word] + 1
        else:
            histogram[word] = 1
    return histogram
print(word_histogram("to be or not to be"))                
