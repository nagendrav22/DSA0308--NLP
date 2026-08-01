Implement a simple stochastic part-of-speech tagging algorithm using 
a basic probabilistic model to assign POS tags using python.


pos_prob = {
    "book": {"NN": 0.7, "VB": 0.3},
    "can": {"MD": 0.6, "VB": 0.4},
    "run": {"VB": 0.8, "NN": 0.2},
    "dog": {"NN": 1.0},
    "quickly": {"RB": 1.0},
    "beautiful": {"JJ": 1.0},
    "the": {"DT": 1.0},
    "is": {"VBZ": 1.0}
}
sentence = "the dog can run quickly"
words = sentence.split()
print("Word\t\tPOS Tag")
print("-" * 25)
for word in words:
    if word in pos_prob:
        tag = max(pos_prob[word], key=pos_prob[word].get)
        print(f"{word}\t\t{tag}")
    else:
        print(f"{word}\t\tUnknown")
