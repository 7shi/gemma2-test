import ollama, random, os, sys
from datetime import timedelta

models = """
gemma2:2b-instruct-q8_0
gemma2:9b-instruct-q4_K_M
llama3.1:8b-instruct-q4_K_M
mistral-nemo:12b-instruct-2407-q4_K_M
""".strip().split("\n")

def split(s):
    ret = []
    while (i := s.find("\n")) >= 0:
        if i:
            ret.append(s[:i])
        ret.append(s[i])
        s = s[i+1:]
    if s:
        ret.append(s)
    return ret

def stream(model, messages, format="", seed=None):
    if seed is None:
        seed = random.randint(0, 2**30)
    text = ""
    prev = ""
    lines = ""
    chunks = []
    stream = ollama.chat(
            model=model,
            messages=messages,
            stream=True,
            format=format,
            options={"seed": seed})
    for chunk in stream:
        chunks.append(chunk)
        content = chunk["message"]["content"]
        text += content
        t = ""
        for ch in split(content):
            if ch == "\n" and prev == "\n":
                lines += ch
            else:
                if lines:
                    t += lines
                    lines = ""
                t += ch
            prev = ch
        if t:
            print(t, end="", flush=True)
    if prev != "\n":
        print()
    chunk["seed"] = seed
    return text, chunks

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

def read_seeds(filename):
    import re
    with open(filename, "r") as f:
        return [int(m) for m in re.findall(r"seed=(\d+)", f.read())]

def print_contents(messages):
    for i, m in enumerate(messages):
        if i:
            print()
        if m["role"] == "user":
            print("```")
        print(m["content"])
        if m["role"] == "user":
            print("```")
        elif i < len(messages) - 1:
            print()
            print("----")

def filename(path):
    return os.path.splitext(path)[0]

class Tee:
    def __init__(self, filename=None):
        self.file = open(filename, "w") if filename else None
        self._stdout = sys.stdout

    def write(self, obj):
        if self.file:
            self.file.write(obj)
        self._stdout.write(obj)

    def flush(self):
        if self.file:
            self.file.flush()
        self._stdout.flush()

    def close(self):
        if self.file:
            self.file.close()

    def __enter__(self):
        sys.stdout = self
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        sys.stdout = self._stdout
        self.close()
