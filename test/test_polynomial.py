from polynomial import Poly
import pytest

def test_print():
    
    p=Poly((2,1,0,3))

    assert str(p)== "3x^3+x+2"

def test_equility():
    assert Poly((0,1))==Poly((0,1))

@pytest.mark.parametrize(
    "a,b,sum",
    (((0,),(0,1),(0,1)),
    ((2,0,3),(1,2),(3,2,3)),
    ((4,2),(10,2,4),(14,4,4)))
     )

def test_add(a,b,sum):
    assert Poly(a)+Poly(b)==Poly(sum)

def test_add_scalar():
     assert Poly((2,1))+3 == Poly((5,1))

def test_reverse_add_scalar():
     assert 3+Poly((2,1)) == Poly((5,1))

def test_add_unknown():
    with pytest.raises(TypeError):
     Poly((1,))+ "frog"