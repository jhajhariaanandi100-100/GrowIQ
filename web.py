from flask import Flask, render_template, request
import json, os
# These are the "Bridge" tools we installed
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

app = Flask(__name__)
DATA_FILE = "students.json"

# --- 🟢 ZONE 1: AZURE CONFIGURATION ---
# We now get these safely from Environment Variables
AZURE_KEY = os.environ.get("AZURE_KEY") 
AZURE_ENDPOINT = os.environ.get("AZURE_ENDPOINT")

def get_ai_summary(text):
    """This function sends your data to the Azure AI you tested in Language Studio"""
    try:
        # Check if user actually typed something
        if not text or len(text) < 5:
            return "Focus on your goals and keep practicing!"
            
        client = TextAnalyticsClient(AZURE_ENDPOINT, AzureKeyCredential(AZURE_KEY))
        
        # We tell the AI to summarize the student's struggle
        poller = client.begin_abstractive_summary([text])
        result = poller.result()
        
        for doc in result:
            if not doc.is_error:
                return doc.summaries[0].text
    except Exception as e:
        print(f"AI Error: {e}")
    
    # Backup message if AI is busy or key is wrong
    return "Stay consistent and follow your structured path to success."

# --- 🔵 ZONE 2: YOUR ORIGINAL LOGIC (UPGRADED) ---
def generate_dynamic_plan(data, ai_insight):
    stream = data["stream"]
    weak = data["weak_areas"].lower()
    hours = int(data["daily_time"])
    style = data["learning_style"]

    # We start the plan with the professional AI Insight
    plan = [
        "🌟 AI PROFESSIONAL INSIGHT:",
        ai_insight,
        "------------------------------------------"
    ]

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

    weekly = """
📅 Weekly Plan
• Mon–Wed: Weak areas + core concepts
• Thu–Fri: Practice & revision
• Saturday: Test + improvement
• Sunday: Light study + rest
"""
    return "\n".join(plan) + weekly


# --- 🟡 ZONE 3: WEBSITE ROUTES ---
@app.route("/generate-plan", methods=["POST"])
def generate_plan():
    try:
        data = request.form.to_dict()
        
        # This prevents the crash if data is missing
        if not data.get('weak_areas'):
            return "Please describe your challenges so the AI can help!", 400

        # Call Azure AI
        ai_insight = get_ai_summary(data['weak_areas'])

        # Generate Plan
        plan = generate_dynamic_plan(data, ai_insight)

        return render_template("plan.html", plan=plan, data=data)
    except Exception as e:
        # This tells you EXACTLY what went wrong in the Render logs
        print(f"CRITICAL ERROR: {e}")
        return f"System Error: {e}", 500