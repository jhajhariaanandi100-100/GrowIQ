from flask import Flask, render_template, request
import json, os

app = Flask(__name__)

DATA_FILE = "students.json"

# Home Page
@app.route("/")
def home():
    return render_template("index.html")

# Form Page
@app.route("/form")
def form():
    return render_template("form.html")

# Process Form & Generate Plan
@app.route("/generate-plan", methods=["POST"])
def generate_plan():
    data = request.form.to_dict()

    # Save student data to JSON file
    if os.path.exists(DATA_FILE):
        students = json.load(open(DATA_FILE))
    else:
        students = []

    students.append(data)
    json.dump(students, open(DATA_FILE, "w"), indent=4)

    # Generate simple study plan logic (free AI style)
    stream = data.get("stream", "")
    weak = data.get("weak_areas", "")
    goal = data.get("goal", "")
    time = data.get("daily_time", "")

    plan = f"""
    🌱 GrowIQ Personalized Study Plan
    ---------------------------------
    🎯 Goal: {goal}
    📚 Stream / Subjects: {stream}
    🔻 Weak Areas to Improve: {weak}
    ⏳ Daily Study Time: {time} hours

    📌 Weekly Plan:
    - Mon–Wed: Focus on weak subjects for 60% of your time
    - Thu–Fri: Revision + Practice worksheets
    - Sat: Mock test or quiz + analyze mistakes
    - Sun: Rest + Light revision

    ⭐ Strength Strategy:
    Continue practicing strong areas for confidence.
    """

    return render_template("plan.html", data=data, plan=plan)


    if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

