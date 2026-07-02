# OOP in Python: Classes, Objects, Methods, and Constructors

## The Problem OOP Solves

Say you are tracking bodas at a stage. Each boda has a driver, a plate number, and a fuel level. Each boda can start and can ride a distance. Without OOP, you would need separate variables for every boda, and separate functions that somehow know which boda they are working with. This gets messy fast with more than a couple of bodas.

A class solves this. It lets you define one blueprint describing what a boda has and what a boda can do. You then use that single blueprint to create as many individual bodas as needed, each keeping its own data completely separate from the others.

---

## Class

A class is a blueprint. It describes what something has (its data) and what it can do (its actions). A class on its own does nothing. It is only the design, not a real thing.

```python
class Boda:
    pass
```

This defines a class called `Boda`. At this point it is empty, but valid. Nothing has been built yet.

---

## Object

An object is a real thing built from a class. If the class is the design for a boda, the object is an actual boda sitting at the stage. Objects are also called instances.

```python
boda1 = Boda()
boda2 = Boda()
```

`boda1` and `boda2` are two separate objects, both built from the same `Boda` class. They exist independently. Changing one does not affect the other.

---

## Parameters and Arguments

These two terms get confused often, so they are worth separating clearly, with no class involved at all.

**Parameter** — a named placeholder inside a function or method's definition. It has no value yet. It is just a label, waiting to be filled in later.

**Argument** — the actual value supplied when the function or method is called. This is what fills in the parameter.

```python
def greet(name):          # name is a PARAMETER, an empty label
    print(f"Hello {name}")

greet("Deen")              # "Deen" is the ARGUMENT, the real value
```

The parameter is the empty seat. The argument is who sits in it.

---

## The Constructor (`__init__`)

A constructor is a special method whose job is to build, or "construct," a new object, and set up its starting attributes, the moment that object is created.

In Python, the constructor is named `__init__`. The double underscores on each side mark it as a special method that Python recognises and runs automatically. It is never called directly by name.

The constructor runs exactly once per object, at the moment that object is created, and never again after that. It fires the instant something like `Boda("John", "UAA 123A", 50)` is written, before that line even finishes executing.

Before the constructor runs, the object is blank. It exists in memory but holds no attributes, nothing usable. After the constructor finishes, the object is fully formed, holding every attribute the constructor set up for it.

```python
class Boda:
    def __init__(self, driver, plate, fuel):
        self.driver = driver
        self.plate = plate
        self.fuel = fuel
```

`driver`, `plate`, `fuel` in the parameter list are temporary. They exist only for the life of `__init__`, and disappear completely once it finishes running.

Once the constructor finishes, its parameters are torn down. The object itself does not disappear. It remains in memory, now carrying every attribute the constructor gave it, ready to be used for as long as the object exists.

---

## `self`

`self` always refers to whichever object a piece of code is currently working with. The class is written once, but many objects get built from it. `self` is how the shared code inside the class knows which specific object it should read from or write to at any given moment.

**Outside the class**, when calling a method, whatever sits before the dot becomes `self`:

```python
boda1.start()   # self becomes boda1 inside start
boda2.start()   # self becomes boda2 inside start
```

**Inside `__init__` specifically**, there is no dot yet, because the object does not have a name until the line finishes. Python creates a blank object first, then hands that blank object to `__init__` directly as `self`. `self` here represents the object being built, the same object that will be named `boda1` once construction is complete.

`self` is the object itself. `self.driver` is not the object, it is one single attribute stored inside that object.

---

## Attributes

An attribute is a piece of data permanently stored on a specific object. Attributes are created inside the constructor, using the pattern:

```python
self.attribute_name = parameter_name
```

For example:

```python
self.driver = driver
```

Reading this correctly, right side first: take the value currently sitting in the parameter `driver`, and store it into a new, permanent slot on the object, called `driver`, accessed through `self`.

**Why this line is necessary.** Parameters are temporary. The moment `__init__` finishes running, its parameters vanish completely. If the value only ever sat in the parameter, it would be lost the instant `__init__` ended. `self.driver = driver` exists to catch that value before the parameter disappears, and move it onto the object, where it survives permanently.

Parameters and attributes can share the same name, which is exactly why this line looks confusing at first. They are not the same thing. The parameter is a temporary carrier, gone as soon as the constructor ends. The attribute is a permanent slot, living on the object for as long as the object exists.

```python
boda1 = Boda("John", "UAA 123A", 50)
print(boda1.driver)   # still works, long after __init__ has finished
```

