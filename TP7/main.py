from fraction import ComplexNumberException, DenominatorNullException, Fraction, DivZero, ShoulBeAnInteger


if __name__ == "__main__":
    try:

        f = Fraction(-2, -3)
        f1 = Fraction(-2, -4)
        f2 = Fraction(524, 124.58)
        f3 = Fraction(18, 57.5)
        f4 = Fraction(47.2, -9)
        f5 = Fraction(-1.2, 3.6)
        f6 = Fraction(1, 2)
        f7 = Fraction(10, 23)
        f8 = Fraction(45.35654, 12.4214)
        f9 = Fraction(15.3, 102.8)
        f10 = Fraction(-87, 0)
        f11 = Fraction(17.4, 17.4)

        print(f10)





    except DenominatorNullException as e:
        print(e)
    except DivZero as d:
        print(d)
    except ComplexNumberException as c:
        print(c)
    except ShoulBeAnInteger as s:
        print(s)



