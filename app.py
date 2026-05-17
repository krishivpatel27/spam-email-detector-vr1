from flask import Flask, render_template, request

import pickle

import re
import string

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
app = Flask(__name__)
# Load the trained model
with open("linear_svm_model.pkl", "rb") as file:
    
    model = pickle.load(file)

with open("tfidf_vectorizer.pkl", "rb") as file:
    
    vectorizer = pickle.load(file)
    
lemmatizer = WordNetLemmatizer()

stop_words = set(stopwords.words('english'))
def clean_text(text):

    text = text.lower()

    text = re.sub(r'http\S+', '', text)

    text = re.sub(r'\S+@\S+', '', text)

    text = re.sub(r'\d+', '', text)

    text = text.translate(
        str.maketrans('', '', string.punctuation)
    )

    text = re.sub(r'\s+', ' ', text).strip()

    words = text.split()

    words = [
        lemmatizer.lemmatize(word)
        for word in words
        if word not in stop_words
    ]

    return " ".join(words)
@app.route("/")
def home():

    return render_template("index.html")
@app.route("/predict", methods=["POST"])

@app.route("/predict", methods=["POST"])

def predict():

    email = request.form["email"]

    cleaned_email = clean_text(email)

    vectorized_email = vectorizer.transform(
        [cleaned_email]
    )

    prediction = model.predict(
        vectorized_email
    )

    decision_score = model.decision_function(
    vectorized_email
)[0]

    if decision_score > 1.5:

        risk_level = "HIGH RISK"

    elif decision_score > 0.5:

        risk_level = "MEDIUM RISK"

    else:

        risk_level = "LOW RISK"

    important_words = []

    words = cleaned_email.split()

    feature_names = vectorizer.get_feature_names_out()

    coefficients = model.coef_[0]

    for word in words:

        if word in feature_names:

            index = list(feature_names).index(word)

            weight = coefficients[index]

            if weight > 0:

                important_words.append(word)

    important_words = list(set(important_words))

    if prediction[0] == 1:

        result = "SPAM"

    else:

        result = "HAM"

    return render_template(

        "index.html",

        prediction=result,

        risk_level=risk_level,

        important_words=important_words,

        email_text=email
    )
if __name__ == "__main__":

    app.run(debug=True)