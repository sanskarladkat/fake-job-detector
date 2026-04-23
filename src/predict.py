import pickle
import re
import numpy as np
from scipy.sparse import hstack
import os

# Get the project root directory
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
model_path = os.path.join(project_root, "models", "model.pkl")
tfidf_path = os.path.join(project_root, "models", "tfidf.pkl")

model = pickle.load(open(model_path, "rb"))
tfidf = pickle.load(open(tfidf_path, "rb"))

keywords = ['urgent', 'quick money', 'no experience', 'work from home']

def clean_text(text):
    text = str(text).lower()
    text = re.sub(r'[^a-zA-Z]', ' ', text)
    return text

def predict_job(text):
    text_clean = clean_text(text)

    
    X_text = tfidf.transform([text_clean])

    
    text_length = len(text_clean)
    num_words = len(text_clean.split())
    has_suspicious_words = int(any(word in text_clean for word in keywords))

    X_extra = np.array([[text_length, num_words, has_suspicious_words]])


    X = hstack([X_text, X_extra])

    
    prob = model.predict_proba(X)[0][1]

    if prob > 0.7:
        risk = "HIGH ⚠️"
    elif prob > 0.4:
        risk = "MEDIUM ⚠️"
    else:
        risk = "LOW ✅"

    return prob, risk