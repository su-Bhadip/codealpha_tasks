from sklearn.feature_extraction.text import TfidfVectorizer
import pickle
import json

faqs = {
    "What is Python?": "Python is a programming language.",
    "How many states in India?": "India has 28 states and 8 union territories.",
    "What is AI?": "AI stands for Artificial Intelligence."
}

with open("faqs.json", "w") as f:
    json.dump(faqs, f)

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(faqs.keys())

with open("vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)

with open("faq_vectors.pkl", "wb") as f:
    pickle.dump(X, f)
