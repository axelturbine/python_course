class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} says WOOOOF!")

    def info(self):
        print(f"{self.name} is a {self.breed}.")

my_dog = Dog("Buddy", "Golden Retriever")
my_dog .bark()
my_dog .info()

your_dog = Dog("Lajka", "Space Dog")
your_dog.bark()
your_dog.info()