import sys
def print_table(objects, colnames,formatter):
    '''make a formatted table showing attributes from a list of objects'''
    formatter.headings(colnames)
    for obj in objects:
        rowdata = [str(getattr(obj, colname)) for colname in colnames]
        formatter.row(rowdata)

class TableFormatter(object):
    def __init__(self, outfile=None):
        if outfile == None:
            outfile = sys.stdout
        self.outfile = outfile
    # serves as a design spec for making tables

    def headings(self,headers):
        raise NotImplementedError

    def row(self, rowdata):
        raise NotImplementedError

class TextTableFormatter(TableFormatter):
    def headings(self,headers):
        for header in headers:
            print('{:>10s}'.format(item), end=' ', file=self.outfile)
        print(file=self.outfile)


    def row(self,rowdata):
        for item in rowdata:
            print('{:>10s'.format(item), end=' ', file=self.outfile)
        print(file=self.outfile)

class CSVTableFormatter(TableFormatter):
    def headings(self,headers):
        print(','.join(headers))

    def row(self,rowdata):
        print(','.join(rowdata))

class QuotedMixin(object):
    def row(self,rowdata):
        quoted = ['"{}"'.format(d) for d in rowdata]
        super.row(quoted)