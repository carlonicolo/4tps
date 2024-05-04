import source.esercitazionePytest as ex
import pytest

def test_mult():
    assert ex.mult(6, 5) == 30
    assert ex.mult(0, 5) == -1
    assert ex.mult(-8, -5) == 40
    
    
def test_computeAreaQuadrato():
    assert ex.computeAreaQuadrato(5) == 25
    assert ex.computeAreaQuadrato(6) == 36
    assert ex.computeAreaQuadrato(8) == 64
    
    
