import common

with open("proust.txt", "r") as f:
    text = f.read().strip()
messages = [{ "role": "user", "content": "Translate into English:\n" + text }]
seeds = iter([144350804, 627871955, 197720406, 553534933])

for model in common.models:
    print()
    print("#", model)
    print()
    common.query(model, messages, seed=next(seeds))
