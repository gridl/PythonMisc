import csv

def read_csv(filename, types, * , errors = 'warn')

    if errors not in {'warn', 'silent','raise'}:
        raise ValueError('errors must be one of warn ,silent, raise')

    records = []
    with open(filename, 'r') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for rowno, row in enumerate(rows, start=1):
            try:
                row = [ func(val) for func,val in zip(types, row)]
            except ValueError as err:
                if errors == 'warn':
                    print('row', rowno, 'bad row', row)
                    print('row', rowno, 'reason: ', err)
                elif errors == 'raise':
                    raise
                else:
                    pass
                continue
            record = dict(zip(headers,row))
            records.append(record)
    return records

    total += holding['shares']*holding['price']

# invoke on file as
# import datatypes
# portfolio = datatypes.read_csv('portfolio.csv', [str,str,int,float])