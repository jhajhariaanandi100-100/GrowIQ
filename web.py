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

    data = {
        "name": request.form.get("name"),
        "age": request.form.get("age"),
        "email": request.form.get("email"),
        "student_type": request.form.get("student_type"),
        "class_year": request.form.get("class_year"),
        "stream": request.form.get("stream"),
        "level": request.form.get("level"),
        "weak_areas": request.form.get("weak_areas"),
        "strengths": request.form.get("strengths"),
        "goal": request.form.get("goal"),
        "target_date": request.form.get("target_date"),
        "daily_time": request.form.get("daily_time"),
        "learning_style": request.form.get("learning_style"),
        "preferred_time": request.form.get("preferred_time"),
        "attention_span": request.form.get("attention_span"),
        "feedback": request.form.get("feedback"),
        "progress_data": request.form.get("progress_data")
    }

    # Save data to JSON file
    if os.path.exists(DATA_FILE):
        students = json.load(open(DATA_FILE))
    else:
        students = []

    students.append(data)
    json.dump(students, open(DATA_FILE, "w"), indent=4)

    # ---- Personalized Plan Logic ---- #

    stream = data["stream"]
    weak = data["weak_areas"]
    strengths = data["strengths"]
    time = data["daily_time"]
    learning = data["learning_style"]
    goal = data["goal"]
    pref = data["preferred_time"]

    # Plan output text
    plan = f"""
    🌱 GrowIQ Personalized Study Plan
    -------------------------------------------

    👤 Student: {data['name']}
    🎯 Goal: {goal}
    📅 Target Date: {data['target_date']}
    📚 Stream / Subjects: {stream}
    ⏳ Daily Study Time: {time} hours
    📌 Preferred Study Time: {pref}
    🧠 Learning Style: {learning}

    🔻 Weak Areas:
    {weak}

    ⭐ Strengths:
    {strengths}

    --------------------------------------------

    📌 Suggested Weekly Routine:
    • Mon–Wed → Focus on weak areas (70% time)
    • Thu–Fri → Practice + revision
    • Saturday → Mock tests, quiz, practice worksheets
    • Sunday → Rest + light revision + mental health break

    🎯 Special Tips for {learning} Learners:
    {"Use videos, diagrams, and mind maps." if learning == "Visual" else ""}
    {"Record voice notes & listen, group study works best." if learning == "Auditory" else ""}
    {"Learn by doing: practical tasks, exercises, experiments." if learning == "Kinesthetic" else ""}

    --------------------------------------------

    ⭐ Strength Strategy:
    Keep practicing strong areas to build confidence & motivation.

    🚀 Progress Review:
    Check progress every Sunday, update weak areas & adjust plan.

    ❤️ Remember:
    Your growth is not a race. Grow at your pace with GrowIQ!
    """

    return render_template("plan.html", data=data, plan=plan)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
