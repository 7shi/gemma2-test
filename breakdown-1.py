import common

messages = [{ "role": "user", "content": """
Translate into French with a breakdown:
The world is full of beauty.
""".strip() }]

seeds = iter([
    741216264, 166311031, 278279906,
    371205739, 920345356, 933603107,
    1054064964, 133713482, 1067573600,
    992012649, 527118300, 460533073,
])

for model in common.models:
    print()
    print("#", model)
    for i in range(3):
        print()
        print("##", i + 1)
        print()
        common.query(model, messages, seed=next(seeds))
