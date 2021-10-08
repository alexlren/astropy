from astropy.secp256k1.field import Element

CURVE_B = Element(7)

INFINITY = Point(Element(0), Element(0), True)


class Point:
    def __init__(self, x: Element, y: Element, infinity: bool = False):
        self.x = x
        self.y = y
        self.infinity = infinity
        if infinity:
            return
        if y ** 2 != x ** 3 + CURVE_B:
            raise ValueError('Point is not on the curve')

    def __repr__(self) -> str:
        return 'Point({}, {})'.format(self.x, self.y)

    def __eq__(self, rhs: object) -> bool:
        if not isinstance(rhs, Point):
            return NotImplemented
        if self.is_infinity():
            return rhs.is_infinity()
        if rhs.is_infinity():
            return self.is_infinity()
        return self.x == rhs.x and self.y == rhs.y

    def __ne__(self, rhs: object) -> bool:
        if not isinstance(rhs, Point):
            return NotImplemented
        return not (rhs == self)

    def __add__(self, rhs: Point) -> Point:
        if self.is_infinity():
            return rhs

        if rhs.is_infinity():
            return self

        if self.x == rhs.x and self.y != rhs.y:
            return INFINITY

        if self == rhs and self.y.is_zero():
            return INFINITY

        if rhs.x != self.x:
            s = (self.y - rhs.y) / (self.x - rhs.x)
            x3 = s ** 2 - self.x - rhs.x
            y3 = s * (self.x - x3) - self.y
        else:
            s = (3 * self.x ** 2) / (2 * self.y)
            x3 = s ** 2 - 2 * self.x
            y3 = s * (self.x - x3) - self.y
        return self.__class__(x3, y3)

    def __rmul__(self, coefficient: int) -> Point:
        coef = coefficient
        current = self
        result = INFINITY

        while coef:
            if coef & 1:
                result += current
            coef >>= 1
            if coef != 0:
                current += current
        return result

    def is_infinity(self) -> bool:
        return self.infinity
