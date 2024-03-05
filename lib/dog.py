# Define the Dog class with two instance methods
class Dog:
    # Instance method definition
    def bark(self):
        print("Woof!")
    
    # Instance method sit()
    def sit(self):
        print("The dog is sitting.")

# Create an instance of a dog
fido = Dog()

# Call the instance method using dot notation
fido.bark()  # Output: Woof!

# Create a second instance of Dog
snoppy = Dog()

# Call the same method on snoppy's object
snoppy.bark()  # Output: Woof!

fido.sit()