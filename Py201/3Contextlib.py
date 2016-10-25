from contextlib import contextmanager, closing, redirect_stdout
from urllib.request import urlopen

@contextmanager # context manger function as decorator which doesnt need to create a class or separate enter and exit
#  methods
def file_open(path):
    try:
        f_obj = open(path, 'w')
        yield f_obj
    except OSError:
        print("We had an error")
    finally:
        print('Closing file')
        f_obj.close()


def closer():
    with closing(urlopen('https://www.google.com')) as webpage: # will cause the handle on the webpage to be closed
        # once we fall out of the with statements code block
        for line in webpage:
            print('Yes')


# contextlib.redirect_stdout/redirect_stderr
def redirector():
    path = '/Users/vsubr2/Projects/PythonMisc/Py201/test.txt'
    with open(path, 'w') as fobj:
        with redirect_stdout(fobj):
            print('Redirecting')
            help(redirect_stdout)

if __name__ == '__main__':
    with file_open('/Users/vsubr2/Projects/PythonMisc/Py201/test.txt') as fobj:
        fobj.write('Testing context managers')

    closer()
    redirector()