import logging

logger = logging.getLogger()


def testfunction():
    logging.info('Running tests')
    logging.warning('This program does nothing')
    return 'This is a test'

if __name__ == '__main__':
    logging.basicConfig(level=logging.WARNING)
    testfunction()


