#Use the Porter Stemmer algorithm to perform word stemming on a list of words using python libraries.


from nltk.stem import PorterStemmer
stemmer = PorterStemmer()
words = [
    "running", "playing", "studies", "studying",
    "connected", "connection", "happiness",
    "flying", "wolves", "cars"
]
print("Original Word\tStemmed Word")
print("-" * 35)
for word in words:
    stem = stemmer.stem(word)
    print(f"{word}\t\t{stem}")
