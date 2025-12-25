from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    name = request.form['name']
    category = request.form['category']
    stream = request.form['stream']
    interest = request.form['interest']

    plan = []

    # ================= SCHOOL STUDENT =================
    if category == "School Student":

        if stream == "Science":
            if interest == "Medical":
                plan = [
                    "🧬 Biology – 2 hrs (NCERT + diagrams)",
                    "⚗️ Chemistry – 1.5 hrs",
                    "📘 Physics – 1.5 hrs (numericals)",
                    "📅 Weekly: NEET practice questions"
                ]

            elif interest == "Engineering":
                plan = [
                    "📐 Maths – 2 hrs (problem solving)",
                    "⚡ Physics – 1.5 hrs",
                    "⚗️ Chemistry – 1 hr",
                    "💻 Basic coding – 30 mins",
                    "📅 Weekly: JEE mock tests"
                ]

        elif stream == "Commerce":
            if interest == "Business":
                plan = [
                    "📊 Accountancy – 2 hrs",
                    "📈 Economics – 1.5 hrs",
                    "🏢 Business Studies – 1 hr",
                    "🧠 Case studies on weekends"
                ]

        elif stream == "Arts":
            if interest == "Civil Services":
                plan = [
                    "🌍 History & Geography – 2 hrs",
                    "📜 Polity – 1.5 hrs",
                    "📰 Current Affairs – 1 hr",
                    "📝 Answer writing practice"
                ]

    # ================= COMPUTER SCIENCE STUDENT =================
    elif category == "Computer Science Student":

        if stream == "CSE":
            if interest == "Web Development":
                plan = [
                    "🌐 HTML & CSS – 1 hr",
                    "⚙️ JavaScript – 1.5 hrs",
                    "🐍 Python / Flask – 1 hr",
                    "💼 Weekly mini projects"
                ]

            elif interest == "Artificial Intelligence":
                plan = [
                    "📊 Python – 1 hr",
                    "🧠 Machine Learning – 2 hrs",
                    "📐 Maths for AI – 1 hr",
                    "📁 AI mini project weekly"
                ]

            elif interest == "Cyber Security":
                plan = [
                    "🔐 Networking basics – 1 hr",
                    "🖥️ Linux – 1 hr",
                    "🛡️ Cyber tools – 1.5 hrs",
                    "📅 Practice labs weekly"
                ]

        elif stream == "IT":
            if interest == "Data Science":
                plan = [
                    "📊 Python & Pandas – 1.5 hrs",
                    "📈 Statistics – 1 hr",
                    "📉 Data Visualization – 1 hr",
                    "📁 Real datasets practice"
                ]

    return render_template('result.html', name=name, plan=plan)

if __name__ == "__main__":
    app.run(debug=True)