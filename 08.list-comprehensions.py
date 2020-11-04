# range(1,11) means [1,11) in maths
a = [8 for a in range(1,11)]
print(a)

b = [b for b in range(1,11) if b%2==0]
print(b)

# range(11) means [0,11) in maths
c = (c for c in range(11))
# it's a generator
print(c)

d = [d for d in range(3) for e in range(2)]
print(d)
# the same result as the above
list1 = []
for d in range(3):
    for e in range(2):
        list1.append(d)
print(list1)

f = [(f,g) for f in range(3) for g in range(2)]
# like a combination in maths
print(f)


# result:
# [8, 8, 8, 8, 8, 8, 8, 8, 8, 8]
# [2, 4, 6, 8, 10]
# <generator object <genexpr> at 0x10eb67d50>
# [0, 0, 1, 1, 2, 2]
# [0, 0, 1, 1, 2, 2]
# [(0, 0), (0, 1), (1, 0), (1, 1), (2, 0), (2, 1)]
