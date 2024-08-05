import ollama

models = """
gemma2:2b-instruct-q4_K_M
gemma2:9b-instruct-q4_K_M
llama3.1:8b-instruct-q4_K_M
llama3:8b-instruct-q4_K_M
mistral-nemo:12b-instruct-2407-q4_K_M
""".strip().split()

messages = [
  {
    "role": "user",
    "content": """
Translate into French with a breakdown:
The world is full of beauty.
""".strip()
  },
  {
    "role": "assistant",
    "content": """
Le monde est plein de beauté.

* Le monde: The world
* est: is
* plein de beauté: full of beauty
""".strip()
  },
  {
    "role": "user",
    "content": """
Translate into French with a breakdown:
Describe your favorite season and explain why you like it.
""".strip()
  }
]

prompt = """
""".strip()

for model in models:
    print("#", model)
    for i in range(3):
        print("##", i + 1)
        response = ollama.chat(model=model, messages=messages)
        print(response["message"]["content"])
