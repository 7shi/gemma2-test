import common

with open("hemingway.txt", "r") as f:
    text = f.read().strip()

seeds = [
    774639974, 605964979, 791356739, 884201550,
    704099149, 660951710, 316156925, 118588328
]

it = iter(seeds)
for lang in ["日本語", "フランス語"]:
    print()
    print("#", lang)
    messages = [{ "role": "user", "content": f"{lang}に翻訳してください：{text}" }]
    for model in common.models:
        print()
        print("##", model)
        print()
        common.query(model, messages, seed=next(it))

it = iter(seeds)
for lang in ["Japanese", "French"]:
    print()
    print("#", lang)
    messages = [{ "role": "user", "content": f"Translate into {lang}:{text}" }]
    for model in common.models:
        print()
        print("##", model)
        print()
        common.query(model, messages, seed=next(it))

it = iter(seeds)
for lang in ["japonais", "français"]:
    print()
    print("#", lang)
    messages = [{ "role": "user", "content": f"Traduisez en {lang}:{text}" }]
    for model in common.models:
        print()
        print("##", model)
        print()
        common.query(model, messages, seed=next(it))
