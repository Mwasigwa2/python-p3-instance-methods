#!/usr/bin/env python3

class Dog:
  def  bark(self):
    print("Woof") #Instance method definition
  def sit(self):
    print("The dog is sitting.") #Instance method definition

fido = Dog()
fido.bark()
fido.sit()

snoopy = Dog()
snoopy.bark()
snoopy.sit()