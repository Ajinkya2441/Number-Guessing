import webview
from flask import Flask, request, jsonify, render_template_string
import random

app = Flask(__name__)
target_number = random.randint(1, 100)
attempts = 0

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Number Guessing Game</title>
    <style>
        body { font-family: sans-serif; background: #222; color: #fff; text-align: center; padding-top: 50px; }
        input, button { font-size: 1.5em; padding: 10px; margin: 10px; border-radius: 5px; border: none; }
        input { width: 100px; }
    </style>
</head>
<body>
    <h1>🎯 Guess the Number (1–100)</h1>
    <input type="number" id="guess" />
    <button onclick="submitGuess()">Submit</button>
    <p id="result"></p>

    <script>
        function submitGuess() {
            fetch("/guess", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ guess: document.getElementById("guess").value })
            }).then(res => res.json())
              .then(data => {
                  document.getElementById("result").innerText = data.result;
              });
        }
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML)

@app.route('/guess', methods=['POST'])
def guess():
    global target_number, attempts
    data = request.get_json()
    guess = int(data['guess'])
    attempts += 1

    if guess < target_number:
        return jsonify(result="🔼 Too low!")
    elif guess > target_number:
        return jsonify(result="🔽 Too high!")
    else:
        msg = f"✅ Correct! You guessed it in {attempts} tries."
        target_number = random.randint(1, 100)
        attempts = 0
        return jsonify(result=msg)

if __name__ == '__main__':
    webview.create_window("Guess the Number", app)
    webview.start()
