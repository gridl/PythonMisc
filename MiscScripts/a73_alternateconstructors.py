class Date(object):
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def from_string(cls,s): # cls is class i.e Date
        parts = s.split('-')
        return cls(int(parts[0]), int(parts[1]), int(parts[2])) # cls is Date(year,month,data)


    @classmethod
    def today(cls):
        import time
        t = time.localtime()
        return cls(t.tm_year, t.tm_mon, t.tm_mday)



e = Date(2016,6,11)
print(e.year)
d = Date.from_string('2016-06-11')
print(d.year)

f = Date.today()
print(f.year)