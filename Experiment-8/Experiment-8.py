class Animal(ABC):

    def __init__(self, name):
        
        self.__name = name

    def get_name(self):
        return self.__name

    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):

    # Polymorphism
    def sound(self):
        print(self.get_name(), "says Woof!")


class Cat(Animal):

   
    def sound(self):
        print(self.get_name(), "says Meow!")



d = Dog("Buddy")
c = Cat("Kitty")

d.sound()
c.sound()