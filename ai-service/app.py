from flask import Flask, request, jsonify
from middleware import sanitize_input, detect_prompt_injection
from services.groq_client import call_groq

app = Flask(__name__)

@app.route("/generate", methods=["POST"])
def generate():
    data = request.json.get("text", "")

    # 1. Clean input
    clean_text = sanitize_input(data)

    # 2. Check attack
    if detect_prompt_injection(clean_text):
        return jsonify({"error": "Prompt injection detected"}), 400

    # 3. Call AI
    response = call_groq(clean_text)

    # 4. Return result
    return jsonify({
        "input": clean_text,
        "output": response
    })

if __name__ == "__main__":
    app.run(debug=True)