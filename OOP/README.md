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

A constructor is a special method whose job is to build, or "construct," a new object, and set up its starting attributes, the moment that object is created. 

self.driver = driver, self.plate = plate, self.fuel = fuel
- Still not running. It is part of writing the definition of init. So Python is reading these here are the instructions init will carry out.
- take the value currently sitting in this parameter and it as as a merpantent attribute on the object, using the same name.
- Right side: read the parameter driver, whatever value was passed in, e.g John. Left side: a new new attribute slot on the object. 

The left side, self.driver, creates a new attribute slot on the object self currently refers to. The right side, driver, is read first, and whatever value is sitting in that parameter at that moment gets copied into the new slot.
So the full instruction: create a slot called driver on the object, and immediately fill it with whatever value the parameter driver is currently holding.




create five classes with objects


--- 

A constructor is a special method whose job is to build, or "construct," a new object, and set up its starting attributes, the moment that object is created.

In Python, the constructor is named `__init__`. The double underscores on each side mark it as a special method that Python recognises and runs automatically, you never call `__init__()` directly by name yourself.

The constructor runs exactly once per object, at the moment that object is created, and never again after that. It fires the instant you write something like `Boda("John", "UAA 123A", 50)`, before that line even finishes executing.

Before the constructor runs, the object is blank, it exists in memory but holds no data, no attributes, nothing usable. After the constructor finishes, the object is fully formed, holding every attribute the constructor set up for it.

The constructor's first parameter is always `self`, which represents the object currently being built. Every other parameter after `self` represents a piece of data the object needs at the moment of its creation, supplied as arguments when the object is called into existence.

Inside the constructor, each attribute gets created and filled in the same way, `self.attribute_name = parameter_name`, taking a value that arrived through a parameter and storing it permanently on the object, in a slot that will still exist long after the constructor itself has finished running.

Once the constructor finishes, its parameters are torn down and disappear. The object itself does not disappear, it remains in memory, now carrying every attribute the constructor gave it, ready to be used by its methods for as long as the object exists.