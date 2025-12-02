from flask import Flask, request, jsonify, render_template
from sklearn.metrics.pairwise import cosine_similarity
import pickle
import json

app = Flask(__name__)

# Load FAQ data
with open("faqs.json") as f:
    faqs = json.load(f)

# Load vectorizer & vectors
with open("vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

with open("faq_vectors.pkl", "rb") as f:
    faq_vectors = pickle.load(f)

# ----------------------------
#   HOMEPAGE ROUTE (FIXED)
# ----------------------------
@app.route("/")
def home():
    return render_template("index.html")

# ----------------------------
#   CHAT API ROUTE
# ----------------------------
@app.route("/chat", methods=["POST"])
def chat():
    user_msg = request.json["message"]
    user_vec = vectorizer.transform([user_msg])
    similarity = cosine_similarity(user_vec, faq_vectors)
    best_match = similarity.argmax()
    answer = list(faqs.values())[best_match]
    return jsonify({"answer": answer})

# ----------------------------
#   START FLASK SERVER
# ----------------------------
if __name__ == "__main__":
    app.run(port=5000, debug=True)
