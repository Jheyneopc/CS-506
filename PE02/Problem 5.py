#Object-Oriented Programming*
#Part 1* class called Us
class User:
    def __init__(self, first_name, last_name, age, city):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city

    def describe_user(self):
        print(f"User: {self.first_name} {self.last_name}, Age: {self.age}, City: {self.city}")

    def greet_user(self):
        print(f"Hello {self.first_name}! Welcome back.")

# Create two users
user1 = User("Jheyne", "Cordeiro", 25, "Seattle")
user2 = User("Alex", "Smith", 30, "New York")

user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

#Part 2**  Multilevel Inheritance
class Animal:
    def speak(self):
        print("Animals can make sounds")

class Dog(Animal):
    def bark(self):
        print("Dogs bark")

class Puppy(Dog):
    def weep(self):
        print("Puppies weep softly")

# Test it
puppy = Puppy()
puppy.speak()
puppy.bark()
puppy.weep()


