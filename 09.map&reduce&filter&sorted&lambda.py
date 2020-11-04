# map function abstracts the operation, and visualises the mapping of input and output
def func1(n):
    return n*n
list1 = [1, 2, 3, 4, 5]

v1 = map(func1, list1)
# it is a lazy sequence
print(v1)
# list function outputs the entire iterator sequence
print(list(v1))

# apply str function to every element in list1
v2 = map(str, list1)
print(list(v2))


# realise factorial operation by reduce function
from functools import reduce

def multiply(a, b):
    return a * b

def func2(n):
    list2 = [i for i in range(1, n+1)]
    # reduce function repeatedly operates on two elements in a sequence
    return reduce(multiply, list2)
print(func2(6))

# or apply lambda function to replace multiply above
def func2(n):
    list2 = [i for i in range(1, n+1)]
    # lambda describes a simple function of addition or multiplication
    return reduce(lambda a,b:a*b, list2)
print(func2(6))


# realise factorial operation by recursion
def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)

print(fact(6))


# sorted function
students = {"Don": 75, "Adam": 92, "Bart": 66, "Lisa": 88}
# sorted can sort a sequence directly
print(sorted(students))
# sorted receives a key function to operate a sequence ("key=" can be omitted)
print(sorted(students.items(), key=lambda n: n[0]))
print(sorted(students.items(), key=lambda n: n[1], reverse=True))
# unlike mylist.sort(), the operations above did not change the original list
print(students)

students = [("Don", 75), ("Adam", 92), ("Bart", 66), ("Lisa", 88)]
# this has changed the original list
students.sort(); print(students)


# filter function
list3 = [2, 5, 3, 8, 0]
condition1 = lambda n: n > 4
condition2 = lambda n: n*n < 50
# filter returns an iterator
print(filter(condition1, list3))
# apply list function to output the entire iterator sequence
print(list(filter(condition1, list3)))  
print(list(filter(condition2, list3)))

names = ["", "Amy", "Bob", "", 0, None, {}, "Carl"]
print(list(filter(None, names)))


# result:
# <map object at 0x1071f8a50>
# [1, 4, 9, 16, 25]
# ['1', '2', '3', '4', '5']
# 720
# 720
# 720
# [('Adam', 92), ('Bart', 66), ('Don', 75), ('Lisa', 88)]
# [('Adam', 92), ('Bart', 66), ('Don', 75), ('Lisa', 88)]
# [('Adam', 92), ('Lisa', 88), ('Don', 75), ('Bart', 66)]
# [('Don', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
# [('Adam', 92), ('Bart', 66), ('Don', 75), ('Lisa', 88)]
# <filter object at 0x1071f8f90>
# [5, 8]
# [2, 5, 3, 0]
# ['Amy', 'Bob', 'Carl']
