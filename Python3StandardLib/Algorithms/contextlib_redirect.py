from contextlib import redirect_stderr, redirect_stdout
import io
import sys

def misbehaving_function(a):
    sys.stdout.write('(stdout) A: {!r}\n'.format(a))
    sys.stderr.write('(stderr) A: {!r} \n'.format(a))

capture = io.StringIO()
with redirect_stdout(capture), redirect_stderr(capture):
    misbehaving_function(5)

print(capture.getvalue())

#misbehaving fucntions write to both stdout and stderr but the two context managers send that output to the same io.string instance where it is saved to be used later