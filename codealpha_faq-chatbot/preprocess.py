import re
import spacy

nlp = spacy.load("en_core_web_sm", disable=["parser","ner"])

def clean_text(text):
    text = text.lower().strip()
    text = re.sub(r'\s+', ' ', text)
    return text

def preprocess(text):
    text = clean_text(text)
    doc = nlp(text)
    tokens = [t.lemma_ for t in doc if not t.is_stop and not t.is_punct]
    return " ".join(tokens)
