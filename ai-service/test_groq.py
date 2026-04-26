from services.groq_client import call_groq

result = call_groq("Give 2 advantages of AI")

print("AI RESPONSE:")
print(result)