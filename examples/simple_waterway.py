from pebbleflow import pebble, stream

@pebble
def drop():
    return "💧"

@pebble
def ripple(d):
    return f"{d} ripple"

@stream
def waterway():
    d = drop()
    return ripple(d)

waterway.flow()

