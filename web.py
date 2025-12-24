from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        age = request.form.get("age")
        student_class = request.form.get("class")
        gender = request.form.get("gender")
        difficulty = request.form.get("difficulty")
        interest = request.form.get("interest")

        plan = f"""
        Hello {name},

        Based on your interest in {interest} and difficulty level {difficulty},
        we recommend daily practice, concept learning, and weekly revisions.

        Keep learning with GrowIQ!
        """

        return render_template("index.html", result=plan)

    return render_template("index.html", result=None)


if __name__ == "__main__":
    app.run()
