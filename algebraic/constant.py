from typing import Optional, Tuple

import objname


__all__ = [
    "Constant", "Integer", "Rational", "Real", "Complex",
]


_CONSTANT_REQUIRED_ATTRIBUTES = [
    "name",
    "value",
]


class Constant(objname.AutoName):
    pass


class Integer(Constant):
    def __init__(self, value: Optional[int] = None) -> None:
        super().__init__()  # set the name attribute
        self.value: Optional[int] = value


class Rational(Constant):
    def __init__(
        self,
        numerator: Optional[int] = None,
        denominator: Optional[int] = None,
        /
    ) -> None:
        super().__init__()  # set the name attribute
        self.value: Tuple[Optional[int], Optional[int]] = \
            (numerator, denominator)


class Real(Constant):
    def __init__(self, value: Optional[float] = None, /) -> None:
        super().__init__()  # set the name attribute
        self.value: Optional[float] = value


class Complex(Constant):
    def __init__(self, value: Optional[complex] = None, /) -> None:
        super().__init__()  # set the name attribute
        self.value: Optional[complex] = value
