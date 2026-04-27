<<<<<<< HEAD
from flask import Flask, request, jsonify
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from middleware import sanitize_input, detect_prompt_injection

app = Flask(__name__)

# Rate limiter
limiter = Limiter(get_remote_address, app=app, default_limits=["30 per minute"])


@app.route("/test", methods=["POST"])
@limiter.limit("30 per minute")
def test():
    data = request.json.get("text", "")

    # sanitize
    clean_text = sanitize_input(data)

    # detect injection
    if detect_prompt_injection(clean_text):
        return jsonify({"error": "Prompt injection detected"}), 400

    return jsonify({"cleaned": clean_text})


if __name__ == "__main__":
    
from flask import Flask, request, jsonify
from middleware import sanitize_input, detect_prompt_injection
from services.groq_client import call_groq
from datetime import datetime

app = Flask(__name__)

@app.route("/generate", methods=["POST"])
def generate():
    data = request.json.get("text", "")

    # 1. Clean input
    clean_text = sanitize_input(data)

    # 2. Check injection
    if detect_prompt_injection(clean_text):
        return jsonify({
            "status": "error",
            "message": "Prompt injection detected"
        }), 400

    # 3. Call AI
    ai_output = call_groq(clean_text)

    # 4. Return structured response
    return jsonify({
        "status": "success",
        "input": clean_text,
        "output": ai_output,
        "timestamp": datetime.utcnow().isoformat()
    })


if __name__ == "__main__":
    app.run(debug=True)