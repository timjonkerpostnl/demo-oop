# Demo

> This demo shows the power of object oriented programming

# Before you start:

Create a new environment and install packages:

```bash
poetry install
```

## Project description
After installation you can start the assignment. There are two modules:  
- src/exercise
- src/possible_solution

In principle you do not need the possible solution module, but you could use it for inspiration if you like.

Within the src/exercise module you find files that contain different classes. You are not restricted to keep these files
, but I think they are useful.

The main file is still empty and you can fill it as you like. This should be the only file that you execute.

Most of the other files have a class definition, a short description of the class's attributes and the methods that it should implement.

Steps to complete the assignment:
- Fill the Person class by implementing the required attributes
- Create the Car class by implementing the required attributes. You can choose the types yourself for now.
- Refactor your code such that Brand becomes a class. The brand should get its attributes solely based on the brand name.
- Refactor your code such that Engine becomes a class that holds the amount of horse power.
- Make sure that when creating a car the Brand and the Engine are compatible.
- Fill the insurance company module by implementing the correct cost formula. The good thing in Python is that you can mix functional and object oriented programming
- Add a method to person that let's you request insurance.
- If done correctly you can now Create a Person with a name and age and with or without a Car, The person can buy a car by giving a few specs these specs should be compatible.
The Person should be able to request insurance costs. If you get a person of 28 yr, driving a 20 hp Suzuki you should have 316 insurance cost.
- Now you can free style around adding more methods to your classes or making them more fancy.
  - Think of a navigation system
  - A climate control system
  - A self driving functionality
  Remember not to make it too complex within this assigment, if you don't know something than take something random or hardcode it. 
  The pro of using classes is that it is very modular so you can easily implement methods more thoroughly later

I hope that you learned something about Object Oriented Programming.
