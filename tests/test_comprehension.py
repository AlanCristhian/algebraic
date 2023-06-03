import dis
import unittest

import algebraic.comprehension


class GetMememberSuite(unittest.TestCase):
    def test_single_member(self) -> None:

        def expected(x: int) -> int:
            return x

        obtained = algebraic.comprehension.get_member(x for x in ())
        print("expected")
        print("--------")
        dis.dis(expected)
        print("obtained")
        print("--------")
        dis.dis(obtained)
#         zip_exp_obt = zip(dis.Bytecode(expected), dis.Bytecode(obtained))
#         for i, (exp, obt) in enumerate(zip_exp_obt):
#             with self.subTest(i=i):
#                 self.assertEqual(exp.opname, obt.opname)
#                 self.assertEqual(exp.argval, obt.argval)

#     def test_elaborated_expression_member(self):
#
#         def expected(x, y):
#             return max(x, y)
#
#         obtained = get_member(max(x, y) for x, y in ())
#         zip_exp_obt = zip(dis.Bytecode(expected), dis.Bytecode(obtained))
#         for i, (exp, obt) in enumerate(zip_exp_obt):
#             with self.subTest(i=i):
#                 self.assertEqual(exp.opname, obt.opname)
#                 self.assertEqual(exp.argval, obt.argval)
#
#     def test_name(self):
#         obtained = get_member(x for x in ())
#         self.assertEqual(obtained.__name__, "<member>")


if __name__ == "__main__":
    unittest.main()
