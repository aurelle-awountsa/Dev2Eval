class ComplexNumberException(Exception):
    pass


class DenominatorNullException(Exception):
    pass


class DivZero(Exception):
    pass


class ShoulBeAnInteger(Exception):
    pass


class Fraction:
    """Class representing a fraction and operations on it

    Author : Aurelle Awountsa
    Date : November 2023
    This class allows fraction manipulations through several operations.

    """

    def __init__(self, num, den):
        """This builds a fraction based on some numerator and denominator.

        PRE :  num and den which are real numbers
        POST : Returns the reduced form of the fraction if den !=0
        Raise : Exception if den = 0 or ShouldbeAndIntegerException if num and den are not real number

        """

        if isinstance(num, complex) or isinstance(den, complex):
            raise ComplexNumberException("Attention!!! Veuillez entrer des nombres réels")

        if isinstance(num, str) or isinstance(den, str):
            raise ShoulBeAnInteger('Attention!!! les numerateurs et denominateurs doivent etre des nombres')

        if den == 0:
            raise DenominatorNullException("Vous avez entrer un dénominateur nul")
        if num == 0:
            self.__num = 0
            self.__den = den
            self.pgcd = 0

        if isinstance(num, float) or isinstance(den, float):

            if num == den:
                self.__num = 1
                self.__den = 1
                self.pgcd = 0
            else:
                self.__num = num
                self.__den = den

        elif num == den:
            self.__num = 1
            self.__den = 1
            self.pgcd = 0
        else:
            x1 = num
            x2 = den
            pgcd = 1
            while True:
                if x1 % x2 == 0:
                    break
                pgcd = x1 % x2
                if pgcd == 1:
                    break
                x1, x2 = x2, pgcd
            self.pgcd = pgcd
            self.__num = int(num / self.pgcd)
            self.__den = int(den / self.pgcd)

    @property
    def numerator(self):
        return self.__num

    @property
    def denominator(self):
        return self.__den

    def __str__(self) -> str:
        """Return a textual representation of the reduced form of the fraction

        PRE : receive a Fraction Object
        POST : returns a textual representation of the reduced from the fraction
        """

        if self.numerator == self.denominator:
            return f"{self.numerator}"
        else:
            return f"{self.numerator}/{self.denominator}"

    def as_mixed_number(self) -> str:
        """Return a textual representation of the reduced form of the fraction as a mixed number

        A mixed number is the sum of an integer and a proper fraction

        PRE : self.numerator/self.denominator is a reduced form of a fraction
        POST : returns the mixed number of the fraction
        """
        if self.numerator == self.denominator:
            return f"{self.numerator}"
        q = self.numerator // self.denominator
        rest = self.numerator % self.denominator
        return f"{q}+({rest}/{self.denominator})"

    def __add__(self, other):

        """Overloading of the + operator for fractions

         PRE : Receive two object of Fraction class
         POST : Return an object Fraction which is Fraction 1 + Fraction 2
         """
        numerator = (self.numerator * other.denominator + self.denominator * other.numerator)
        denominator = (self.denominator * other.denominator)

        return Fraction(numerator, denominator)

    def __sub__(self, other):
        """Overloading of the - operator for fractions

        PRE : Receive two object of Fraction class
        POST :  Return an object Fraction which is (Fraction 1 - Fraction 2)
        """
        numerator = self.numerator * other.denominator - self.denominator * other.numerator
        denominator = self.denominator * other.denominator

        return Fraction(numerator, denominator)

    def __mul__(self, other):
        """Overloading of the * operator for fractions

        PRE : Receive two object from Fraction class
        POST : Return an object Fraction which is the reduced form of (Fraction 1 * Fraction 2)
        """
        numerator = self.numerator * other.numerator
        denominator = self.denominator * other.denominator

        return Fraction(numerator, denominator)

    def __truediv__(self, other):

        """Overloading of the / operator for fractions

        PRE : Receive two object from Fraction class
        POST : Return an object Fraction which is the reduced form of (Fraction 1 / Fraction 2)
        Raise : DivZeroException if num fraction 2 = 0
        """
        """ if other.numerator == 0:
            raise DivZero("Attention! Vous avez rentrer une fraction nulle")
        else:"""
        numerator = self.numerator * other.denominator
        denominator = self.denominator * other.numerator
        return Fraction(numerator, denominator)

    def __pow__(self, other):
        """Overloading of the ** operator for fractions

        PRE : Receive two instances of the Fraction class
        POST : Return the reduced form of (Fraction 1 ** Fraction 2 )
        """
        numerator = (self.numerator ** (other.numerator / other.denominator)).real
        denominator = (self.denominator **
                       (other.numerator / other.denominator)).real
        if numerator < 0 and denominator < 0:
            numerator = -1 * numerator
            denominator = -1 * denominator

        return Fraction(numerator, denominator)

    def __eq__(self, other):
        """Overloading of the == operator for fractions

        PRE : Receive two instances of the Fraction class
        POST : Return True if (Fraction1 = Fraction2)

        """
        if isinstance(other, str):
            return f"{self.numerator}/{self.denominator}" == other
        return self.numerator == other.numerator and self.denominator == other.denominator

        # return Fraction(self.numerator, self.denominator) == Fraction(other.numerator, other.denominator)

    def __float__(self):
        """Returns the decimal value of the fraction

        PRE : Receive one instances of the Fraction class
        POST : Return decimal value of an object Fraction
        """
        return round(self.numerator / self.denominator, 2)

    # TODO : [BONUS] You can overload other operators if you wish (ex : <, >, ...)

    # ------------------ Properties checking ------------------

    def is_zero(self):
        """Check if a fraction's value is 0

        PRE : receive an object from Fraction class
        POST : returns True if numerator=0 and False if not

        """
        return not self.numerator

    def is_integer(self):
        """Check if a fraction is integer (ex : 8/4, 3, 2/2, ...)

        PRE : Receive an object of the Fraction class
        POST : Return a boolean. True if the object is an integer and False if not
        """
        # isinstance(int(self.numerator%self.denominator), int)
        return self.numerator % self.denominator == 0

    def is_proper(self):
        """Check if the absolute value of the fraction is < 1

        PRE : Receive an object of the Fraction class
        POST : Return a boolean. True if the absolute value of the fraction is < 1 and False if not.
        """
        return abs(self.numerator / self.denominator) < 1

    def is_unit(self):
        """Check if a fraction's numerator is 1 in its reduced form

        PRE : Receive an object of the Fraction class
        POST : Return a boolean. True if the fraction's numerator is 1 in its reduced form and False if not
        """
        return abs(self.numerator) == 1

    def is_adjacent_to(self, other):
        """Check if two fractions differ by a unit fraction

        Two fractions are adjacents if the absolute value of the difference them is a unit fraction

        PRE : Receive two ojects of Fraction class
        POST : Return True if numerateur(|Fraction 1 - Fraction 2|) == 1
        """
        return (Fraction(self.numerator, self.denominator) -
                Fraction(other.numerator, other.denominator)).is_unit()
