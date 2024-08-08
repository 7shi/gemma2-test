import common

inferno1 = [line[4:] for line in """
  1 Nel mezzo del cammin di nostra vita
  2 mi ritrovai per una selva oscura,
  3 ché la diritta via era smarrita.
  4 Ahi quanto a dir qual era è cosa dura
  5 esta selva selvaggia e aspra e forte
  6 che nel pensier rinova la paura!
  7 Tant’ è amara che poco è più morte;
  8 ma per trattar del ben ch’i’ vi trovai,
  9 dirò de l’altre cose ch’i’ v’ho scorte.
 10 Io non so ben ridir com’ i’ v’intrai,
 11 tant’ era pien di sonno a quel punto
 12 che la verace via abbandonai.
 13 Ma poi ch’i’ fui al piè d’un colle giunto,
 14 là dove terminava quella valle
 15 che m’avea di paura il cor compunto,
 16 guardai in alto e vidi le sue spalle
 17 vestite già de’ raggi del pianeta
 18 che mena dritto altrui per ogne calle.
 19 Allor fu la paura un poco queta,
 20 che nel lago del cor m’era durata
 21 la notte ch’i’ passai con tanta pieta.
 22 E come quei che con lena affannata,
 23 uscito fuor del pelago a la riva,
 24 si volge a l’acqua perigliosa e guata,
 25 così l’animo mio, ch’ancor fuggiva,
 26 si volse a retro a rimirar lo passo
 27 che non lasciò già mai persona viva.
 28 Poi ch’èi posato un poco il corpo lasso,
 29 ripresi via per la piaggia diserta,
 30 sì che ’l piè fermo sempre era ’l più basso.
 31 Ed ecco, quasi al cominciar de l’erta,
 32 una lonza leggera e presta molto,
 33 che di pel macolato era coverta;
 34 e non mi si partia dinanzi al volto,
 35 anzi ’mpediva tanto il mio cammino,
 36 ch’i’ fui per ritornar più volte vòlto.
"""[1:-1].split("\n")]

prompt = "Translate into English with a breakdown:\n"

messages = [
    { "role": "user", "content": prompt + "\n".join(inferno1[:3]) },
    { "role": "assistant", "content": """
**English translation:**

```
In the middle of the journey of our life
I found myself within a dark forest,
because the straight way was lost.
```

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

for lnum in range(1):
#for lnum in range(0, len(inferno1), 3):
    print()
    print("#", lnum + 1)
    print()
    lines = "\n".join(inferno1[lnum:lnum+3])
    print("```")
    print(lines)
    print("```")
    messages[-1]["content"] = prompt + lines
    for model in common.models:
        print()
        print("##", model)
        print()
        common.query(model, messages, seed=next(seeds))
