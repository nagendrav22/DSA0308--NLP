Implement transformation-based tagging using a set of transformation rules, apply a simple rule to tag words using python.


sentence = "The boys are playing happily"
words = sentence.split()
tags = ["NN"] * len(words)
for i in range(len(words)):
    word = words[i].lower()
    if word in ["the", "a", "an"]:
        tags[i] = "DT"          # Determiner
    elif word in ["is", "am", "are", "was", "were"]:
        tags[i] = "VB"          # Verb
    elif word.endswith("ing"):
        tags[i] = "VBG"         # Gerund Verb
    elif word.endswith("ly"):
        tags[i] = "RB"          # Adverb
    elif word.endswith("s"):
        tags[i] = "NNS"         # Plural Noun
print("Word\t\tPOS Tag")
print("-" * 25)
for word, tag in zip(words, tags):
    print(f"{word}\t\t{tag}")
