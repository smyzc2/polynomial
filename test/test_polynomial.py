from polynomial import Poly

def test_print():
    
    p=Poly((2,1,0,3))

    assert str(p)== "3x^3+x+2"