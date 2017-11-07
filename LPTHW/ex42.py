## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## Dog is-a class of type Animal
class Dog(Animal):

    def __init__(self, name):
        ## name is-a attribute of class Dog
        self.name = name

## Cat is-a class of type Animal
class Cat(Animal):

    def __init__(self, name):
        ## name is-a attribute of class Cat
        self.name = name

## Person is-a class of type object
class Person(object):

    def __init__(self, name):
        ## name is-a attribute of Person
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

## Employee is-a class of type Person
class Employee(Person):

    def __init__(self, name, salary):
        ## Invoke the __init__ of parent Person class, hmm what is this strange magic?
        super(Employee, self).__init__(name)
        ## salary is-a attribute of class Employee
        self.salary = salary

## ??
class Fish(object):
    pass

## ??
class Salmon(Fish):
    pass

## ??
class Halibut(Fish):
    pass


## rover is-a Dog
rover = Dog("Rover")

## ??
satan = Cat("Satan")

## ??
mary = Person("Mary")

## ??
mary.pet = satan

## ??
frank = Employee("Frank", 120000)

## ??
frank.pet = rover

## ??
flipper = Fish()

## ??
crouse = Salmon()

## ??
harry = Halibut()