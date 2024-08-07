import common

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

for model in common.models:
    print()
    print("#", model)
    for i in range(3):
        print()
        print("##", i + 1)
        print()
        print("```json")
        result = common.q(model, messages, "json")
        print("```")
        print()
        common.show(*result[1:])
