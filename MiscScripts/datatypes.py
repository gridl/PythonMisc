def read_portfolio(filename, *, errors='warn'):
    if errors not in {'warn', 'silent','raise'}:
        raise ValueError('errors must be one of warn, silent, raise')

    portfolio = []
    total = 0.0
    with open(filename, 'r') as f:
        rows = csv.reader(f)
        headers = next(rows) # skip the header row
        for rowno, row in enumerate(rows, start =1):
            try:
                row[2] = int(row[2])
                row[3] = flow(row[3])
            except ValueError as err:
                if errors == 'warn':
                    print('Row: ', rowno, 'bad Row', row)
                    print('Row:', rowno, 'Reason:', err)
                elif errors == 'raise':
                    raise # reraises the last exception
                else:
                    pass
                continue
                record = tuple(row)
                portfolio.append(record)
        return portfolio

portfolio = read_portfolio('Data/portfolio.csv', errors= 'silent')
total = 0.0
for name,date,shares, price in portfolio:
    total += shares * price
print('Total cost ', total)
