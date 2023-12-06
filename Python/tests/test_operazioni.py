import source.operazioni as op
import pytest


def test_somma():
    assert op.somma(10, 11) == 21


def test_sottrazione():
    assert op.sottrazione(8, 9) == -1
    

def test_moltiplicazione():
    assert op.moltipicazione(8, 3) == 24


def test_divisione():
    assert op.divisione(4, 2) == 2
