import subprocess

print("🎓 VIT Vellore Campus Assistant (Offline)")
print("Ask me anything about VIT Vellore (type 'exit' to quit)\n")

while True:
    user_input = input("You: ")

    if user_input.lower() in ["exit", "quit"]:
        print("Assistant: Alright, see you around campus 👋")
        break

    prompt = f"""
You are a friendly senior from VIT Vellore.
Guide juniors around campus in simple, casual language.

Question: {user_input}
Answer:
"""

    result = subprocess.run(
        ["ollama", "run", "mistral"],
        input=prompt,
        text=True,
        capture_output=True
    )

    print("Assistant:", result.stdout.strip())
