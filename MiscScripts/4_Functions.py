import csv
def portfolio_cost(filename, *, errors='warn'):

    if errors not in {'warn','silent','raise'}:
        raise ValueError("error must be one of 'warn','silent','raise'")
    total = 0.0
    with open(filename, 'r') as f:
        rows = csv.reader(f)
        headers = next(rows)
        rowno = 0
        for rowno, row in enumerate(rows, start=1):
            try:
                row[2] = int(row[2])
                row[3] = float(row[3])

            except ValueError as err:
                if errors == 'warn':
                print("Row: ", rowno, 'Bad row: ', row)
                print('Row: ', rowno, 'Reason:', err)
                continue
            total += row[2] * row[3]
    return total

total = portfolio_cost('portfolio.csv', errors='ignore')
print('Total Cost: ' , total)