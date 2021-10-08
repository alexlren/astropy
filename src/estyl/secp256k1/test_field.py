from .field import Element, P


def test_fe_add():
    a = Element(25)
    b = Element(P - 10)
    c = Element(15)

    assert a + b == c


def test_fe_sub():
    a = Element(25)
    b = Element(P - 10)
    c = Element(15)
    assert a == c - b


def test_fe_mul():
    a = Element(25)
    b = Element(6)
    assert a * b == (a + a + a + a + a + a)


def test_fe_pow():
    a = Element(P - 10)
    assert a ** 3 == a * a * a


def test_fe_div():
    a = Element(25)
    b = Element(P - 10)
    assert b * a ** -1 == b / a
