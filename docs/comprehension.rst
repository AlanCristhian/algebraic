comprehension module
====================

A generator expression have the following parts:

.. code-block::

              varnames                                  constraints
               ┌─┴──┐                                 ┌──────┴───────┐
   ((x, y) for (x, y) in zip(iterable1, iterable2) if x > 0 and y == 0)
    └──┬─┘               └──────────┬────────────┘
    member                       domain

.. function:: get_member(generator: Generator[Any, Any, Any]) -> Callable[[Any], Any]

   Returns a function whose body is the *member* of the ``generator`` argument.
