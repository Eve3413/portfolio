# Create a file in your repository called portfolio.py by using VSCode from GitHub Desktop, as we did a few weeks ago.

# Within it, define a new class called Portfolio which:

# has a method called buy, which adds a new stock to the portfolio, taking 3 arguments

# name, a str, the symbol of the stock which is being bought

# shares, an int, the quantity which is being bought

# price, a float, the price paid per share

# and has a second method called cost which returns a float, the total cost paid for all stocks in the portfolio

# Consider that to implement the cost method, you'll need to be storing the purchases made each time the buy method is called somewhere. You may do so by any means convenient to you.


class Portfolio:

    def __init__(self):
        self._stocks = []
    
    def buy(self, name, shares, price):
        if shares < 0:
            raise ValueError ("share cannot be negative")
        self._stocks.append((name,shares,price))


    def cost(self):
        return sum(
            shares * price for name, shares, price in self._stocks
        )

     
