"""
Write a function that returns the most common word in this Harry Potter text.

Make sure you convert to lowercase, strip out non-alphanumeric characters and stopwords. 
Your function should return a tuple of (most_common_word, frequency).
"""

"""
take the whole stopwords.txt and remove all the occurrences in harry.txt, also remove non-alphanumeric characters and convert it to lowercase.

most common word?

- take each word and check for its occurrences, save the word and its occurrence as a key-value pair. (can use counter library)
- output the key-value pair which has the max (highest) value. 
"""
from collections import Counter
import re

def most_common(text, stopwords_file):
        # read stopwords from file
        with open(stopwords_file, 'r') as stop_file:
                stop_words = set(stop_file.read().split())

        # read content from the text file
        with open(text, 'r') as in_file:
                content = in_file.read()

        # clean the text
        clean_text = re.sub(r'[^a-zA-Z\s]', '', content.lower())

        # remove stopwords
        clean_words = [word for word in clean_text.split() if word not in stop_words]

        # count word occurrences
        word_counts = Counter(clean_words)

        # find the most common word
        most_common_word, frequency= word_counts.most_common(1)[0]

        return most_common_word, frequency




text = '/harry.txt'
stopwords_file = 'stopwords.txt'

print(most_common(text, stopwords_file))