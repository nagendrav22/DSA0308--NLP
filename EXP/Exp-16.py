import spacy
nlp = spacy.load("en_core_web_sm")

text = input("Enter a text: ")

doc = nlp(text)

print("\nNamed Entities:")
print("-" * 40)

for ent in doc.ents:
    print("Entity:", ent.text)
    print("Type  :", ent.label_)
    print("Start :", ent.start_char)
    print("End   :", ent.end_char)
    print("-" * 40)
