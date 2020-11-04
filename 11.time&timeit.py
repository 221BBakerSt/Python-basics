import time
import timeit

print("The time taken is", timeit.timeit(stmt="a=10; b=10; sum=a+b"), "s")

import_module = "import random"
testcode = """ 
def test(): 
    return random.randint(1, 10)
"""
# get a list of 10 elements, each of which is time of an execution
exec_time_list = timeit.repeat(stmt=testcode, setup=import_module, repeat=10)
print("The average exec time is", sum(exec_time_list)/len(exec_time_list), "s")

start_time = timeit.default_timer()
# put a target program here, when the process finishes, exec_time = end_time - start_time
end_time = timeit.default_timer()

start_time = time.perf_counter()
# put a target program here, when the process finishes, exec_time = end_time - start_time
end_time = time.perf_counter()

# check exec_time with command line:
# python3 -m timeit -n 20000 -s "import time" "a piece of target code"
# output: 20000 loops, best of 5: 156 nsec per loop
