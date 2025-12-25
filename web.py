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

    # Save data
    students = []
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            students = json.load(f)

    students.append(data)
    with open(DATA_FILE, "w") as f:
        json.dump(students, f, indent=4)

    plan = {
        "name": data["name"],
        "goal": data["goal"],
        "daily_time": data["daily_time"],
        "weak": data["weak_areas"],
        "learning": data["learning_style"]
    }

    return render_template("plan.html", plan=plan)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
