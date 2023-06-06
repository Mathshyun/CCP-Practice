# Advanced OOP (1): Point Class & Pythagoras Class
class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

class Pythagoras():

    def setPointOne(self, point):
        self.point_one = point
    
    def setPointTwo(self, point):
        self.point_two = point
    
    def getSlope(self):
        return (self.point_two.y - self.point_one.y) / (self.point_two.x - self.point_one.x)
    
    def getDistance(self):
        return ((self.point_two.x - self.point_one.x) ** 2 + (self.point_two.y - self.point_one.y) ** 2) ** 0.5

# Advanced OOP (2): Calculator Class
class Calculator():

    def __init__(self):
        self.num = 0
        self.current = ''
        self.history = []
    
    def add(self, n):
        self.num += n
        if self.current == '':
            self.current = str(n)
        else:
            self.current += ' + %d' % n
    
    def subtract(self, n):
        self.num -= n
        if self.current == '':
            self.current = str(-n)
        else:
            self.current += ' - %d' % n
    
    def multiply(self, n):
        self.num *= n
        self.current += ' * %d' % n

    def equals(self, print_result=False):
        if self.current == '':
            print("No calculation done yet!")
        else:
            if print_result:
                print(self.num)
            self.current += ' = %d' % self.num
            self.history.append(self.current)
            self.num = 0
            self.current = ''

    def show_history(self):
        print("History:")
        for i in self.history:
            print(i)

if __name__ == "__main__":
    test = Calculator()
    test.equals()
    test.show_history()

    test.add(2)
    test.subtract(1)
    test.equals()
    test.show_history()

    test.add(2)
    test.multiply(4)
    test.equals(True)

    test.add(10)
    test.subtract(5)
    test.multiply(2)
    test.equals()

    test.show_history()

# Advanced OOP (3): Account Class
class Account:

    def __init__(self, account_holder):
        self.balance = 0
        self.holder = account_holder
        self.transactions = []
    
    def deposit(self, amount):
        """
        Increase the account balance by amount and return the new balance.
        """
        self.balance = self.balance + amount
        self.transactions.append(('deposit', amount))
    
    def withdrawal(self, amount):
        """
        Decrease the account balance by amount and return the new balance.
        """
        if amount > self.balance:
            return "Insufficient funds"
        self.balance = self.balance - amount
        self.transactions.append(('withdrawal', amount))
    
    def status(self):
        print(self.holder + ": ", end="")
        print(self.transactions)

# Advanced OOP (4): Atom and Molecule
Atno_to_Symbol = {1:'H', 2:'He', 3:'Li', 4:'Be', 5:'B', 6:'C', 7:'N', 8:'O'}
class atom(object):
    def __init__(self,atno,x,y,z):
        self.atno = atno
        self.position = (x,y,z)
    def symbol(self):   # a class method
        return Atno_to_Symbol[self.atno]
    def __repr__(self): # overloads printing
        return '%d %10.4f %10.4f %10.4f' % (self.atno, self.position[0], self.position[1], self.position[2])

'''
instance가 생성될 때
    atno(원자 번호), x, y, z(좌표)를 parameter로 받아 instance variable로 저장한다.

symbol()
    이 원자의 원소 기호를 반환한다.
    원소 기호는 Atno_to_Symbol에 dict type으로 저장되어 원소 번호가 기호에 대응되도록 정의되어 있다.

표현할 때
    "{원자 번호} {x} {y} {z}"의 형태로 표현한다.
    x, y, z 좌표는 각 10칸을 차지하며, 소숫점 아래 4자리까지 표시한다.
'''

class molecule:
    def __init__(self,name='Generic'):
        self.name = name
        self.atomlist = []
    def addatom(self, atom):
        self.atomlist.append(atom)
    def __repr__(self):
        str = 'This is a molecule named %s\n' % self.name
        str = str+'It has %d atoms\n' % len(self.atomlist)
        for atom in self.atomlist:
            str = str + " %s \n" % atom
        return str

