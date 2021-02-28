import inspect
from typing import Callable
from python_polymorphism.lib.types import PolyFunc, PolyMethodArgumentsException

class Poly():
    def __init__(self) -> None:
        self.functions = {}

    def get_default_args(_, func):
        signature = inspect.signature(func)
        return {
            k: v.default
            for k, v in signature.parameters.items()
            if v.default is not inspect.Parameter.empty
        }

    def poly_wrapper(self, fn: Callable):
        args = fn.__code__.co_varnames
        default_args = self.get_default_args(fn)

        arg_list = []

        for arg in args:
            if not arg == 'self' and arg not in default_args.keys():
                arg_list.append(arg)

        name_args = '_'.join(arg_list)

        self.functions[fn.__name__] = self.functions.get(fn.__name__) or {}
        self.functions[fn.__name__][name_args] = PolyFunc(fn, default_args)

        def get_target(that, **kwargs):
            name = '_'.join(kwargs.keys())

            if name not in self.functions[fn.__name__].keys():
                raise PolyMethodArgumentsException(fn.__name__, kwargs.keys())

            target: PolyFunc = self.functions[fn.__name__][name]

            kwargs.update(target.default)
            return target.call(that, **kwargs)
        
        return get_target

    def this(self):
        return self.poly_wrapper
