from typing import Callable

class PolyMethodArgumentsException(Exception):
    def __init__(_, name, args) -> None:
        super().__init__(
            f'The method {name} does not accept the given arguments {args} or some is missing'
        )

class PolyFunc():
    def __init__(self, fn: Callable, default: dict) -> None:
        self.call = fn
        self.default = default
