import enum

class BugStatus(enum.Enum):
    new = 7
    incomplete = 6
    invalid = 5
    wont_fix = 4
    in_progress = 3
    fix_committed = 2
    fix_released = 1

print('Member name: {}'.format(BugStatus.wont_fix.name))
print('Member value: {}'.format(BugStatus.wont_fix.value))

print('Member name: {}'.format(BugStatus.in_progress.name))
print('Member value: {}'.format(BugStatus.in_progress.value))

#enum iterate
#not orderred
for status in BugStatus:
    print('{:15} = {}'.format(status.name,status.value))

# Creating enumerations programatically

BugStatus = enum.Enum(
    value='BugStatus',
    names=('fix_released fix_comitted in_progress wont_fix invalid incomplte new'),

)

print('Member: {}'.format(BugStatus.new))

print('\nAll members:')
for status in BugStatus:
    print('{:15} = {}'.format(status.name,status.value))