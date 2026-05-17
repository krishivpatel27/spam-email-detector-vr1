# 📧 Spam Email Detector

An AI-powered email classification web app built with Flask and Machine Learning. Paste any email content and instantly find out if it's spam or legitimate (ham), along with a risk level and the key words that triggered the detection.

---

## 🚀 Features

- **Spam / Ham Classification** — detects whether an email is spam or not
- **Risk Level Scoring** — rates detected spam as Low, Medium, or High risk using SVM decision scores
- **Keyword Highlighting** — shows the important words that contributed to the spam prediction
- **Two model versions** — v1 (CountVectorizer + basic model) and v2 (TF-IDF + Linear SVM with full NLP preprocessing)

---

## 🗂️ Project Structure

```
spam-email-detector/
│
├── spam-email-detector-vr1/        # Version 1 — simple baseline
│   ├── app.py                      # Flask app
│   ├── model.pkl                   # Trained ML model
│   ├── vectorizer.pkl              # CountVectorizer
│   ├── datasets/
│   │   └── spam.csv                # Training dataset
│   ├── templates/
│   │   └── index.html
│   └── static/
│       └── style.css
│
└── spam-email-detector-vr2/        # Version 2 — improved with SVM + TF-IDF
    ├── app.py                      # Flask app with NLP preprocessing
    ├── linear_svm_model.pkl        # Linear SVM model
    ├── tfidf_vectorizer.pkl        # TF-IDF Vectorizer
    ├── templates/
    │   └── index.html
    └── static/
        └── style.css
```

---

## 🛠️ Tech Stack

- **Backend:** Python, Flask
- **ML/NLP:** scikit-learn, NLTK (lemmatization, stopword removal)
- **Models:** CountVectorizer + ML classifier (v1), TF-IDF + Linear SVM (v2)
- **Frontend:** HTML, CSS (Jinja2 templates)

---

## ⚙️ Setup & Installation

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/spam-email-detector.git
cd spam-email-detector
```

### 2. Create and activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install flask scikit-learn nltk
```

### 4. Download NLTK data (required for v2)
```python
import nltk
nltk.download('stopwords')
nltk.download('wordnet')
```

### 5. Run the app

**Version 1:**
```bash
cd spam-email-detector-vr1
python app.py
```

**Version 2:**
```bash
cd spam-email-detector-vr2
python app.py
```

Then open your browser at `http://127.0.0.1:5000`

---

## 🧠 How It Works

**Version 1** uses a basic CountVectorizer with lowercasing as the only preprocessing step.

**Version 2** adds a full NLP preprocessing pipeline before vectorization:
- Lowercasing
- Removal of URLs, emails, digits, and punctuation
- Stopword removal
- Lemmatization (via NLTK WordNetLemmatizer)
- TF-IDF vectorization
- Linear SVM classification with decision score-based risk levels

---

## 📊 Datasets

The models were trained on two datasets:

- **[SMS Spam Collection Dataset](https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset)** (`spam.csv`) — a labeled collection of SMS spam and ham messages, used in v1.
- **[Enron Spam Dataset](http://www.aueb.gr/users/ion/data/enron-spam/)** — a large real-world email dataset derived from the Enron email corpus, with spam/ham labels. Used to improve v2's generalization on actual email content.

> ⚠️ The `datasets/` folder and `.pkl` model files are included in this repo for convenience since they are small enough. For larger datasets or models, consider using Git LFS or external storage.

