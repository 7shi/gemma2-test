import common

messages = [
    { "role": "user", "content": """
Translate into French with a breakdown and output in JSON:
The world is full of beauty.
"""[1:-1] },
    { "role": "assistant", "content": """
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
"""[1:-1] },
    { "role": "user", "content": """
Translate into French with a breakdown and output in JSON:
Describe your favorite season and explain why you like it.
"""[1:-1] },
]

seeds = iter([
    262006003, 310331335, 704363529,
    234934443, 929345705, 25910753,
    268805974, 58049255, 21594096,
    541873174, 785152001, 7663002,
])

with common.Tee(common.filename(__file__) + ".md"):
    common.print_contents(messages)
    for model in common.models:
        print()
        print("#", model)
        for i in range(3):
            print()
            print("##", i + 1)
            print()
            print("```json")
            _, chunks = common.stream(model, messages, "json", next(seeds))
            print("```")
            print()
            common.show(chunks[-1])
