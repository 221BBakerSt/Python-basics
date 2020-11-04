def bar():
    try:
        foo()
        print("hello there")

    except (NameError, FileNotFoundError):
        print("if it's one of the two errors above, print this")

    except Exception as e:
        print("if it's not those two errors, this catches any other error")
        print("The error is: " + str(e))
        print(type(e))

    else:
        print("if no error, print this")

    finally:
        print("finally must be executed in the end")


if __name__ == "__main__":
    
    def foo():
        open("xxx.txt", rb)
        11/0
    bar()
    print("-------------------------------")
    
    def foo():
        11/0
        open("xxx.txt", rb)
    bar()
    print("-------------------------------")

    def foo():
        pass
    bar()

# result:
# if it's one of the two errors above, print this
# finally must be executed in the end
# -------------------------------
# if it's not those two errors, this catches any other error
# The error is: division by zero
# <class 'ZeroDivisionError'>
# finally must be executed in the end
# -------------------------------
# hello there
# if no error, print this
# finally must be executed in the end
