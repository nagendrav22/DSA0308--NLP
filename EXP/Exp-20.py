from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

documents = [
    "Python is a popular programming language",
    "Machine learning uses Python for data analysis",
    "Natural language processing deals with text data",
    "Information retrieval searches and ranks documents",
    "Python is useful for machine learning and data science"
]

query = input("Enter your search query: ")

vectorizer = TfidfVectorizer()

tfidf_matrix = vectorizer.fit_transform(documents)

query_vector = vectorizer.transform([query])

similarity_scores = cosine_similarity(query_vector, tfidf_matrix)[0]

ranked_documents = similarity_scores.argsort()[::-1]

print("\nSearch Results")
print("=" * 50)

for rank, index in enumerate(ranked_documents, start=1):
    print("Rank:", rank)
    print("Score:", round(similarity_scores[index], 4))
    print("Document:", documents[index])
    print("-" * 50)
