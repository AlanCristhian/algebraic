# algebraic

Symbolical computation like SymPy.

## API Reference

### constant module

#### class algebraic.Constant()

Base class common to all types defined in the `algebraic.constant` module.

#### class algebraic.constant.Integer(value: Optional[int], /)

Creates an algebraic Integer constant.

```python
>>> fifteen = algebraic.constant.Integer(15)
>>> fifteen
fifteen
>>> fifteen.value
15
```

#### class algebraic.constant.Rational(numerator: Optional[int], denominator: Optional[int], /)

Creates an algebraic Rational constant.

```python
>>> half = algebraic.constant.Rational(1, 2)
>>> half
half
>>> half.value
1/2
```

#### class algebraic.constant.Real(value: Optional[float], /)

Creates an algebraic Real constant.

```python
>>> pi = algebraic.constant.Real(3.14)
>>> pi
pi
>>> pi.value
3.14
```

#### class algebraic.constant.Complex(value: Optional[complex], /)

Creates an algebraic Complex constant.

```python
>>> root = algebraic.constant.Complex(1.0 + 2.0j)
>>> root
root
>>> root.value
1.0 + 2.0j
```
