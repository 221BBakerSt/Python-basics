a = [11,22,33]
b = [11,22,33]
print(b == a) # "==" -- value/equality comparison, do they have the same value?
print(b is a) # "is" -- memory address/identity comparison, do they share the same block of memory?
print(id(a), id(b)) # they point to different blocks of memory
# "==": we both use the same phone. "is": but one belongs to you, the other belongs to me, they are different

m = (11,22,33)
n = (11,22,33)
print(n == m)
print(n is m)
print(id(m), id(n)) # they have the same memory address this time, because tuples are immutable
print("-------------------------\n")

c = a
print(id(a), id(c))
print(a is c)
# This is shallow copy, only copy the address, pointing to the same block of memory, not copy the value.
# If a is modified, c is modified along:
a.append(44)
print(c)
# If c is modified, a is modified along:
c.pop()
print(a)
print("---------shallow copy above----------\n")

import copy
d = copy.deepcopy(a)
print(id(d), d)
print(id(a), a)
# This is deep copy. It exploits a new block of memory and put the content into the memory, so the variable points to the new memory address.
print("-------------------------")

a.append(44)
print(id(a), a)
print(id(c), c)
print(id(d), d)
# a is modified, c is modified along but d remains unmodified.
# Shallow copy simply means pointing to the same block of memory.Deep copy copies the substantial content/value.
print("----------deep coy above---------\n")

x = [11,22]
import copy
y = copy.copy(x)
print(y)
print(id(x))
print(id(y))
print(x == y)
print(x is y)
# list is mutable and tuple is immutable, so copy.copy() handles the two types in different ways.
print("---------lists above, tuples below----------")

x = (11,22)
import copy
y = copy.copy(x)
print(id(x))
print(id(y))
print(x == y)
print(x is y)


# result:
# True
# False
# 4503282144 4503284704
# True
# True
# 4505121648 4505121648
# -------------------------

# 4503282144 4503282144
# True
# [11, 22, 33, 44]
# [11, 22, 33]
# ---------shallow copy above----------

# 4505124448 [11, 22, 33]
# 4503282144 [11, 22, 33]
# -------------------------
# 4503282144 [11, 22, 33, 44]
# 4503282144 [11, 22, 33, 44]
# 4505124448 [11, 22, 33]
# ----------deep coy above---------

# [11, 22]
# 4505014352
# 4505138832
# True
# False
# ---------lists above, tuples below----------
# 4503843056
# 4503843056
# True
# True