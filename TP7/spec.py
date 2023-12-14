from fraction import DenominatorNullException


class Fraction:
    """Class representing a fraction and operations on it

    Author : Aurelle Awountsa
    Date : November 2023
    This class allows fraction manipulations through several operations.

    """
    def __init__(self, num, den):
        """This builds a fraction based on some numerator and denominator.

        PRE :  num and den which are real number
        POST : Returns the reduced form of the fraction if den !=0
        Raise : Exception if den = 0
        """
        pass

    @property
    def numerator(self):
        pass

    @property
    def denominator(self):
        pass

    # ------------------ Textual representations ------------------

    def __str__(self):
        """Return a textual representation of the reduced form of the fraction

        PRE : receive a Fraction Object
        POST : returns a textual representation of the reduced from the fraction
        """
        pass

    def as_mixed_number(self):
        """Return a textual representation of the reduced form of the fraction as a mixed number

        A mixed number is the sum of an integer and a proper fraction

        PRE : a Fraction object is a reduced form of a fraction
        POST : returns the mixed number of the fraction
        """
        pass

    # ------------------ Operators overloading ------------------

    def __add__(self, other):
        """Overloading of the + operator for fractions

         PRE : Receive two (numerator and denominator) object of Fraction class
         POST : Return an object Fraction which is Fraction 1 + Fraction 2
         """
        pass

    def __sub__(self, other):
        """Overloading of the - operator for fractions

        PRE : Receive two (numerator and denominator) object of Fraction class
        POST :  Return an object Fraction which is (Fraction 1 - Fraction 2)
        """
        pass

    def __mul__(self, other):
        """Overloading of the * operator for fractions

        PRE : Receive two object from Fraction class
        POST : Return an object Fraction which is the reduced form of (Fraction 1 * Fraction 2)
        """
        pass

    def __truediv__(self, other):
        """Overloading of the / operator for fractions

        PRE : Receive two object from Fraction class
        POST : Return an object Fraction which is the reduced form of (Fraction 1 / Fraction 2)
        """
        pass

    def __pow__(self, other):
        """Overloading of the ** operator for fractions

        PRE : Receive two instances of the Fraction class
        POST : Return the reduced form of (Fraction 1 ** Fraction 2 )
        """
        pass

    def __eq__(self, other):
        """Overloading of the == operator for fractions

        PRE : Receive two instances of the Fraction class
        POST : Return True if (Fraction1 = Fraction2)

        """

    def __float__(self):
        """Returns the decimal value of the fraction

        PRE : Receive one instances of the Fraction class
        POST : Return decimal value of an object Fraction
        """
        pass

    # TODO : [BONUS] You can overload other operators if you wish (ex : <, >, ...)

    # ------------------ Properties checking ------------------

    def is_zero(self):
        """Check if a fraction's value is 0

                   PRE : receive an object from Fraction class
                   POST : returns True if numerator=0 and False if not

        """
        pass

    def is_integer(self):
        """Check if a fraction is integer (ex : 8/4, 3, 2/2, ...)

            PRE : Receive an object of the Fraction class
            POST : Return a boolean. True if the object is an integer and False if not
        """
        pass

    def is_proper(self):
        """Check if the absolute value of the fraction is < 1

             PRE : Receive an object of the Fraction class
             POST : Return a boolean. True if the absolute value of the fraction is < 1 and False if not.

         """
    def is_unit(self):
        """Check if a fraction's numerator is 1 in its reduced form

                PRE : Receive an object of the Fraction class
                POST : Return a boolean. True if the fraction's numerator is 1 in its reduced form and False if not
        """
        pass

    def is_adjacent_to(self, other):
        """Check if two fractions differ by a unit fraction

           Two fractions are adjacent if the absolute value of the difference them is a unit fraction

           PRE : Receive two objects of Fraction class
           POST : Return True if numerator(|Fraction 1 - Fraction 2|) == 1
           """
        pass

