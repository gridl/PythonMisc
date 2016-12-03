# Neat trick to change logging level on the command line
import logging


def testfunction():
    logging.info('This is info')
    logging.warning('This is a warning')
    logging.debug('This is debug')
    logging.critical('This is critical')
    return 'This is a test'


if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser(description='test parser')
    parser.add_argument('-ll', '--loglevel', type=str, choices=['DEBUG', 'INFO', 'WARNING', 'CRITICAL'],
                        help='Set the logging level')
    args = parser.parse_args()
    logging.basicConfig(level=args.loglevel)
    testfunction()

#ython loggingoncmdline.py -ll CRITICAL