This only works because the value survived as an attribute, not because the parameter is still around. It is not.

An attribute is data, no parentheses, nothing runs. `self.driver` just returns a stored value.

---

## Methods

A method is a function that belongs to a class. It describes something an object can do.

A function on its own, defined outside any class, exists independently and is not tied to any object. A method is different specifically because of where it lives: inside a class, permanently attached to every object built from that class.

```python
def greet(name):          # a function, lives on its own
    print(f"Hello {name}")

class Boda:
    def start(self):      # a method, lives inside the class
        print(f"{self.driver} has started the boda {self.plate}")
```

Every method takes `self` as its first parameter, without exception, because that is how it reaches into a specific object's attributes. A method can take further parameters after `self`, exactly like a normal function.

```python
def ride(self, distance):
    self.fuel = self.fuel - distance
    print(f"Rode {distance} km. Fuel remaining: {self.fuel}")
```

`self` identifies which object is riding. `distance` is a normal argument, supplied when the method is called: `boda1.ride(10)`.

**Attributes are nouns, methods are verbs.** `driver`, `plate`, `fuel` are things a boda *has*. `start()`, `ride()` are things a boda *does*. Methods have parentheses because they run code. Attributes do not, because they only hold data.

Every object built from a class shares the exact same methods, but each call acts on whichever object called it:

```python
boda1 = Boda("John", "UAA 123A", 50)
boda2 = Boda("Gad", "UAN 765D", 30)

boda1.start()   # self = boda1, prints John's details
boda2.start()   # self = boda2, prints Gad's details
```

One method, written once, producing different results depending on which object called it.

---

## `print` versus `return`

These look similar but do completely different jobs.

**`print`** displays a value on screen, for a human to see. Once displayed, the value is gone. It is not stored, not usable anywhere else in the program.

```python
def subtract(num1, num2):
    print(num1 - num2)

answer = subtract(3, 2)   # shows 1 on screen
print(answer)              # prints None, because nothing was returned
```

**`return`** hands a value back to whatever called the function, so it can be stored, reused, or passed elsewhere. It does not display anything on its own.

```python
def subtract(num1, num2):
    return num1 - num2

answer = subtract(3, 2)
print(answer)              # prints 1
print(answer * 10)         # prints 10, because answer actually holds a real value
```

**The rule:** if anything else in the program needs to use the value afterward, use `return`. If a human just needs to see it once, right now, and nothing else will ever touch that value again, `print` is enough. They are not mutually exclusive. The common pattern is to `return` a value from a function, then `print` it wherever the function gets called.

This matters especially when functions or methods work together. If one function only prints instead of returning, any other function or method trying to use its result will receive `None`, and the program will likely break.

---

## Full Example, Everything Together

```python
class Boda:
    def __init__(self, driver, plate, fuel):
        self.driver = driver      # attribute, permanent
        self.plate = plate        # attribute, permanent
        self.fuel = fuel          # attribute, permanent

    def start(self):
        print(f"{self.driver} has started the boda {self.plate}")

    def ride(self, distance):
        self.fuel = self.fuel - distance
        return self.fuel          # returned, so the value can be reused

boda1 = Boda("John", "UAA 123A", 50)
boda2 = Boda("Gad", "UAN 765D", 30)

boda1.start()
remaining = boda1.ride(10)
print(f"Fuel left: {remaining}")

boda2.start()
```

Output:

```
John has started the boda UAA 123A
Fuel left: 40
Gad has started the boda UAN 765D
```

`boda1` and `boda2` are separate objects, each with its own attributes. Calling `ride` on `boda1` never affects `boda2`'s fuel.

---

## Summary Table

| Term | Definition |
|---|---|
| Class | The blueprint. Describes what an object has and can do. Not a real thing. |
| Object | A real thing built from a class. Also called an instance. |
| Constructor (`__init__`) | Special method that runs automatically when an object is created. Sets up starting attributes. |
| Parameter | An empty labelled slot in a method's definition, filled in later. Temporary. |
| Argument | The real value supplied when a function or method is called. |
| Attribute | Data permanently stored on a specific object. Created inside the constructor. Survives after the constructor finishes. |
| `self` | Refers to whichever object is currently being worked with. Inside a method call, it equals whatever sits before the dot. Inside `__init__`, it is the object under construction. |
| Method | A function that belongs to a class. Describes something an object can do. Always takes `self` first. |
| `print` | Displays a value on screen. The value is not stored or reusable afterward. |
| `return` | Hands a value back to the caller, so it can be stored, reused, or passed on. |