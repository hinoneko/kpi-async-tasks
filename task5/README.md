# Task 5

## Description:

Demonstrates a simple EventEmitter pattern in Python.

## Сode part:

```python
class EventEmitter:
    def __init__(self):
        self.listeners = {}

    def on(self, event, listener):
        if event not in self.listeners:
            self.listeners[event] = []
        self.listeners[event].append(listener)

    def emit(self, event, *args):
        if event in self.listeners:
            for listener in self.listeners[event]:
                listener(*args)


def on_data_received(data):
    print(f"Data received: {data}")


def main():
    emitter = EventEmitter()
    emitter.on("data", on_data_received)
    emitter.emit("data", "Hello, EventEmitter!")

main()
```
