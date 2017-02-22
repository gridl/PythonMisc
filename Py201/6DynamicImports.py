import importlib
# create two modules with differnt names such as foo.py and bar.py
def dynamic_import(module):
    return importlib.import_module(module)

def main():
    print(__name__)


if __name__ == '__main__':
    module = dynamic_import('foo')
    module.main()

    module_two = dynamic_import('bar')
    module_two.main()


