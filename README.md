# 📧 Spam Email Detector

An AI-powered email classification web app built with Flask and Machine Learning. Paste any email content and instantly find out if it's spam or legitimate (ham), along with a risk level and the key words that triggered the detection.

---

## 🚀 Features

- **Spam / Ham Classification** — detects whether an email is spam or not
- **Risk Level Scoring** — rates detected spam as Low, Medium, or High risk using SVM decision scores
- **Keyword Highlighting** — shows the important words that contributed to the spam prediction
- **Full NLP Preprocessing** — URLs, emails, digits, punctuation, and stopwords removed before classification

---

## 🗂️ Project Structure

```
spam-email-detector/
├── app.py                  # Flask app with NLP preprocessing pipeline
├── linear_svm_model.pkl    # Trained Linear SVM model
├── tfidf_vectorizer.pkl    # TF-IDF Vectorizer
├── templates/
│   └── index.html
└── static/
    └── style.css
```

---

## 🛠️ Tech Stack

- **Backend:** Python, Flask
- **ML/NLP:** scikit-learn, NLTK (lemmatization, stopword removal)
- **Model:** TF-IDF + Linear SVM
- **Frontend:** HTML, CSS (Jinja2 templates)

---

## 🧠 How It Works

Each email goes through a full NLP preprocessing pipeline before classification:

1. **Lowercasing** — normalize all text
2. **Cleaning** — strip URLs, email addresses, digits, and punctuation
3. **Stopword Removal** — filter out common words that add no signal
4. **Lemmatization** — reduce words to their base form via NLTK's WordNetLemmatizer
5. **TF-IDF Vectorization** — convert cleaned text into numerical features
6. **Linear SVM Classification** — predict spam or ham using a trained Linear SVM
7. **Risk Scoring** — use the SVM decision score to assign Low / Medium / High risk

---

## 📊 Dataset

Trained on the **[Enron Spam Dataset](http://www.aueb.gr/users/ion/data/enron-spam/)** — a large real-world email dataset derived from the Enron email corpus with spam/ham labels. This ensures the model generalizes well to actual email content.

> ⚠️ The `.pkl` model files are included in this repo for convenience. For larger models, consider using Git LFS or external storage.

---
