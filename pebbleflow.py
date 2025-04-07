from functools import wraps


class Task:
    def __init__(self, fn):
        self.fn = fn
        wraps(fn)(self)

    def __call__(self, *args, **kwargs):
        print(f"[Pebbleflow] Running task: {self.fn.__name__}")
        return self.fn(*args, **kwargs)


def task(fn):
    return Task(fn)


class Flow:
    def __init__(self, fn):
        self.fn = fn
        wraps(fn)(self)

    def run(self, *args, **kwargs):
        print(f"[Pebbleflow] Starting flow: {self.fn.__name__}")
        return self.fn(*args, **kwargs)


def flow(fn):
    return Flow(fn)

