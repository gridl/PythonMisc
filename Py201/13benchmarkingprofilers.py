#cprofile
#import  cProfile
#cProfile.run("[x for x in range(1500)]")

#line_profile
# profile the time each individual line takes to execute

import time
@profile
def fast_function():
    print("Im a fast function")

@profile
def slow_function():
    time.sleep(2)
    print("Im a slow function")

if __name__ == '__main__':
    fast_function()
    slow_function()

# Run as kernprof -l -v 13benchmarkingprofilers.py