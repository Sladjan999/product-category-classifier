import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
import joblib

# Učitavanje podataka
df = pd.read_csv("data/IMLP4_TASK_03-products.csv")
df.columns = df.columns.str.strip()
df = df.dropna(subset=["Product Title", "Category Label"])
X = df["Product Title"]
y = df["Category Label"]

# Treniranje pipeline-a
pipeline = Pipeline([
    ("tfidf", TfidfVectorizer(max_features=8000, ngram_range=(1,2))),
    ("clf", LogisticRegression(max_iter=2000))
])

pipeline.fit(X, y)

# Čuvanje modela
joblib.dump(pipeline, "model/product_classifier.pkl")
print("✅ Model sačuvan u 'model/product_classifier.pkl'")