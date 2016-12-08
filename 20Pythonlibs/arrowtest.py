import arrow

# current time in your tz
t0 = arrow.now()
print(t0)

# current date and time with UTC attached
t1 = arrow.utcnow()
print(t1)

difference = (t0-t1).total_seconds()
print('Total difference: %.2f seconds' %difference)

#print current date
print(t0.date())


print(t0.humanize())
t0 = t0.replace(hours=3,minutes=10)
print(t0.humanize())

# very cool
print(t0.humanize(locale='hi'))