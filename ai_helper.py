# ai_helper.py
import sys
from gpt4all import GPT4All

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 ai_helper.py \"your question here\"")
        sys.exit(1)

    prompt = " ".join(sys.argv[1:])
    print("🤖 Running GPT4All locally...\n")

    model = GPT4All("models/q4_0-orca-mini-3b.gguf", model_path=".", allow_download=False)

    with model.chat_session() as session:
        response = session.generate(prompt)

    print("\n💡 Response:\n")
    print(response.strip())

if __name__ == "__main__":
    main()
