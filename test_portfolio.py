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
    p.buy("IBM", 100, 0)
    p.buy("HYW", 100, 0)
    p.buy("GLZ", 100, 0)
    assert p.cost() == 0