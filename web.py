from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    name = request.form.get("name")
    age = request.form.get("age")
    interest = request.form.get("interest")
    difficulty = request.form.get("difficulty")

    # Simple study plan logic
    plan = ""

    if interest == "Programming":
        plan = "Learn C basics → Loops → Functions → DSA"
    elif interest == "AI & ML":
        plan = "Python → Math → Machine Learning → Projects"
    elif interest == "Web Development":
        plan = "HTML → CSS → JavaScript → Flask"
    elif interest == "Data Science":
        plan = "Python → Pandas → Visualization → Projects"

    return f"""
    <h1>Hello {name} 👋</h1>
    <h2>Your Personalized Study Plan</h2>
    <p><b>Interest:</b> {interest}</p>
    <p><b>Difficulty:</b> {difficulty}</p>
    <p><b>Plan:</b> {plan}</p>
    <a href="/">⬅ Go Back</a>
    """

if __name__ == "__main__":
    app.run(debug=True)

