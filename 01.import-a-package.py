import pack

pack.second.test2() # call test2() function from pack
pack.second.Test2()
print(pack.second.num2)
try:
    pack.first.test1()
except Exception as e:
    print(e)
"""
can't import anything from first.py because __init__.py file doesn't include it
but if use "from ... import ...", it works because it skips __all__ in __init__.py
"""
from pack import first

first.test1()
first.Test1()
print(first.num1)


# result:
# this is function test2 from second.py
# this is class Test2 from second.py
# 20
# module 'pack' has no attribute 'first'
# this is function test1 from first.py
# this is class Test2 from first.py
# 10