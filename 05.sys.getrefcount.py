import sys

class X:
    pass

a = X()
b = a

print(a)
print(b)
print(a is b)
print(a == b)
# how many references pointing to the same block of memory as variable a
print(sys.getrefcount(a))
"""
the result is 3, not 2, because X() itself also points there.
class X requested a block of memory from OS, a, as an instance object of the class object,
points to that block of memory. Since b=a, b also points to the same memory.
Each pointer is a hard link pointing to the same block of memory.
"""
del a
# if a is deleted, how many references pointing to the same block of memory as variable b
print(sys.getrefcount(b))


# result:
# <__main__.X object at 0x100cc2850>
# <__main__.X object at 0x100cc2850>
# True
# True
# 3
# 2