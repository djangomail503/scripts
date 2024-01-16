class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def make_sound(self):
        print(f"{self.name} says {self.sound}")

class Dog(Animal):
    def __init__(self, name, sound, breed, color):
        super().__init__(name, sound)
        self.breed = breed
        self.color = color

    def bark(self):
        print(f"{self.name} (a {self.color} {self.breed} dog) barks")

class WorkingDog(Dog):
    def __init__(self, name, sound, breed, color, task):
        super().__init__(name, sound, breed, color)
        self.task = task

    def do_task(self):
        print(f"{self.name} (a {self.color} {self.breed} working dog) performs the task: {self.task}")

# Example usage:
working_dog = WorkingDog("Rex", "Woof", "German Shepherd", "Black and Tan", "Search and Rescue")
working_dog.make_sound()
working_dog.bark()
working_dog.do_task()
