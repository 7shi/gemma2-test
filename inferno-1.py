import ollama

models = """
gemma2:2b-instruct-q4_K_M
gemma2:9b-instruct-q4_K_M
llama3.1:8b-instruct-q4_K_M
llama3:8b-instruct-q4_K_M
mistral-nemo:12b-instruct-2407-q4_K_M
""".strip().split()

prompt = """
Translate into English with a breakdown:
Nel mezzo del cammin di nostra vita
mi ritrovai per una selva oscura,
ché la diritta via era smarrita.
""".strip()

for model in models:
    print("#", model)
    for i in range(3):
        print("##", i + 1)
        print(ollama.generate(model=model, prompt=prompt)["response"])
