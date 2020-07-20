li = [5, 6, 7, 3, 4, 1, 2, 9, 8]

s_li = sorted(li)

print("Orginal list :\t", li)
print("Sorted list  :\t", s_li)

li.sort()

print("Orginal sorted list :\t", li)

li.sort(reverse=True)

print("Orginal reverse Sorted list :\t", li)


tup = (5, 6, 7, 3, 4, 1, 2, 9, 8)
s_tup = sorted(tup)
print(s_tup)

dict1 = {"name": "ravi", "age": 23, "education": "BTECH"}
print(sorted(dict1))

list4 = [-6, -5, -4, 2, 3, 4]

s_list4 = sorted(list4, key=abs)
print(s_list4)


class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return '({},{},${})'.format(self.name, self.age, self.salary)


def e_sort(emp):
    return emp.salary


e1 = Employee("ravi", 24, 50000)
e2 = Employee("sai", 22, 30000)
e3 = Employee("vijay", 20, 80000)

employees = [e1, e2, e3]

s_employees = sorted(employees, key=e_sort, reverse=True)

print(s_employees)
