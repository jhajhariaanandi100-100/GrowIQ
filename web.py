from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    name = request.form.get("name")
    email = request.form.get("email")
    category = request.form.get("category")  # school or cs
    age = request.form.get("age")
    cls = request.form.get("class")
    interest = request.form.get("interest")
    difficulty = request.form.get("difficulty")

    # ------------------- STUDY PLANS -------------------

    school_plan = f"""
📚 **STUDY PLAN FOR SCHOOL STUDENT**
.-.-.-.-.-.-.-.-..-.-.-.-.-.-.-.-..-.-.-.-.-.-.-.-..-.-.-.-.-.-.-.-.

👤 Name: {name}
🎓 Class: {cls}
❤️ Interest: {interest}

🗓️ Daily Routine
- 6:00 AM • Morning revision (30 min)
- 5:00 PM • Homework + Doubt solving (1 hr)
- 7:00 PM • Subject in focus (Math/Science/Eng) (1.5 hr)
- 9:00 PM • Light revision / Notes preparation (30 min)

🎯 Interest Based Guidance
- Interest: {interest} = Practice & explore related Olympiads + YouTube resources.

🔥 Difficulty Level Tips
- {difficulty.capitalize()} topics: Focus more, ask teachers, use NCERT + reference books.
"""

    cs_plan = f"""
💻 STUDY PLAN FOR COMPUTER SCIENCE STUDENT
.-.-.-.-.-.-.-.-..-.-.-.-.-.-.-.-..-.-.-.-.-.-.-.-..-.-.-.-.-.-.-.-.
👤 Name: {name}
🎓 Age: {age}
❤️ Interest Area: {interest}

🗓️ Daily Routine
- 2 hrs Coding practice (C/Python/Java)
- 45 min DSA concepts + Problem Solving
- 1 hr Development Learning (Web/App/ML)
- 30 min GitHub / Resume Building

🎯 Interest Based Path
- Web Dev → HTML, CSS, JS → React → Backend (Flask/Node)
- AI/ML → Python, Numpy, Pandas, ML Algorithms
- App Dev → Flutter / Kotlin
- Cybersecurity → Networking + Linux + Tools (Nmap, BurpSuite)

🔥 Difficulty Level Tips
- {difficulty.capitalize()} topics: Practice 3 problems/day on Hackerrank / CodeStudio.
"""

    # Logic based on category
    if category == "school":
        plan = school_plan
    else:
        plan = cs_plan

    return render_template("result.html", plan=plan, name=name)


if __name__ == "__main__":
    app.run()

