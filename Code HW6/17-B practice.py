# Simple OOP Project (1): Animal and Dog
class Animal:

    def __init__(self):
        print("Animal created")
    
    def whoAmI(self):
        print("Animal")
    
    def eat(self):
        print("Eating")

class Dog(Animal):

    def __init__(self):
        super().__init__()

        print("Dog created")
    
    def whoAmI(self):
        print("Dog")
    
    def bark(self):
        print("Woof!")

'''
이 코드는 Animal, Dog의 두 Classes를 정의하고 있다.

Animal Class:
    instance 생성 시 "Animal created"을 출력한다.
    whoAmI()이 호출되면 "Animal"을 출력한다.
    eat()이 호출되면 "Eating"을 출력한다.

Dog Class:
    Animal Class를 상속한다.
    instance 생성 시 Parent Class인 Animal Class의 __init__을 실행하여 "Animal created"을 출력한다. 이어서 "Dog created"을 출력한다.
    whoAmI()은 Animal Class의 function을 덮어써서 "Dog"을 출력한다.
    eat()이 호출되면 Animal Class의 function을 상속하여 "Eating"을 출력한다.
    bark()이 호출되면 "Woof!"을 출력한다.
'''

d = Dog()
d.whoAmI()
d.eat()
d.bark()

'''
이 코드의 실행 결과는 다음과 같다:
Animal created
Dog created
Dog
Eating
Woof!
'''

# Simple OOP Project (2): Circle
class Circle():
    pi = 3.141592

    def area(self):
        return self.pi * self.r ** 2

    def setRadius(self, r):
        self.r = r
    
    def getRadius(self):
        return self.r

# Simple OOP Project (3): Shape and Others
class Shape:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.description = "This shape has not been described yet"
        self.author = "Nobody has claimed to make this shape yet"
    
    def area(self):
        return self.x * self.y

    def perimeter(self):
        return 2 * self.x + 2 * self.y
    
    def describe(self, text):
        self.description = text
    
    def authorName(self, text):
        self.author = text
    
    def scaleSize(self, scale):
        self.x = self.x * scale
        self.y = self.y * scale

'''
이 코드는 Shape Class를 정의하고 있다.

Shape Class:
    instance 생성 시 parameter로 x, y를 받아 각각 self.x, self.y의 값으로 설정한다. 이어서 self.description과 self.author를 설정한다.
    area()이 호출되면 도형의 넓이를 출력한다.
    perimeter()이 호출되면 도형의 둘레의 길이를 출력한다.
    describe()이 호출되면 parameter로 text를 받아 self.description의 값으로 설정한다.
    authorName()이 호출되면 parameter로 text를 받아 self.author의 값으로 설정한다.
    scaleSize()이 호출되면 parameter로 scale을 받아 self.x, self.y에 각각 곱한다.
'''


rectangle = Shape(100, 45)
print(rectangle.area())
print(rectangle.perimeter())
rectangle.describe("A wide rectangle, more than twice as wide as it is tall")
rectangle.scaleSize(0.5)
print(rectangle.area())

'''
이 코드의 실행 결과는 다음과 같다:
4500
290
1125.0
'''

class Square(Shape):
    def __init__(self, a):
        self.x = self.y = a

class DoubleSquare(Square):
    def area(self):
        return 2 * self.x ** 2
    
    def perimeter(self):
        return 6 * self.x

class InsideDoubleSquare(Square):
    def area(self):
        return (self.x ** 2) / 4.0
    
    def perimeter(self):
        return 2 * self.x
