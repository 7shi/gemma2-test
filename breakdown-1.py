import common

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

for model in common.models:
    print()
    print("#", model)
    for i in range(3):
        print()
        print("##", i + 1)
        print()
        common.query(model, messages)
