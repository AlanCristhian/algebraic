"""Split the generator in their furth parts."""

from typing import Callable, Generator, Any
import opcode
import types


# NOTE 1: A generator expression have the following parts:
#
#            varnames                                  constraints
#             ┌─┴──┐                                 ┌──────┴───────┐
# ((x, y) for (x, y) in zip(iterable1, iterable2) if x > 0 and y == 0)
#  └──┬─┘               └──────────┬────────────┘
#  member                        domain

_FOR_ITER = opcode.opmap["FOR_ITER"]
_YIELD_VALUE = opcode.opmap["YIELD_VALUE"]
_RETURN_VALUE = opcode.opmap["RETURN_VALUE"]


def get_member(
    generator: Generator[Any, Any, Any],
) -> Callable[[Any, ...], Any]:
    "Extract the member bytecode (see NOTE 1) and create a function with it."
    gi_code = generator.gi_code
    old_code = gi_code.co_code
    start = old_code.index(_FOR_ITER)
    end = old_code.index(_YIELD_VALUE)
    new_code = bytearray(old_code[start + 2:end - 1])
    new_code.append(_RETURN_VALUE)
    new_code.append(old_code[end + 1])
    new_name = "<member>"
    new_qualname = ".".join(gi_code.co_qualname.split(".")[:-1] + [new_name])

    code_object = types.CodeType(
        gi_code.co_argcount,
        gi_code.co_posonlyargcount,
        gi_code.co_kwonlyargcount,
        gi_code.co_nlocals,
        gi_code.co_stacksize,
        gi_code.co_flags,
        gi_code.co_code,
        gi_code.co_consts,
        gi_code.co_names,
        gi_code.co_varnames,
        gi_code.co_filename,
        new_name,                    # gi_code.co_name
        new_qualname,                # gi_code.co_qualname
        gi_code.co_firstlineno,
        gi_code.co_linetable,
        gi_code.co_exceptiontable,
        gi_code.co_freevars,
        gi_code.co_cellvars
    )

    function = types.FunctionType(
        code_object,                    # CUSTOM: function.__code__
        generator.gi_frame.f_globals,   # CUSTOM: function.__globals__
        generator.__name__,)

    return function
