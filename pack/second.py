def test2():
    print("this is function test2 from second.py")

num2 = 20

class Test2(object):
    def __repr__(self):
        print("this is class Test2 from second.py")

    __init__ = __repr__

if __name__ == "__main__":
    test2()
    print(num2)
    Test2()