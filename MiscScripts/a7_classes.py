class Holding(object):
    # set up method
    def __init__(self, name, date, shares, price):
        self.name = name
        self.date = date
        self.shares = shares
        self.price = price

    def cost(self):
        return self.shares * self.price


    def sell(self,nshares):
        self.shares -= nshares


def read_portfolio(filename):
    portfolio = []
    with open(filename, 'r') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            h = Holding(row[0], row[1], int(row[2]), float(row[2]))
            portfolio.append(h)
    return portfolio




h = Holding('AA', '2016-06-06', 100, 32.2)
print(h.price)