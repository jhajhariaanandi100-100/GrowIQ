from flask import Flask, render_template, request
import json, os

app = Flask(__name__)
DATA_FILE = "students.json"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/form")
def form():
    return render_template("form.html")

@app.route("/generate-plan", methods=["POST"])
def generate_plan():
    data = request.form.to_dict()

    # Save data to JSON
    students = []
    if os.path.exists(DATA_FILE):
        students = json.load(open(DATA_FILE, "r"))
    students.append(data)
    json.dump(students, open(DATA_FILE, "w"), indent=4)

    # Generate study plan message
    plan = f"""
    🌱 GrowIQ Personalized Study Plan

    👤 Name: {data['name']}
    📚 Stream: {data['stream']}
    🎯 Goal: {data['goal']}
    🕒 Daily Study Time: {data['daily_time']} hrs/day
    🧠 Learning Style: {data['learning_style']}
    ❌ Weak Areas: {data['weak_areas']}

    🔥 Weekly Strategy
    - Mon-Wed: Focus on {data['weak_areas']} (60% of study time)
    - Thu-Fri: Concept Revision + Practice Questions
    - Saturday: Mock Test + Mistake Analysis
    - Sunday: Chill + Light Revision (1 hour)
    
    ⭐ Remember: Consistency > Perfection
    """

    return render_template("plan.html", plan=plan, data=data)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
