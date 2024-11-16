from flask import Flask, render_template, request, jsonify
import joblib
import random
from data import intents

# Initialize Flask app
app = Flask(__name__)

# Load the model and vectorizer
vectorizer, clf = joblib.load('chatbot_model.pkl')

# Define the chatbot function
def chatbot(input_text):
    input_text = vectorizer.transform([input_text])
    tag = clf.predict(input_text)[0]
    for intent in intents:
        if intent['tag'] == tag:
            response = random.choice(intent['responses'])
            return response
    return "I'm sorry, I don't understand that."

# Define routes
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get_response", methods=["POST"])
def get_response():
    user_input = request.json.get("message")  # Receive JSON message
    response = chatbot(user_input)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
