class Memento:
    def __init__(self, snapshot): self._snapshot = list(snapshot)
    def get_state(self): return list(self._snapshot)
