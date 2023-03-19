try:
    print(1 / 0)
except Exception as e:
    print("You can't divide by zero, you're silly.")

try:
    print(1 / 0)
except ZeroDivisionError:
    print("You can't divide by zero, you're silly.")

import sys

try:
    number = int(input("Enter a numbers Only"))
except ValueError:
    print("sorry.. numbers only")
    sys.exit()
print("you entered number", number)


def this_fails():
    x = 1 / 0


try:
    this_fails()
except ZeroDivisionError as detail:
    print('Handling run-time error:', detail)

try:
    a = 10 / 0
    print(a)
except ArithmeticError:
    print("This statement is raising an exception")
else:
    print("Welcome")

try:
    f = open("1.txt", 'r')
except IOError:
    print('cannot open')
else:
    print("file has", len(f.readlines()), 'lines')
    f.close()

try:
    import foo
except ImportError as detail:
    print('Handling run-time error:', detail)

try:
    fh = open("testfile", "w")
    fh.write("This is my test file for exception handling!!")
except IOError:
    print("Error: can\'t find file or read data")
else:
    print("Written content in the file successfully")
fh.close()

try:
    raise KeyboardInterrupt
finally:
    print('Goodbye, world!')


class ErrorInCode(Exception):
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return repr(self.data)


try:
    raise ErrorInCode(2000)
except ErrorInCode as ae:
    print("Received error:", ae.data)

x = "hello"

if not type(x) is int:
    raise TypeError("Only integers are allowed")

try:
    a = 10
    print(a)
    raise NameError("Hello")
except NameError as e:
    print("An exception occurred")
    print(e)
