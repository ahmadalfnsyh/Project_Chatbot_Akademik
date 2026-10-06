import json
import re
import os
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)
import joblib

# 1. MEMBUAT STEMMER BAHASA INDONESI
factory = StemmerFactory()
stemmer = factory.create_stemmer()

stop_factory = StopWordRemoverFactory()
stopword = stop_factory.create_stop_word_remover()

# 2. FUNGSI PREPROCESSING
def preprocess_text(text):
    # Mengubah huruf menjadi lowercase
    text = text.lower()

    # Menghapus tanda baca dan karakter khusus
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)

    # Menghapus spasi berlebihan
    text = re.sub(r'\s+', ' ', text).strip()

    text = stopword.remove(text)

    # Stemming Bahasa Indonesia
    text = stemmer.stem(text)

    return text

# 3. MEMBACA DATASET intents.json
with open("data/intents.json", "r", encoding="utf-8") as file:
    data = json.load(file)

# 4. MENGAMBIL PATTERNS DAN TAGS
patterns = []
tags = []

for intent in data["intents"]:

    for pattern in intent["patterns"]:
        patterns.append(pattern)
        tags.append(intent["tag"])


print("======================================")
print("      TRAINING CHATBOT AKADEMIK")
print("======================================")

print("Jumlah pertanyaan :", len(patterns))
print("Jumlah intent     :", len(set(tags)))

# 5. PREPROCESSING SEMUA PERTANYAAN
processed_patterns = []

for pattern in patterns:
    processed = preprocess_text(pattern)
    processed_patterns.append(processed)


print("\nContoh preprocessing:")

for i in range(min(5, len(patterns))):
    print(f"Asli : {patterns[i]}")
    print(f"Hasil: {processed_patterns[i]}")
    print()

# 6. TF-IDF
vectorizer = TfidfVectorizer()

X = vectorizer.fit_transform(processed_patterns)

print("Ukuran data TF-IDF:", X.shape)

# 7. MEMBAGI DATA TRAINING DAN TESTING
X_train, X_test, y_train, y_test = train_test_split(
    X,
    tags,
    test_size=0.2,
    random_state=42,
    stratify=tags
)

print("\nPembagian data:")
print("Data training:", X_train.shape[0])
print("Data testing :", X_test.shape[0])

# 8. MEMBUAT MODEL MACHINE LEARNING
model = LogisticRegression(
    max_iter=1000
)

# 9. MELATIH MODEL
print("\nTraining model...")

model.fit(X_train, y_train)

print("Training selesai.")

# 10. PREDIKSI DATA TESTING
y_pred = model.predict(X_test)

# 11. EVALUASI MODEL
accuracy = accuracy_score(y_test, y_pred)

print("\n======================================")
print("           HASIL EVALUASI")
print("======================================")

print(f"Accuracy: {accuracy:.2%}")

print("\nClassification Report:")
print(
    classification_report(
        y_test,
        y_pred,
        zero_division=0
    )
)

# 12. CONFUSION MATRIX
print("Confusion Matrix:")

cm = confusion_matrix(y_test, y_pred)

print(cm)

# 13. MEMBUAT FOLDER MODEL
os.makedirs("model", exist_ok=True)

# 14. MENYIMPAN MODEL
joblib.dump(model, "model/chatbot_model.pkl")

# Menyimpan TF-IDF vectorizer
joblib.dump(vectorizer, "model/tfidf_vectorizer.pkl")

# 15. MENYIMPAN DATA INTENT
joblib.dump(
    list(set(tags)),
    "model/intent_tags.pkl"
)


print("\n======================================")
print("Model berhasil disimpan!")
print("======================================")

print("model/chatbot_model.pkl")
print("model/tfidf_vectorizer.pkl")
print("model/intent_tags.pkl")