#### Class
a class is a blueprint. It doesn't do anything by itself. It just describes what something should look like and what it can do.


#### Object
An instance of the class. It is actual thing built from the blueprint. You can make as many objects as you want from a class. 


#### Giving an object properties
We set the details/properties when the project is created. We use a special method called __init__ to set those details when the object is created.


#### Methods
A method is a function that belongs to a class. It descrbes something that an object can do

---

In summary:

def __init__(self, driver, plate, fuel):
- this line announces the setup method and creates its paramter list. self, drive,r plate, fuel. They empty, temporary slots, waiting for something to fill them. This line is only stating what __init__ will expect to receive whenver it eventually runs.

self.driver = driver, self.plate = plate, self.fuel = fuel
- Still not running. It is part of writing the definition of init. So Python is reading these here are the instructions init will carry out.
- take the value currently sitting in this parameter and it as as a merpantent attribute on the object, using the same name.
- Right side: read the parameter driver, whatever value was passed in, e.g John. Left side: a new new attribute slot on the object. 

The left side, self.driver, creates a new attribute slot on the object self currently refers to. The right side, driver, is read first, and whatever value is sitting in that parameter at that moment gets copied into the new slot.
So the full instruction: create a slot called driver on the object, and immediately fill it with whatever value the parameter driver is currently holding.




create five classes with objects