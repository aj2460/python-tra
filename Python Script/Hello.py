#Author : Anand
import sys
print ("hello")

age=20
name="Anand"

print ("{0} was {1} years old when he wrote this book" . format(name, age))
print ("Why is {} playing with that python?"  . format(name))

print ('{0:.3f}'. format(1.0/3), end="  *   ") #end continue the next line oanthe same line
print ('{0:_^11}' . format("Hello"))

print ('{name} wrote {book}' . format (name='Swaroop',book='A byte of python'))


print('python ',sys.version)
