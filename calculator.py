def add(a, b):
    return a + b


def record(value, history=None):
    if history is None:
        history = []
    history.append(value)
    return history


def is_empty(history):
    if history is None:
        return True
    return len(history) == 0
