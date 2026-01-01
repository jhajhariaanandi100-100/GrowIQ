from flask import Flask, render_template, request
import json, os

app = Flask(__name__)
DATA_FILE = "students.json"

def generate_dynamic_plan(data):
    stream = data["stream"]
    weak = data["weak_areas"].lower()
    hours = int(data["daily_time"])
    style = data["learning_style"]

    plan = []

    # STREAM LOGIC
    if stream == "Computer Science / IT":
        plan.append("📘 Core Focus: Programming + Problem Solving")
        if "dsa" in weak or "algorithm" in weak:
            plan.append("🔹 Practice DSA daily using simple problems (arrays, strings)")
        else:
            plan.append("🔹 Focus on basics: C / Python fundamentals")

        plan.append("🛠 Weekly Coding Task: Build 1 small project")

    else:
        plan.append("📘 Core Focus: Concept clarity + revision")
        plan.append(f"🔹 Spend extra time on {data['weak_areas']}")

    # TIME LOGIC
    if hours <= 2:
        plan.append("⏱ Study Strategy: Short focused sessions (Pomodoro)")
    elif hours <= 4:
        plan.append("⏱ Study Strategy: Balanced study + practice")
    else:
        plan.append("⏱ Study Strategy: Deep learning + revision")

    # LEARNING STYLE LOGIC
    if style == "Visual":
        plan.append("🎨 Use diagrams, charts, and videos")
    elif style == "Auditory":
        plan.append("🎧 Learn using explanations and discussion")
    elif style == "Kinesthetic (Hands-on)":
        plan.append("🧪 Learn by doing practical exercises")

    # WEEKLY STRUCTURE
    weekly = """
📅 Weekly Plan
• Mon–Wed: Weak areas + core concepts
• Thu–Fri: Practice & revision
• Saturday: Test + improvement
• Sunday: Light study + rest
"""

    return "\n".join(plan) + weekly


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/form")
def form():
    return render_template("form.html")


@app.route("/generate-plan", methods=["POST"])
def generate_plan():
    data = request.form.to_dict()

    # Save data
    students = []
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            students = json.load(f)
    students.append(data)
    with open(DATA_FILE, "w") as f:
        json.dump(students, f, indent=4)

    plan = generate_dynamic_plan(data)

    return render_template("plan.html", plan=plan, data=data)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)