#Write program using the NLTK library to perform part-of-speech tagging on a text.


import nltk
from nltk import word_tokenize, pos_tag
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
text = "The quick brown fox jumps over the lazy dog."
words = word_tokenize(text)
tagged_words = pos_tag(words)
print("Word\t\tPOS Tag")
print("-" * 25)
for word, tag in tagged_words:
    print(f"{word}\t\t{tag}")
