import csv
import sys

unicode_chars = 'åç'

print(csv.list_dialects())

# read csv
with open(sys.argv[1],'rt') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# write csv
with open(sys.argv[1],'wt') as f:
    writer = csv.writer(f)
    writer.writerow(('Title 1','Title 2', 'Title 3', 'Title 4'))
    for i in range(3):
        row = (
            i + 1,
            chr(ord('a') + i ),
            '08/{:02d}/07'.format(i+1),
            unicode_chars[i]
        )
        writer.writerow(row)

print(open(sys.argv[1],'rt').read())

