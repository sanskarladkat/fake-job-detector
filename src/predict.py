import pickle
import re
import numpy as np
from scipy.sparse import hstack
import os

# Get the project root directory
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
model_dir = os.path.join(project_root, "model")
model_path = os.path.join(model_dir, "model.pkl")
tfidf_path = os.path.join(model_dir, "tfidf.pkl")

if not os.path.exists(model_path) or not os.path.exists(tfidf_path):
    raise FileNotFoundError(
        f"Could not find model assets. Expected files:\n  {model_path}\n  {tfidf_path}\nPlease verify the 'model' directory exists and contains 'model.pkl' and 'tfidf.pkl'."
)

with open(model_path, "rb") as f:
    model = pickle.load(f)
with open(tfidf_path, "rb") as f:
    tfidf = pickle.load(f)

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