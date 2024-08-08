import common

messages = [
    { "role": "user", "content": """
Translate into French with a breakdown:
The world is full of beauty.
"""[1:-1] },
    { "role": "assistant", "content": """
**French Translation:**

Le monde est plein de beauté.

**Breakdown:**

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
    115765205, 60653243, 174840290,
    913415146, 360416609, 814819004,
    416609499, 388350555, 170635955,
    900754601, 233360089, 764294534,
])

for model in common.models:
    print()
    print("#", model)
    for i in range(3):
        print()
        print("##", i + 1)
        print()
        common.query(model, messages, seed=next(seeds))
