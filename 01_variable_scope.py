"""
This file explains the scope of variables in python

LEGB  : Local , Enclosing , Global , Builtin

NOTE  : If a variable is being accessed in python the order it looks for namespace is Local, Enclosing, Global, Builtin

Keywords : global   - to use global variable instead of worrying about scope
           nonlocal - to use enclosing variable by skipping Local variable



"""

x = "Global X"

print('#' * 50)
print("Global and Local scope")
print('#' * 50)


############################################################################################################################

#   GLOBAL and Local scope

############################################################################################################################

"""
Demonstrating Usage of global variable

"""


def func1():
    print(x)


def dem1():
    print("From dem1")
    func1()


dem1()


"""
Demonstrating Usage of local variable when global variable is present with same name

"""


def func2():
    x = 'local x'
    print(x)


def dem2():
    print("From dem1")
    print(x)
    func2()


dem2()

"""
Demonstrating Usage of global variable instead of local variable with same name

"""


def func3():
    global x
    print(x)


def dem3():
    print("From dem3")
    func3()


dem3()

print('#' * 50)
print("Enclosing")
print('#' * 50)

"""
Demonstrating Enclosing scope
"""


def outerfunc1():
    x = "outer x"

    def innerfunc1():
        x = "inner x"
        print(x)

    innerfunc1()
    print(x)


def dem4():
    outerfunc1()


dem4()


def outerfunc2():
    x = "outer x"

    def innerfunc1():
        nonlocal x
        print(x)

    innerfunc1()
    print(x)


def dem5():
    outerfunc2()


dem5()


"""
Builtin available

if you create any function with same name as builtin function it will access defined function and comes out because
for function also it follows LEGB rule

"""

import builtins
print(dir(builtins))
