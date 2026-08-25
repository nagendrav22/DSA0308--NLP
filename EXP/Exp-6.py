#Implement a basic N-gram model for text generation. For example, generate text using a bigram model using python. 
# Morphological Analysis using NLTK (Without Porter Stemmer)


import random
text = "the cat sat on the mat the cat ate the fish"
words = text.split()
bigram = {}
for i in range(len(words) - 1):
    word = words[i]
    next_word = words[i + 1]
    if word not in bigram:
        bigram[word] = []
    bigram[word].append(next_word)
current_word = "the"      
generated_text = [current_word]
for i in range(9):        
    if current_word in bigram:
        next_word = random.choice(bigram[current_word])
        generated_text.append(next_word)
        current_word = next_word
    else:
        break
print("Generated Text:")
print(" ".join(generated_text))
