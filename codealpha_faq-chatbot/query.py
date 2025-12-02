import joblib
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from preprocess import preprocess

vectorizer = joblib.load("models/vectorizer.pkl")
X = joblib.load("models/tfidf_matrix.pkl")
df = pd.read_pickle("models/faqs.pkl")

def get_answer(question):
    processed = preprocess(question)
    q_vec = vectorizer.transform([processed])
    similarities = cosine_similarity(q_vec, X).flatten()
    idx = similarities.argmax()
    return df.iloc[idx]['answer']
