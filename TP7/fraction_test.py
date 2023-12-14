from unittest import TestCase
import unittest
from fraction import ComplexNumberException, DenominatorNullException, Fraction, ShoulBeAnInteger


class TestFraction(TestCase):
    """This class is a test class for the Fraction class.

    Author : Aurelle Awountsa
    Date : Decembre 2023
    """

    # SERT A INSTANCIER LES ATTRIBUTS

    def setUp(self):
        self.fraction1 = Fraction(48, 18)
        self.fraction2 = Fraction(6, 12)
        self.fraction3 = Fraction(-87, -87)

        self.fraction4 = Fraction(45.3, 12.4)
        self.fraction5 = Fraction(15.3, 102.8)
        self.fraction6 = Fraction(17.4, 17.4)

        self.fraction7 = Fraction(524, 124.58)
        self.fraction8 = Fraction(18, 57.5)

        self.fraction9 = Fraction(47.2, -9)
        self.fraction10 = Fraction(-1.2, 3.6)

        self.frac_0 = Fraction(0, 15)
        self.frac_adj = Fraction(1, 4)
        self.frac_adj2 = Fraction(1, 3)

    def test_init(self):
        self.assertEqual(self.fraction1.numerator, 8)
        self.assertEqual(self.fraction1.denominator, 3)
        self.assertEqual(self.fraction9.numerator, 47.2)
        self.assertEqual(self.fraction9.denominator, -9)
        self.assertEqual(self.fraction10.numerator, -1.2)
        self.assertEqual(self.fraction10.denominator, 3.6)

        self.assertRaises(DenominatorNullException, Fraction, 1, 0)
        self.assertRaises(ComplexNumberException, Fraction, complex(2), 5)

    def test_str(self):
        self.assertEqual(self.fraction2.__str__(), "1/2")
        self.assertEqual(self.fraction6.__str__(), f"{self.fraction6.numerator}")

    def test_as_mixed_number(self):
        self.assertEqual(self.fraction1.as_mixed_number(), "2+(2/3)")

    def test_add(self):
        frac_add1 = self.fraction4 + self.fraction5
        frac_add2 = self.fraction1 + self.fraction2
        frac_add3 = self.fraction9 + self.fraction10
        frac_add4 = self.fraction7 + self.fraction8
        self.assertAlmostEqual(frac_add1.numerator, 4846.5599999999995, places=5, msg="Echec Addition : Numerator different")
        self.assertAlmostEqual(frac_add1.denominator, 1274.72, places=5, msg="Echec Addition : Denominator different")
        self.assertEqual(str(frac_add1), "4846.5599999999995/1274.72", "Addition refusé")
        self.assertEqual(str(frac_add2), "19/6", "Addition refusé")
        self.assertEqual(str(frac_add3), "180.72000000000003/-32.4", "Addition refusé")
        self.assertEqual(str(frac_add4), "32372.44/7163.349999999999", "Addition refusé")

    def test_sub(self):
        self.assertEqual(self.fraction1 - self.fraction2, "13/6", "Soustraction impossible")
        self.assertRaises(DenominatorNullException, lambda: self.fraction9 - Fraction(1, 0))

    def test_mul(self):
        frac_mul = self.fraction7 * self.fraction8
        frac = self.frac_0 * self.fraction9

        self.assertEqual(frac.numerator, 0, "Echec Multiplication : Numerateur différent de 0")
        self.assertEqual(frac_mul.numerator, 9432, "Echec Multiplication")
        self.assertEqual(frac_mul.denominator, 7163.349999999999, "Echec Multiplication")
        self.assertEqual(frac_mul, "9432/7163.349999999999", "Multiplication impossible")

    def test_pow(self):
        frac_pow = self.fraction9 ** self.fraction10

        self.assertEqual(frac_pow.numerator, 0.27670648260134734, "Echec Puissance : Numerateur different")
        self.assertEqual(frac_pow.denominator, 0.24037492838456814, "Echec Puissance : denominateur different")
        self.assertEqual(self.fraction9 ** self.fraction10,
                         "0.27670648260134734/0.24037492838456814", "Puissance impossible")

        self.assertRaises(ComplexNumberException, lambda: Fraction(1, complex(8)) ** self.fraction9)

    def test_truediv(self):
        self.assertEqual(self.fraction1 / self.fraction2, "16/3", "Division impossible")
        self.assertEqual(self.fraction9 / self.fraction10, "169.92000000000002/10.799999999999999",
                         "Division impossible")
        self.assertRaises(ComplexNumberException, lambda: Fraction(complex(1), 0) / self.fraction9)
        self.assertRaises(DenominatorNullException, lambda: self.fraction9 / self.frac_0)

    def test_eq(self):
        self.assertEqual(self.fraction3, self.fraction6, "Fraction inégale")
        self.assertEqual(self.frac_0.numerator, 0, "Fraction inégale")

    def test_float(self):
        self.assertEqual(self.fraction5.__float__(),
                         0.15, "Fraction pas un float")

    def test_is_zero(self):
        self.assertTrue(self.frac_0.is_zero(), "Fraction non nulle")
        self.assertFalse(self.fraction9.is_zero(), "Fraction Nulle")

    def test_is_integer(self):
        self.assertTrue(self.fraction6.is_integer(), "Fraction non entiere")
        self.assertFalse(self.fraction8.is_integer(), "Fraction entiere")

    def test_is_proper(self):
        self.assertTrue(self.fraction10.is_proper(), "Fraction supérieur à 1")
        self.assertFalse(self.fraction9.is_proper(), "Fraction inférieur à 1")

    def test_is_unit(self):
        self.assertTrue(self.frac_adj.is_unit(), "Numerateur different de 1")
        self.assertFalse(self.fraction1.is_unit(), "Numerateur egale 1")

    def test_is_adjacent(self):
        self.assertTrue(self.frac_adj.is_adjacent_to(
            self.frac_adj2), "Non Adjacent")
        self.assertFalse(self.fraction9.is_adjacent_to(
            self.fraction9), "Adjacent")


if __name__ == "__main__":
    unittest.main()

    # python -m unittest -v fichierTest
