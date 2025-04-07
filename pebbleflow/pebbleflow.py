class Pebble:
    def __init__(self, fn):
        self.fn = fn

    def __call__(self, *args, **kwargs):
        print(f"[Pebbleflow] Pebble rolling: {self.fn.__name__}")
        return self.fn(*args, **kwargs)


def pebble(fn):
    return Pebble(fn)


class Stream:
    def __init__(self, fn):
        self.fn = fn

    def flow(self, *args, **kwargs):
        print(f"[Pebbleflow] Stream flowing: {self.fn.__name__}")
        return self.fn(*args, **kwargs)


def stream(fn):
    return Stream(fn)

