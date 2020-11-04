def foo(a, b, *args, **kwargs):
    print("a:", a)
    print("b:", b)
    # args put all non-positional & non-keyword arguments into a tuple
    print("args:", args)
    # kwargs put all keyword arguments into a dict
    print("kwargs:", kwargs)
    print("annotations:", foo.__annotations__)

foo("hello", 0, 1, "world", keyword_arg1=True, keyword_arg2=[1, "happy"])


def bar(a: int, b: "int>0" = 1, c: str = "hello") -> bool:
    """
    a should be an int.
    b should be a postive int and default to be 1.
    c should be a str and default to be "hello".
    the function should return a bool.
    breaking these rules won't cause errors.
    """
    print("a:", a, "b:", b, "c:", c)
    return str(a + b) == c
    

print(bar(-1, 2, "ok"))  # follow the rules
print(bar(b="o", a="hell"))  # break the rules
print(bar(a=23))  # take the default b and c
print("annotations:", bar.__annotations__)


# result:
# a: hello
# b: 0
# args: (1, 'world')
# kwargs: {'keyword_arg1': True, 'keyword_arg2': [1, 'happy']}
# annotations: {}
# -1 2 ok
# False
# hell o hello
# True
# 23 1 hello
# False
# annotations: {'a': <class 'int'>, 'b': 'int>0', 'c': <class 'str'>, 'return': <class 'bool'>}
