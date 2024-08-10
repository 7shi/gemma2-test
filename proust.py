import common

with open("proust.txt", "r") as f:
    text = f.read().strip()

seed = 12345

models = """
gemma2:2b-instruct-q4_0
gemma2:2b-instruct-q4_K_S
gemma2:2b-instruct-q4_K_M
gemma2:2b-instruct-q8_0
gemma2:9b-instruct-q4_0
gemma2:9b-instruct-q4_K_S
gemma2:9b-instruct-q4_K_M
llama3.1:8b-instruct-q4_0
llama3.1:8b-instruct-q4_K_S
llama3.1:8b-instruct-q4_K_M
mistral-nemo:12b-instruct-2407-q4_0
mistral-nemo:12b-instruct-2407-q4_K_S
mistral-nemo:12b-instruct-2407-q4_K_M
"""[1:-1].split("\n")

messages = [{ "role": "user", "content": "Translate into English:\n" + text }]

print()
common.print_contents(messages)

for model in models:
    print()
    print("##", model)
    print()
    common.query(model, messages, seed=seed)
