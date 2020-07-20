person = {'name': 'ravi', 'age': 23}

# accessing dictionary using posional
print("My name is {} my age is {}".format(person['name'], person['age']))

# formatting string using index

print("My name is {1} my age is {0}".format(person['age'], person['name']))

# formating string using key in dictonary
print("My name is {0[name]} my age is {0[age]}".format(person))

# acessing list using index
l = ['ravi', 23]
print("My name is {0[0]} my age is {0[1]}".format(l))


class Person():
    """docstring for Person"""

    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person('ravi', 23)

# accessing class instance using .
print("My name is {0.name} my age is {0.age}".format(p1))

# accessing using named variables
print("My name is {name} my age is {age}".format(name='ravi', age=23))


# accessing using unpacking unpacking the dictonary
print("My name is {name} my age is {age}".format(**person))


for i in range(1, 11):
    print("The value of i is :{:}".format(i))

# zero padding the string to 2 digits
for i in range(1, 11):
    print("The value of i is :{:02}".format(i))

# displaying decimal to 2 digits
pi = 3.14159265
print("The value of i is :{:.2f}".format(pi))


# Putting , in number

print("The value of i is :{:,}".format(1000**3))

# Putting , in number and 2 decimal

print("The value of i is :{:,.2f}".format(1000**3))


import datetime

my_date = datetime.datetime(2020, 7, 20, 12, 00, 45)
print("The date is {}".format(my_date))

print("The date is {: %B %d, %Y}".format(my_date))


print("{0:%B %d, %Y} fell on a {0:%A} and was on the {0:%j} day of the year".format(my_date))
