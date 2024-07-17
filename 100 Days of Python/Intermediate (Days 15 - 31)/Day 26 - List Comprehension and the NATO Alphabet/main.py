# NATO Phonetic Alphabet
# By Marco Redulla
# Day 26 (11/07/2024)
import pandas as pd

CSVPATH = r"100 Days of Python\Intermediate (Days 15 - 31)\Day 26 - List Comprehension and the NATO Alphabet\nato_phonetic_alphabet.csv"
phonetic_alphabet = pd.read_csv(CSVPATH)


conversion = {row.letter:row.code for (index,row) in phonetic_alphabet.iterrows()}

user_input = list(input("Enter a word:").upper())

converted = [conversion[char] for char in user_input if char.isalpha()]
print(converted)