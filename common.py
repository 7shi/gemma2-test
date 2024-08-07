import ollama, random
from datetime import timedelta

models = """
gemma2:2b-instruct-q4_K_M
gemma2:9b-instruct-q4_K_M
llama3.1:8b-instruct-q4_K_M
mistral-nemo:12b-instruct-2407-q4_K_M
""".strip().split()

def stream(model, messages, format="", seed=None):
    if seed is None:
        seed = random.randint(0, 2**30)
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
    chunk["seed"] = seed
    return "".join(chunks), chunks

def show(chunk):
    count = chunk["eval_count"]
    duration = chunk["eval_duration"] / 1e9
    delta = timedelta(seconds=duration)
    tps = count / duration
    seed = chunk["seed"]
    print(f"[count={count}, duration={delta}, tps={tps:.2f}, seed={seed}]")

def query(model, messages, format="", seed=None):
    result = stream(model, messages, format, seed)
    print()
    show(result[1][-1])
    return result
