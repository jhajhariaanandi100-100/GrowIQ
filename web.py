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

    if os.path.exists(DATA_FILE):
        with open(DATA_FILE) as f:
            students = json.load(f)
    else:
        students = []

    students.append(data)

    with open(DATA_FILE, "w") as f:
        json.dump(students, f, indent=4)

    plan = f"""
    Goal: {data.get('goal')}
    Stream: {data.get('stream')}
    Weak Areas: {data.get('weak_areas')}
    Daily Time: {data.get('daily_time')} hrs
    """

    return render_template("plan.html", plan=plan)

if __name__ == "__main__":
    app.run()
