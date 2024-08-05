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
Translate into French with a breakdown and output in JSON:
The world is full of beauty.
""".strip()
  },
  {
    "role": "assistant",
    "content": """
```json
{
  "en": "The world is full of beauty.",
  "fr": "Le monde est plein de beauté.",
  "breakdown": [
    { "fr": "Le", "meaning": "the", "lemma": "le", "part": "indefinite article", "description": "masculine singular" },
    { "fr": "monde", "meaning": "world", "lemma": "monde", "part": "noun", "description": "masculine singular" },
    { "fr": "est", "meaning": "is", "lemma": "être", "part": "verb", "description": "third person singular present indicative" },
    { "fr": "plein", "meaning": "full", "lemma": "plein", "part": "adjective", "description": "masculine singular" },
    { "fr": "de", "meaning": "of", "lemma": "de", "part": "preposition", "description": "" },
    { "fr": "beauté", "meaning": "beauty", "lemma": "beauté", "part": "noun", "description": "feminine singular" }
  ]
}
```
""".strip()
  },
  {
    "role": "user",
    "content": """
Translate into French with a breakdown and output in JSON:
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
