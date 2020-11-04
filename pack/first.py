def test1():
    print("this is function test1 from first.py")

num1 = 10

class Test1(object):
    def __init__(self):
        print("this is class Test2 from first.py")

if __name__ == "__main__":
    test1()
    print(num1)
    Test1()