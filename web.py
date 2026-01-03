from flask import Flask, render_template, request  # Fixed: from is lowercase
import json, os
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

app = Flask(__name__)

# --- 🟢 ZONE 1: AZURE CONFIGURATION ---
AZURE_KEY = os.environ.get("AZURE_KEY") 
AZURE_ENDPOINT = os.environ.get("AZURE_ENDPOINT")

def get_ai_summary(text):
    try:
        if not text or len(text) < 5:
            return "Focus on your goals and keep practicing!"
            
        client = TextAnalyticsClient(AZURE_ENDPOINT, AzureKeyCredential(AZURE_KEY))
        poller = client.begin_abstractive_summary([text])
        result = poller.result()
        
        for doc in result:
            if not doc.is_error:
                return doc.summaries[0].text
    except Exception as e:
        print(f"AI Error: {e}")
    return "Stay consistent and follow your structured path to success."

# --- 🔵 ZONE 2: DYNAMIC PLAN LOGIC ---
def generate_dynamic_plan(data, ai_insight):
    stream = data.get("stream", "General")
    weak = data.get("weak_areas", "").lower()
    hours = int(data.get("daily_time", 4))
    style = data.get("learning_style", "Visual")

    plan = [
        "🌟 AI PROFESSIONAL INSIGHT:",
        ai_insight,
        "------------------------------------------"
    ]

    if "computer" in stream.lower() or "it" in stream.lower():
        plan.append("📘 Core Focus: Programming + Problem Solving")
        if "dsa" in weak or "algorithm" in weak:
            plan.append("🔹 Practice DSA daily using simple problems (arrays, strings)")
        else:
            plan.append("🔹 Focus on basics: C / Python fundamentals")
    else:
        plan.append(f"📘 Core Focus: Concept clarity in {stream}")
        plan.append(f"🔹 Spend extra time on specific topics you mentioned.")

    if hours <= 2:
        plan.append("⏱ Study Strategy: Short focused sessions (Pomodoro)")
    elif hours <= 4:
        plan.append("⏱ Study Strategy: Balanced study + practice")
    else:
        plan.append("⏱ Study Strategy: Deep learning + revision")

    weekly = """
\n📅 Weekly Plan
• Mon–Wed: Weak areas + core concepts
• Thu–Fri: Practice & revision
• Saturday: Test + improvement
• Sunday: Light study + rest
"""
    return "\n".join(plan) + weekly

# --- 🟡 ZONE 3: WEBSITE ROUTES (The Map) ---

@app.route("/")
def home():
    """This route was missing - it shows your index page"""
    return render_template("index.html")

@app.route("/form")
def show_form():
    """This route was missing - it shows your form page"""
    return render_template("form.html")

@app.route("/generate-plan", methods=["POST"])
def generate_plan():
    try:
        data = request.form.to_dict()
        
        if not data.get('weak_areas'):
            return "Please describe your challenges so the AI can help!", 400

        ai_insight = get_ai_summary(data['weak_areas'])
        plan = generate_dynamic_plan(data, ai_insight)

        return render_template("plan.html", plan=plan, data=data)
    except Exception as e:
        print(f"CRITICAL ERROR: {e}")
        return f"System Error: {e}", 500

if __name__ == "__main__":
    app.run(debug=True)