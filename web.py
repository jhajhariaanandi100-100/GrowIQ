from flask import Flask, render_template, request
import os

app = Flask(__name__)

# Interest options
INTEREST_OPTIONS = [
    "AI",
    "Web Development",
    "Cyber Security",
    "Data Science",
    "App Development"
]

@app.route("/", methods=["GET", "POST"])
def home():
    submitted = False
    plan = ""
    data = {}

    if request.method == "POST":
        submitted = True
        data = {
            "name": request.form.get("name"),
            "email": request.form.get("email"),
            "age": request.form.get("age"),
            "gender": request.form.get("gender"),
            "difficulty": request.form.get("difficulty"),
            "interest": request.form.get("interest")
        }

        interest = data["interest"]
        level = data["difficulty"]

        # Planner logic
        if interest == "AI":
            if level == "Beginner":
                plan = "Learn Python → Math Basics → Intro to AI"
            elif level == "Intermediate":
                plan = "Machine Learning → Data Handling → Mini Projects"
            else:
                plan = "Deep Learning → Neural Networks → AI Research"

        elif interest == "Web Development":
            if level == "Beginner":
                plan = "HTML → CSS → JavaScript Basics"
            else:
                plan = "Flask / React → APIs → Full-Stack Projects"

        elif interest == "Cyber Security":
            plan = "Networking → Linux → Ethical Hacking → Security Tools"

        elif interest == "Data Science":
            plan = "Python → Pandas → Data Visualization → ML Models"

        elif interest == "App Development":
            plan = "Java/Kotlin → Android Basics → App Projects"

        else:
            plan = "Please select a valid interest"

    return render_template(
        "index.html",
        submitted=submitted,
        data=data,
        plan=plan,
        interests=INTEREST_OPTIONS
    )

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
