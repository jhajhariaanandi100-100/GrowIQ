from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/result", methods=["POST"])
def result():
    age = request.form["age"]
    difficulty = request.form["difficulty"]
    interest = request.form["interest"]

    if difficulty == "memory":
        plan = "Use visual learning with flashcards."
    elif difficulty == "attention":
        plan = "Use short interactive activities."
    else:
        plan = "Use audio-based learning."

    return f"""
    <h2>GrowIQ Learning Plan</h2>
    <p>Age: {age}</p>
    <p>{plan}</p>
    """

app.run(debug=True)
