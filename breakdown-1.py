import common

messages = [{"role": "user", "content": """
Translate into French with a breakdown:
The world is full of beauty.
""".strip()}]

for model in common.models:
    print()
    print("#", model)
    for i in range(3):
        print()
        print("##", i + 1)
        print()
        common.query(model, messages)
