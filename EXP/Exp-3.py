#Write program demonstrates how to perform morphological analysis using the NLTK library in Python.

import nltk
from nltk.stem import PorterStemmer, LancasterStemmer, WordNetLemmatizer
nltk.download('wordnet')
nltk.download('omw-1.4')
porter = PorterStemmer()
lancaster = LancasterStemmer()
lemmatizer = WordNetLemmatizer()
words = [
    "running", "studies", "playing", "wolves",
    "better", "cars", "connected", "flying"
]
print("{:<12} {:<12} {:<12} {:<12}".format(
    "Original", "Porter", "Lancaster", "Lemma"))
print("-" * 50)
for word in words:
    porter_word = porter.stem(word)
    lancaster_word = lancaster.stem(word)
    lemma_word = lemmatizer.lemmatize(word)
    print("{:<12} {:<12} {:<12} {:<12}".format(
        word, porter_word, lancaster_word, lemma_word))
