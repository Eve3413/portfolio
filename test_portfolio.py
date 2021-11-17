import pytest

from portfolio import Portfolio

def test_buy_one_stock():
    p = Portfolio()
    p.buy("IBM", 100, 176.48)
    assert p.cost() == 17648.0


def test_buy_two_stock():
    p = Portfolio()
    p.buy("IBM", 100, 176.48)
    p.buy("HPQ", 100, 36.15)
    assert p.cost() == 21263.0



def test_buy_three_stock():
    p = Portfolio()
    assert p.cost() == 0.0

def test_buy_negative_shares():
    p = Portfolio()
    with pytest.raises(ValueError):
        p.buy("MKFT", -100, 100.0)
    