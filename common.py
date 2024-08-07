import ollama, random
from datetime import datetime

models = """
gemma2:2b-instruct-q4_K_M
gemma2:9b-instruct-q4_K_M
llama3.1:8b-instruct-q4_K_M
mistral-nemo:12b-instruct-2407-q4_K_M
""".strip().split()

def stream(model, messages, format="", seed=None):
    if seed is None:
        seed = random.randint(0, 2**30)
    start = datetime.now()
    chunks = []
    line = ""
    stream = ollama.chat(
            model=model,
            messages=messages,
            stream=True,
            format=format,
            options={"seed": seed})
    for chunk in stream:
        content = chunk["message"]["content"]
        print(content, end="", flush=True)
        chunks.append(content)
        line += content
        while (i := line.find("\n")) >= 0:
            line = line[i+1:]
    if chunks and not chunks[-1].endswith("\n"):
        print()
    end = datetime.now()
    count = len(chunks)
    duration = end - start
    tps = count / duration.total_seconds()
    return "".join(chunks), count, duration, tps, seed

def show(count, duration, tps, seed):
    print(f"[count={count}, duration={duration}, tps={tps:.2f}, seed={seed}]")

def query(model, messages, format="", seed=None):
    result = stream(model, messages, format, seed)
    print()
    show(*result[1:])
    return result
