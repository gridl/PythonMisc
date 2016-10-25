# chain map is a class that allows the ability ot link multiple mappings together such that they end up being a
# single unit

# from collections import ChainMap
# car_parts = {'hood': 500, 'engine':5000, 'front_door':750}
# car_options = {'A/C': 1000, 'Turbo': 2500,'rollbar': 300}
# car_accessories = {'cover': 100, 'hood_ornament':150,'seat_cover':99}
# car_pricing = ChainMap(car_accessories, car_options, car_parts)
# print(car_pricing['hood'])

import argparse
import os
from collections import ChainMap

def main():
    app_defaults = {'username':'admin', 'password':'admin'}
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--username')
    parser.add_argument('-p','--password')
    args = parser.parse_args()
    command_line_arguments = {key:value for key,value in vars(args).items() if value}

    chain = ChainMap(command_line_arguments, os.environ,app_defaults)
    print(chain['username'])

if __name__ == '__main__':
    main()
    os.environ['username'] ='test'
    main()