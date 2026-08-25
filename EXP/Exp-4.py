#Implement a finite-state machine for morphological parsing. In this example, we'll create a simple machine to generate plural forms of English nouns using python.

def generate_plural(noun):
    if noun.endswith("y") and len(noun) > 1 and noun[-2].lower() not in "aeiou":
        return noun[:-1] + "ies"
    elif noun.endswith(("s", "x", "z", "ch", "sh")):
        return noun + "es"
    else:
        return noun + "s"
words = [
    "cat", "dog", "bus", "box",
    "church", "dish", "baby",
    "toy", "buzz"
]
print("Singular\tPlural")
print("-" * 25)
for word in words:
    print(f"{word}\t\t{generate_plural(word)}")
