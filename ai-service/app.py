from flask import Flask, request, jsonify
from middleware import sanitize_input, detect_prompt_injection
from services.groq_client import call_groq
from datetime import datetime

app = Flask(__name__)

@app.route("/report", methods=["POST"])
def generate_report():
    data = request.json.get("topic", "")

    clean_text = sanitize_input(data)

    if detect_prompt_injection(clean_text):
        return jsonify({
            "status": "error",
            "message": "Prompt injection detected"
        }), 400

    # Create structured prompt
    prompt = f"""
    Generate a detailed report on the topic: {clean_text}

    Include:
    - Introduction
    - Key Points
    - Conclusion
    """

    ai_output = call_groq(prompt)

    return jsonify({
        "status": "success",
        "topic": clean_text,
        "report": ai_output
    })
    

if __name__ == "__main__":
    app.run(debug=True)