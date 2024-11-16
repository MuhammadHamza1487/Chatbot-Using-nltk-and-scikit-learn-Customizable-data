# Chatbot with Logistic Regression and Flask

This project is a basic chatbot application built using Python. It uses `TfidfVectorizer` for text feature extraction and `LogisticRegression` for classifying user inputs. The chatbot is hosted on a Flask web server, which provides a simple interface for user interaction.

---

## Features

- **Text classification** using Logistic Regression.
- **Customizable intents and responses** for creating personalized bots.
- **Web-based interface** using Flask for user interaction.
- Model training and saving for efficient deployment.

---

## Requirements

- Python 3.9.2
- Required Python libraries:
  - `nltk`
  - `scikit-learn`
  - `joblib`
  - `Flask`

---

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/chatbot.git](https://github.com/MuhammadHamza1487/Chatbot-Using-nltk-and-scikit-learn-Customizable-data/
   cd Chatbot-Using-nltk-and-scikit-learn-Customizable-data
   ```

2. **Set up a virtual environment (optional):**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install the dependencies:**
   ```bash
   pip install ______
   ```

4. **Download NLTK data:**
   - The script automatically downloads required `nltk` data files when run for the first time. Alternatively, you can pre-download them:
     ```python
     import nltk
     nltk.download('punkt')
     ```

---

## Usage

### 1. Train the Model
Train and save the chatbot model using the `training.py` script:
```bash
python training.py
```
This generates a `chatbot_model.pkl` file containing the trained model and vectorizer.

### 2. Run the Flask App
Start the web server:
```bash
python app.py
```
Visit the chatbot interface in your browser at `http://127.0.0.1:5000/`.

### 3. Chat with the Bot
Type a message into the interface, and the bot will respond based on the intents defined in the `data.py` file.

---

## Project Structure

- **`training.py`**: Script for training the chatbot model.
- **`app.py`**: Flask application for hosting the chatbot.
- **`data.py`**: Contains intents (tags, patterns, and responses) for training the chatbot.
- **`nltk_data`**: Directory to store downloaded NLTK data.
- **`chatbot_model.pkl`**: Saved model and vectorizer (generated after training).
- **`templates/index.html`**: Web interface for the chatbot.

---

## Customize Intents

Modify the `data.py` file to customize the bot’s responses. Define intents with the following structure:
```python
intents = [
    {
        "tag": "greeting",
        "patterns": ["Hi", "Hello", "How are you?"],
        "responses": ["Hello!", "Hi there!", "How can I assist you?"]
    },
    ...
]
```

---

## Troubleshooting

- Ensure all required libraries are installed using `pip install _____`.
- If the model is not found, re-train using `training.py`.
- Verify the Python version (3.9.2) and compatibility of installed libraries.

---

## Contributing

Contributions are welcome! Feel free to fork the repository, make improvements, and submit a pull request.

---

### Author

- **Muhammad Hamza**

For queries, contact at [muhammadhamza1487@gmail.com].
