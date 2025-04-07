# Pebbleflow
In Pebbleflow, every task is a **pebble** -- small, self-contained, and full or potential.
But without a stream, pebbles scatter.
**Pebbleflow** lets you define that stream -- a flowing path that guides pebbles in harmony, from start to finish.

It's not a pipeline
It's a riverbed you carve.

```python
from pebbleflow import pebble, stream


@pebble
def drop():
    return "water"


@pebble
def ripple(d):
    return f"{d} ripple"


@stream
def waterway():
    d = drop()
    return ripple(d)


waterway.flow()
```

