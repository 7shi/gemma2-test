import common

with open("hemingway.txt", "r") as f:
    text = f.read().strip()

seed = 774639974

def query(*prompts):
    for lang, prompt in prompts:
        print()
        print("#", lang)
        messages = [{ "role": "user", "content": prompt + "\n" + text }]
        for model in models:
            print()
            print("##", model)
            print()
            common.query(model, messages, seed=seed)

models = """
gemma2:2b-instruct-q4_0
gemma2:2b-instruct-q4_K_S
gemma2:2b-instruct-q4_K_M
gemma2:2b-instruct-q8_0
gemma2:9b-instruct-q4_0
gemma2:9b-instruct-q4_K_S
gemma2:9b-instruct-q4_K_M
llama3.1:8b-instruct-q4_0
llama3.1:8b-instruct-q4_K_M
llama3.1:8b-instruct-q4_K_S
mistral-nemo:12b-instruct-2407-q4_0
mistral-nemo:12b-instruct-2407-q4_K_M
mistral-nemo:12b-instruct-2407-q4_K_S
"""[1:-1].split("\n")

query(
    ("日本語", "日本語に翻訳してください："),
    ("français", "Traduisez en français:"),
)

models = """
gemma2:2b-instruct-q8_0
gemma2:9b-instruct-q4_K_M
llama3.1:8b-instruct-q4_K_M
mistral-nemo:12b-instruct-2407-q4_K_M
"""[1:-1].split("\n")

query(
    ("日本語", "日本語に翻訳してください："),
    ("Japanese", "Translate into Japanese:"),
    ("japonais", "Traduisez en japonais:"),
    ("フランス語", "フランス語に翻訳してください："),
    ("French", "Translate into French:"),
    ("français", "Traduisez en français:"),
)
