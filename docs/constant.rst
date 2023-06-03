constant module
===============

.. class:: algebraic.Constant()

   Base class common to all types defined in the ``algebraic.constant`` module.

   .. attribute:: name: str

      The name of the current variable. Is assigned automatically.

.. class:: algebraic.constant.Integer(value: Optional[int], /)

   Creates an algebraic Integer constant.

   .. attribute:: name: str

      The name of the current constant. Is assigned automatically.

   .. attribute:: value: Optional[int]

      The actual value of the constant.

   .. code-block::

      >>> fifteen = algebraic.constant.Integer(15)
      >>> fifteen
      fifteen
      >>> fifteen.value
      15

.. class:: algebraic.constant.Rational(numerator: Optional[int], denominator: Optional[int], /)

   Creates an algebraic Rational constant.

   .. attribute:: name: str

      The name of the current constant. Is assigned automatically.

   .. attribute:: value: Optional[Tuple[int, int]]

      The actual value of the constant.

   .. code-block::

      >>> half = algebraic.constant.Rational(1, 2)
      >>> half
      half
      >>> half.value
      1/2

.. class:: algebraic.constant.Real(value: Optional[float], /)

   Creates an algebraic Real constant.

   .. attribute:: name: str

      The name of the current constant. Is assigned automatically.

   .. attribute:: value: Optional[float]

      The actual value of the constant.

   .. code-block::

      >>> pi = algebraic.constant.Real(3.14)
      >>> pi
      pi
      >>> pi.value
      3.14

.. class:: algebraic.constant.Complex(value: Optional[complex], /)

   Creates an algebraic Complex constant.

   .. attribute:: name: str

      The name of the current constant. Is assigned automatically.

   .. attribute:: value: Optional[complex]

      The actual value of the constant.

   .. code-block::

      >>> root = algebraic.constant.Complex(1.0 + 2.0j)
      >>> root
      root
      >>> root.value
      1.0 + 2.0j
