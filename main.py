from flask import Flask, request, jsonify, render_template
import json
import re
import random
import joblib
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

app = Flask(__name__)

# LOAD MODEL
model = joblib.load("model/chatbot_model.pkl")
vectorizer = joblib.load("model/tfidf_vectorizer.pkl")

KEYWORD_RULES = {
    "jadwal_kuliah": [
        "semester baru mulai kapan",
        "semester baru dimulai kapan",
        "semester baru tanggal berapa",
        "kapan semester baru dimulai"
    ],
    "jadwal_uts": [
        "uts", "ujian tengah semester"
    ],
    "jadwal_uas": [
        "uas", "ujian akhir semester"
    ],
    "syarat_wisuda": [
        "syarat wisuda",
        "persyaratan wisuda",
        "memenuhi syarat wisuda",
        "syarat ikut wisuda"
    ],
    "izin_kuliah": [
        "tidak bisa masuk kuliah",
        "tidak bisa hadir kuliah",
        "tidak bisa ikut kuliah",
        "tidak bisa ikut kelas",
        "tidak hadir kuliah",
        "berhalangan hadir kuliah" 
    ],
    "cuti_kuliah": [
       "cuti kuliah",
        "cuti semester",
        "berhenti kuliah sementara",
        "berhenti sementara dari kuliah" 
    ],
    "poin_sispema": [
        "sispema"
    ]
}

# LOAD INTENT
with open("data/intents.json", "r", encoding="utf-8") as file:
    data = json.load(file)


# SASTRAWI
factory = StemmerFactory()
stemmer = factory.create_stemmer()


# 4. FUNGSI PREPROCESSING
def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    text = stemmer.stem(text)

    return text

def detect_keyword_intent(text):
    text = text.lower()

    for intent, keyword in KEYWORD_RULES.items():
        for keyword in keyword:
            if keyword in text:
                return intent

    return None

# 5. FUNGSI MENCARI RESPONSE
def get_response(intent_tag):
    for intent in data["intents"]:
        if intent["tag"] == intent_tag:
            return random.choice(
                intent["responses"]
            )

    return "Maaf, saya belum memahami pertanyaan tersebut."

# 6. FUNGSI CHATBOT
def chatbot(user_input):
    #cek keyword dulu
    keyword_intent = detect_keyword_intent(user_input)

    if keyword_intent:
        response = get_response(keyword_intent)

        return{
            "intent": keyword_intent,
            "response": response,
            "confidence": 1.0
        }

    # Preprocessing pertanyaan
    processed_input = preprocess_text(user_input)

    # Mengubah pertanyaan menjadi TF-IDF
    input_vector = vectorizer.transform([processed_input])

    # Memprediksi intent
    predicted_intent = model.predict(input_vector)[0]

    probabilities = model.predict_proba(input_vector) [0]
    
    confidence = max(probabilities)

    threshold = 0.50

    # confident terlalu rendah
    if confidence < threshold:
        return {
            "intent": "tidak_dikenali", 
            "response": "Maaf, saya belum memahami pertanyaan tersebut.",
            "confidence": confidence
        }
    
    # confident cukup tinggi
    response = get_response(predicted_intent)

    return {
                "intent": predicted_intent, 
                "response": response,
                "confidence": confidence
            }

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data_input = request.get_json()
    user_message = data_input.get("message", "")

    if not user_message:
        return jsonify({
            "response": "silahkan masukan pertanyaan."
        })

    result = chatbot(user_message)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)