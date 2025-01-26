
from flask import Flask, jsonify, render_template
import random
from datetime import datetime

app = Flask(__name__)
#
# Sample quotes and facts
# QUOTES = [
#     "The best way to predict the future is to invent it. – Alan Kay",
#     "Life is what happens when you’re busy making other plans. – John Lennon",
#     "Success is not the key to happiness. Happiness is the key to success. – Albert Schweitzer",
#     "Your time is limited, so don’t waste it living someone else’s life. – Steve Jobs",
#     "The only way to do great work is to love what you do. – Steve Jobs"
# ]

FACTS = [
    "Honey never spoils. Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old!",
    "Octopuses have three hearts.",
    "Bananas are berries, but strawberries aren't.",
    "There are more stars in the universe than grains of sand on Earth.",
    "A day on Venus is longer than a year on Venus."
]

@app.route("/")
def home():
    # random_quote = random.choice(QUOTES)
    random_fact = random.choice(FACTS)
    time_fetched = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return render_template("index.html" , fact=random_fact, time=time_fetched)
#""",quote=random_quote"""
# @app.route("/quote")
# def get_quote():
#     random_quote = random.choice(QUOTES)
#     return jsonify({"quote": random_quote})

@app.route("/fact")
def get_fact():
    random_fact = random.choice(FACTS)
    return jsonify({"fact": random_fact})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    