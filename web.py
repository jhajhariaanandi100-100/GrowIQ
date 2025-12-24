from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/submit", methods=["POST"])
def submit():
    name = request.form.get("name")
    age = request.form.get("age")
    student_class = request.form.get("class")
    gender = request.form.get("gender")
    difficulty = request.form.get("difficulty")
    interest = request.form.get("interest")

    # SIMPLE STUDY PLAN LOGIC
    study_plan = []

    if interest == "Programming":
        study_plan = [
            "Learn basics of Python",
            "Practice coding 1 hour daily",
            "Build small projects",
            "Solve problems on HackerRank"
        ]
    elif interest == "AI / ML":
        study_plan = [
            "Learn Python fundamentals",
            "Study basic Mathematics",
            "Understand Machine Learning concepts",
            "Practice small ML projects"
        ]
    elif interest == "Web Development":
        study_plan = [
            "Learn HTML & CSS",
            "Learn JavaScript basics",
            "Build simple websites",
            "Learn Flask framework"
        ]
    else:
        study_plan = [
            "Create daily study routine",
            "Revise concepts",
            "Practice questions",
            "Take weekly tests"
        ]

    return render_template(
        "result.html",
        name=name,
        age=age,
        student_class=student_class,
        difficulty=difficulty,
        interest=interest,
        study_plan=study_plan
    )


if __name__ == "__main__":
    app.run(debug=True)
