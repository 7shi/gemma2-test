import common

messages = [
    { "role": "user", "content": """
Translate into French with a breakdown:
The world is full of beauty.
"""[1:-1] },
    { "role": "assistant", "content": """
Le monde est plein de beauté.

* Le monde: The world
* est: is
* plein de beauté: full of beauty
"""[1:-1] },
    { "role": "user", "content": """
Translate into French with a breakdown:
Describe your favorite season and explain why you like it.
"""[1:-1] },
]

seeds = iter([
    142221657, 879802827, 276362303,
    788133326, 296563742, 731847016,
    64416952, 115269847, 3227022,
    70771379, 122945003, 871140356,
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
            common.query(model, messages, seed=next(seeds))
