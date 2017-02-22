import parsedatetime as pdt
from datetime import datetime
cal = pdt.Calendar()
examples = [
    "19 November 1975",
    "19 November 75",
    "19 Nov 75",
    "tomorrow",
    "yesterday",
    "10 minutes from now",
    "the first of January, 2001",
    "3 days ago",
    "in four days' time",
    "two weeks from now",
    "three months ago",
    "2 weeks and 3 days in the future",
]

print('Now: {}'.format(datetime.now().ctime()),end='\n\n')
print('{:40s} {:>30s}'.format('Input', 'Result'))
print('=' * 70)
for e in examples:
    dt, result = cal.parseDT(e)
    print('{:<40s}{:>30}'.format('"' + e + '"', dt.ctime()))
