import sys
 
def main(argv):
    print("the file name is:", sys.argv[0])
    # this program receives as many parameters as you want
    # but since we invoke argv[3], it should receive at least 3 variables
    print("the first 3 parameters this program receives are", argv[1], argv[2], argv[3])
    # whatever parameter is passed in, it will be transformed into str type
    print("argument list:", sys.argv)
    print("each parameter you enter is", type(argv[1]))
    
 
if __name__ == "__main__":
    sum = 0
    main(sys.argv)
    # the range skips 0 and starts from 1
    for _ in range(1, len(sys.argv)):
        sum += int(sys.argv[_])
    print("the sum of the parameters you enter is", sum)

# run this in command line: python argument-variable.py  11 22 33

# result:
# the file name is: argument-variable.py
# this program receives 3 parameters, and they are 11 22 33
# argument list: ['argument-variable.py', '11', '22', '33']
# each parameter you enter is <class 'str'>
# the sum of the parameters you enter is 66