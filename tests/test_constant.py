import unittest

import algebraic.constant


class IntegerConstantCase(unittest.TestCase):
    def test_instance(self) -> None:
        one = algebraic.constant.Integer()
        self.assertIsInstance(one, algebraic.constant.Integer)
        self.assertIsInstance(one, algebraic.constant.Constant)

    def test_name(self) -> None:
        two = algebraic.constant.Integer()
        self.assertEqual(two.name, "two")

    def test_value(self) -> None:
        three = algebraic.constant.Integer(value=3)
        self.assertEqual(three.value, 3)


class RationalConstantCase(unittest.TestCase):
    def test_instance(self) -> None:
        half = algebraic.constant.Rational()
        self.assertIsInstance(half, algebraic.constant.Rational)
        self.assertIsInstance(half, algebraic.constant.Constant)

    def test_name(self) -> None:
        third = algebraic.constant.Rational()
        self.assertEqual(third.name, "third")

    def test_value(self) -> None:
        fourth = algebraic.constant.Rational(1, 4)
        self.assertEqual(fourth.value, (1, 4))


class RealConstantCase(unittest.TestCase):
    def test_instance(self) -> None:
        alpha = algebraic.constant.Real()
        self.assertIsInstance(alpha, algebraic.constant.Real)
        self.assertIsInstance(alpha, algebraic.constant.Constant)

    def test_name(self) -> None:
        beta = algebraic.constant.Real()
        self.assertEqual(beta.name, "beta")

    def test_value(self) -> None:
        pi = algebraic.constant.Real(3.14)
        self.assertEqual(pi.value, 3.14)


class ComplexConstantCase(unittest.TestCase):
    def test_instance(self) -> None:
        a = algebraic.constant.Complex()
        self.assertIsInstance(a, algebraic.constant.Complex)
        self.assertIsInstance(a, algebraic.constant.Constant)

    def test_name(self) -> None:
        b = algebraic.constant.Complex()
        self.assertEqual(b.name, "b")

    def test_value(self) -> None:
        c = algebraic.constant.Complex(1.0 + 2.0j)
        self.assertEqual(c.value, 1.0 + 2.0j)


if __name__ == "__main__":
    unittest.main()
