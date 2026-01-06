import os
from flask import Flask, render_template, request, flash, redirect, url_for
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Needed for flashing error messages

#ZONE 1: AZURE CONFIGURATION:-
# Best Practice: Use environment variables for security
AZURE_KEY = os.environ.get("AZURE_KEY") 
AZURE_ENDPOINT = os.environ.get("AZURE_ENDPOINT")

def get_ai_summary(text):
    """Professional AI extraction with robust error handling."""
    if not AZURE_KEY or not AZURE_ENDPOINT:
        print("Configuration Error: Azure Credentials missing.")
        return "Stay consistent and follow your structured path to success."

    try:
        # Client initialization is cheap, but can be moved outside for high-traffic apps
        client = TextAnalyticsClient(AZURE_ENDPOINT, AzureKeyCredential(AZURE_KEY))
        
        # Using Abstractive Summarization for human-like study advice
        poller = client.begin_abstractive_summary([text])
        result = poller.result()
        
        for doc in result:
            if not doc.is_error and doc.summaries:
                return doc.summaries[0].text
    except Exception as e:
        # Log error internally, but don't crash the user experience
        print(f"Azure AI Logic Error: {e}")
    
    return "Focus on gradual improvement and mastery of core concepts."

#ZONE 2:DYNAMIC PLAN LOGIC:-
def generate_dynamic_plan(data, ai_insight):
    """Constructs a structured, professional-grade study roadmap."""
    stream = data.get("stream", "General Academic")
    weak = data.get("weak_areas", "").lower()
    hours = int(data.get("daily_time", 4))
    
    # Building the plan with a professional 'Report' structure
    plan_blocks = [
        f"🎯 GROWIQ ACADEMIC DIAGNOSTIC",
        f"AI Insight: {ai_insight}",
        "---------------------------------",
        f"Stream: {stream}",
        "Core Objectives:"
    ]

    # Logical Subject Routing
    if any(tech in stream.lower() for tech in ["computer", "it", "software"]):
        plan_blocks.append("• Master Logic: Focus on Programming fundamentals and Algorithmic thinking.")
        if any(w in weak for w in ["dsa", "algorithm", "coding"]):
            plan_blocks.append("• Priority: Daily Data Structures practice (Arrays, Linked Lists).")
    else:
        plan_blocks.append(f"• Deep Dive: Concentrate on theoretical mastery in {stream}.")

    # Time-based Strategy
    if hours <= 2:
        plan_blocks.append("• Efficiency: Utilize the Pomodoro Technique (25m study / 5m break).")
    elif hours <= 5:
        plan_blocks.append("• Balance: 60% Active Recall, 40% Reading/Revision.")
    else:
        plan_blocks.append("• Immersion: Focus on mock tests and peer teaching for advanced mastery.")

    # Standard Professional Footer
    plan_blocks.append("\n📅 WEEKLY MILESTONES")
    plan_blocks.append("1. Mon-Wed: Attack the 'Hard' topics first.\n2. Thu-Fri: Revision and self-testing.\n3. Weekend: Rest and review progress.")

    return "\n".join(plan_blocks)

#ZONE 3:WEBSITE ROUTES:-

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/form")
def show_form():
    return render_template("form.html")

@app.route("/generate-plan", methods=["POST"])
def generate_plan():
    try:
        # Use request.form specifically for safety
        weak_areas = request.form.get('weak_areas', '').strip()
        
        if len(weak_areas) < 10:
            # Better UX: Inform the user they need to provide more detail
            return "Please provide a bit more detail (at least 10 characters) for a better AI plan.", 400

        data = request.form.to_dict()
        ai_insight = get_ai_summary(weak_areas)
        plan = generate_dynamic_plan(data, ai_insight)

        return render_template("plan.html", plan=plan, data=data)
    except Exception as e:
        print(f"Route Error: {e}")
        return "Our AI mentor is taking a short break. Please try again in a moment.", 500

if __name__ == "__main__":
    # In production (Azure/Render), debug should be False
    app.run(debug=True)