'''
instance가 생성될 때
    name(분자 이름)을 parameter로 받아 instance variable로 저장한다.
    name이 입력되지 않은 경우 'Generic'으로 저장한다.
    instance variable atomlist(원자 목록)를 빈 리스트로 생성한다.

addatom()
    atomlist에 입력된 atom을 추가한다.

표현할 때
    첫째 줄에 'This is a molecule named {분자 이름}'
    둘째 줄에 'It has {원자 개수} atoms'(원자 개수는 atomlist의 길이를 사용한다)
    셋째 줄 이하는 atomlist의 각 원자를 표현한다.
    atomlist에는 atom Class instance가 원소로 있어 해당 클래스의 표현 방법을 따른다.
'''

at = atom(6, 0.0, 1.0, 2.0)
print(at)

'''
6     0.0000     1.0000     2.0000
'''

print(at.symbol())

'''
C
'''

mol = molecule('Water')
at = atom(8,0.,0.,0.)
mol.addatom(at)
mol.addatom(atom(1,0.,0.,1.))
mol.addatom(atom(1,0.,1.,0.))
print(mol)

'''
This is a molecule named Water
It has 3 atoms
 8     0.0000     0.0000     0.0000 
 1     0.0000     0.0000     1.0000 
 1     0.0000     1.0000     0.0000 

'''

# Advanced OOP (5): Professor and Student
class Person:
    
    def __init__(self, name, depart):
        self.name = name
        self.depart = depart
    
    def getName(self):
        return self.name
    
    def getDepart(self):
        return self.depart

class Student(Person):
    
    def __init__(self, name, depart, year, credit):
        super().__init__(name, depart)
        self.year = year
        self.credit = credit
    
    def getCredit(self):
        return self.credit
    
    def setCredit(self, credit):
        self.credit = credit
    
    def increaseYear(self):
        self.year += 1

class Professor(Person):
    
    def __init__(self, name, depart, course, salary):
        super().__init__(name, depart)
        self.course = course
        self.salary = salary
    
    def getAnnualSalary(self):
        return self.salary * 12
    
    def raiseSalary(self, percent):
        self.salary *= 1 + percent / 100
        return self.salary

tim_cook = Professor("Tim Cook", "CSE", "Soft. Arch.", 5500)
sum = 0

print("sum of 5 year annual salary: %d" % (tim_cook.getAnnualSalary() * 5))
for i in range(5):
    sum += tim_cook.getAnnualSalary()
    tim_cook.raiseSalary(15)
print("sum of 5 year annual salary with 15%% increase: %.11f" % sum)

# Advanced OOP (6): Staff and Student
class Person:
    
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def getName(self):
        return self.name
    
    def getAddress(self):
        return self.address

class Staff(Person):
    
    def __init__(self, name, address, school, annual_pay):
        super().__init__(name, address)
        self.school = school
        self.annual_pay = annual_pay
    
    def getSchool(self):
        return self.school
    
    def getMonthlyPay(self):
        return self.annual_pay / 12
    
    def raiseAnnualPay(self, percent):
        self.annual_pay *= 1 + percent / 100

class Student(Person):
    
    def __init__(self, name, address, gpa, year, fee):
        super().__init__(name, address)
        self.gpa = gpa
        self.year = year
        self.fee = fee
    
    def getGpa(self):
        return self.gpa
    
    def setGpa(self, gpa):
        self.gpa = gpa
    
    def hasMinimumGpa(self):
        return self.gpa >= 3.5
    
    def willGraduateNextYear(self):
        return self.year == 4

tom = Staff("Tom", "Gangnam", "Yonsei", 35000)
dane = Staff("Dane", "Shindorim", "Sogang", 20000)
sum_tom = tom.getMonthlyPay() * 12
sum_dane = dane.getMonthlyPay() * 12

for i in range(6):
    tom.raiseAnnualPay(7)
    dane.raiseAnnualPay(15)
    sum_tom += tom.getMonthlyPay() * 12
    sum_dane += dane.getMonthlyPay() * 12
print("%s has a larger monthly pay" % "Tom" if sum_tom > sum_dane else "Dane")
