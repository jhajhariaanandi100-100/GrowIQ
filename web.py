from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    name = request.form["name"]
    category = request.form["category"]
    interest = request.form["interest"]

    # 📌 STUDY PLANS
    school_plan = {
        "math": ["Algebra - 1 hr", "Geometry - 45 mins", "Practice 15 questions"],
        "science": ["Physics laws (1 hr)", "Chemistry formulas (45 mins)", "Biology revision (30 mins)"],
        "arts": ["History (1 hr)", "Political Science (45 mins)", "Essay writing (30 mins)"],
        "commerce": ["Accountancy basics", "Economics chapter review", "Business Studies summary"]
    }

    engineering_plan = {
        "cse": ["DSA (1 hr)", "Python (1 hr)", "DBMS (45 mins)", "Leetcode practice (30 mins)"],
        "mechanical": ["Thermodynamics", "Machine Design", "Fluid Mechanics"],
        "civil": ["Surveying", "AutoCAD practice", "Structural analysis"],
        "ece": ["Digital electronics", "Microprocessors", "Analog circuits"],
        "eee": ["Power systems", "Control systems", "Circuit theory"]
    }

    # 📌 SELECT PLAN BASED ON CATEGORY
    if category == "school":
        final_plan = school_plan.get(interest, ["Study basics", "Revision", "Practice worksheets"])
    else:
        final_plan = engineering_plan.get(interest, ["General Engineering concepts", "Notes", "Study model papers"])

    return render_template("result.html", name=name, plan=final_plan)

if __name__ == "__main__":
    app.run()
