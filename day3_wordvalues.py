"""
Find the dictionary word with the highest value using Scrabble rules.

There are three tasks to complete for this Bite:

Finish the function load_words which creates and returns a list of words from a text file.
Finish the function calc_word_value which calculates and returns a word's Scrabble value.
Finish the function max_word_value which finds and returns the dictionary word with the highest score.
Notes:

The text of the dictionary is downloaded for you and is available with the path contained in the variable DICTIONARY.
The words in the file are separated by a newline character.
Letters not found in LETTER_SCORES score zero points.
"""

import os
import urllib.request

TMP = os.getenv("TMP", "/tmp")
S3 = 'https://bites-data.s3.us-east-2.amazonaws.com/'
DICT = 'dictionary.txt'
DICTIONARY = os.path.join(TMP, DICT)
urllib.request.urlretrieve(f'{S3}{DICT}', DICTIONARY)

scrabble_scores = [(1, "E A O I N R T L S U"), (2, "D G"), (3, "B C M P"),
                   (4, "F H V W Y"), (5, "K"), (8, "J X"), (10, "Q Z")]
LETTER_SCORES = {letter: score for score, letters in scrabble_scores
                 for letter in letters.split()}

def load_words():
    """Load the words dictionary (DICTIONARY constant) into a list and return it"""
    with open(DICTIONARY, 'r') as file:
        words = [word.strip() for word in file.readlines()]
    return words
    

def calc_word_value(word):
    """Given a word calculate its value using the LETTER_SCORES dict"""
    word = word.upper()
    score = 0
    for letter in word:
        score += LETTER_SCORES.get(letter, 0)
    return score


def max_word_value(words):
    """Given a list of words calculate the word with the maximum value and return it"""
    if not words:
        return None
    max_word = max(words, key=calc_word_value)
    return max_word


print(load_words())
print(calc_word_value(word='zootomy'))
print(max_word_value(words='zootomy'))