from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load saved files
cv = pickle.load(open('vectorizer.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))

# Home Route
@app.route('/')
def home():
    return render_template('index.html')

# Prediction Route
@app.route('/predict', methods=['POST'])
def predict():

    message = request.form['message']

    # Simple preprocessing
    transformed_message = message.lower()

    # Vectorization
    vector_input = cv.transform([transformed_message])

    # Prediction
    result = model.predict(vector_input)[0]

    if result == 1:
        prediction = "⚠️ Spam Message"
    else:
        prediction = "✅ Not Spam"

    return render_template(
        'index.html',
        prediction=prediction,
        original_message=message
    )


if __name__ == '__main__':
    app.run(debug=True)