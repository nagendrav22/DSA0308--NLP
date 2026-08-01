Implement a rule-based part-of-speech tagging system using regular expressions using python.


import re
sentence = input("Enter a sentence: ")
words = sentence.split()
print("\nWord\t\tPOS Tag")
print("-" * 30)
for word in words:
    if re.fullmatch(r"\d+", word):
        tag = "CD (Number)"
    elif re.fullmatch(r".*ing$", word):
        tag = "VBG (Verb - Gerund)"
    elif re.fullmatch(r".*ed$", word):
        tag = "VBD (Verb - Past Tense)"
    elif re.fullmatch(r".*ly$", word):
        tag = "RB (Adverb)"
    elif re.fullmatch(r".*ous$", word):
        tag = "JJ (Adjective)"
    elif re.fullmatch(r".*tion$", word):
        tag = "NN (Noun)"
    elif re.fullmatch(r".*s$", word):
        tag = "NNS (Plural Noun)"
    else:
        tag = "NN (Noun)"
    print(f"{word}\t\t{tag}")
