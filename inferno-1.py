import common

messages = [{ "role": "user", "content": """
Translate into English with a breakdown:
Nel mezzo del cammin di nostra vita
mi ritrovai per una selva oscura,
ché la diritta via era smarrita.
""".strip() }]

seeds = iter([
    6349636, 1014400374, 71309843,
    817187924, 697241969, 748567551,
    981832298, 1016541309, 889656337,
    13020530, 1039299909, 235259056,
])

for model in common.models:
    print()
    print("#", model)
    for i in range(3):
        print()
        print("##", i + 1)
        print()
        common.query(model, messages, seed=next(seeds))
