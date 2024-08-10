import common

fn = common.filename(__file__)
with open(f"{fn}.txt", "r") as f:
    inferno1 = f.read().strip().split("\n")

prompt = "Translate into English with a breakdown:\n"

messages = [
    { "role": "user", "content": prompt + "\n".join(inferno1[:3]) },
    { "role": "assistant", "content": """
**Breakdown:**

* **Nel mezzo del cammin di nostra vita:** In the middle of the journey of our life
    * **Nel mezzo:** In the middle
    * **del cammin:** of the journey
    * **di nostra vita:** of our life
* **mi ritrovai per una selva oscura:** I found myself within a dark forest.
    * **mi ritrovai:**  I found myself
    * **per una selva oscura:** within a dark forest
        * **selva:**  wood, forest
        * **oscura:** dark
* **ché la diritta via era smarrita:** because the straight way was lost.
    * **ché:** because
    * **la diritta via:** the straight way
    * **era smarrita:**  was lost

**English translation:**

```
In the middle of the journey of our life
I found myself within a dark forest,
because the straight way was lost.
```
""".strip() },
    { "role": "user", "content": "" },
]

seeds = iter([
    949578222, 905200098, 291406545, 4779120281,
    606199286, 410169790, 236777461, 1009928125,
    163374333, 812472360, 444193777, 51779628,
    147672688, 998620174, 127694767, 59755225,
    57004965, 23581421, 121497278, 694473296,
    226667986, 709342713, 484421030, 591942197,
    967270761, 800109255, 884346673, 1023645330,
    757134518, 471201462, 304939046, 1035720024,
    580874498, 270509668, 1045651619, 193766689,
    23057904, 1066786363, 993155727, 775490719,
    562012234, 836875994, 507463013, 1018816023,
    165123746, 83518692, 151223161, 197674250,
])

with common.Tee(f"{fn}.md"):
    common.print_contents(messages[:-1])
    for lnum in range(0, len(inferno1), 3):
        print()
        print("#", lnum + 1)
        lines = "\n".join(inferno1[lnum:lnum+3])
        messages[-1]["content"] = prompt + lines
        print()
        common.print_contents(messages[-1:])
        for model in common.models:
            print()
            print("##", model)
            print()
            common.query(model, messages, seed=next(seeds))
