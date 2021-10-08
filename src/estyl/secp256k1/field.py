P = 2 ** 256 - 2 ** 32 - 977


class Element:
    def __init__(self, val: int):
        if val < 0 or val >= P:
            raise ValueError('{} should be between 0 and {}'.format(val, P - 1))
        self.val = val

    def __repr__(self) -> str:
        return 'Element({:064x})'.format(self.val)

    def __eq__(self, rhs: object) -> bool:
        if not isinstance(rhs, Element):
            return NotImplemented
        return rhs.val == self.val

    def __ne__(self, rhs: object) -> bool:
        if not isinstance(rhs, Element):
            return NotImplemented
        return not (rhs == self)

    def __add__(self, rhs: 'Element') -> 'Element':
        val = (self.val + rhs.val) % P
        return self.__class__(val)

    def __sub__(self, rhs: 'Element') -> 'Element':
        val = (self.val - rhs.val) % P
        return self.__class__(val)

    def __mul__(self, rhs: 'Element') -> 'Element':
        val = (self.val * rhs.val) % P
        return self.__class__(val)

    def __pow__(self, exp: int) -> 'Element':
        n = exp % (P - 1)
        val = pow(self.val, n, P)
        return self.__class__(val)

    def __truediv__(self, rhs: 'Element') -> 'Element':
        val = (self.val * pow(rhs.val, P - 2, P)) % P
        return self.__class__(val)

    def __rmul__(self, coef: int) -> 'Element':
        val = (coef * self.val) % P
        return self.__class__(val)

    def is_zero(self) -> bool:
        return self.val == 0
