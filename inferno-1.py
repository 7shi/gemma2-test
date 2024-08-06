import common

messages = [{"role": "user", "content": """
Translate into English with a breakdown:
Nel mezzo del cammin di nostra vita
mi ritrovai per una selva oscura,
ché la diritta via era smarrita.
""".strip()}]

for model in common.models:
    print()
    print("#", model)
    for i in range(3):
        print()
        print("##", i + 1)
        print()
        common.query(model, messages)
