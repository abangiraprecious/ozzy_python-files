#### Methods

A method is a function that belongs to a class. It describes something that an object can do.

A function on its own, written outside any class, exists independently. It doesn't belong to anything, and it isn't tied to any particular object. A method is different specifically because of where it lives, inside a class, which means it is permanently attached to whatever objects get built from that class.

```python
def greet(name):          # a function, lives on its own
    print(f"Hello {name}")

class Boda:
    def start(self):      # a method, lives inside the class
        print(f"{self.driver} has started the boda {self.plate}")
```

Both are defined with `def`. Both can take parameters. Both can run code. The difference is entirely about location, and that location changes everything about how it behaves.

**Why methods always take `self` first**

Because a method belongs to a class, it needs a way to reach into the specific object it's currently working with, to read or change that object's attributes. `self` is how it does that. Every method, without exception, takes `self` as its first parameter, and Python automatically fills that in with whichever object sits before the dot when the method gets called.

```python
boda1.start()
```

Here, `boda1` sits before the dot, so `self` becomes `boda1` for the entire time `start` is running.

**What a method actually describes**

A method describes an action or a behaviour that belongs to the object. Not data, an action. This is the core difference between an attribute and a method. An attribute is a stored value, `self.driver`, `self.fuel`, just information sitting on the object. A method is something the object does, an active behaviour, `start()`, `ride()`, code that runs and can change those attributes, or use them to produce an output.

```python
class Boda:
    def __init__(self, driver, plate, fuel):
        self.driver = driver     # attribute, data
        self.plate = plate       # attribute, data
        self.fuel = fuel         # attribute, data

    def start(self):             # method, an action
        print(f"{self.driver} has started the boda {self.plate}")

    def ride(self, distance):    # method, an action
        self.fuel = self.fuel - distance
        print(f"Rode {distance} km. Fuel remaining: {self.fuel}")
```

`start` and `ride` are things a boda can do. `driver`, `plate`, `fuel` are things a boda has. That's the clean way to separate them, methods are verbs, attributes are nouns.

**Methods can take extra parameters beyond `self`**

`self` is always first, but a method can take more parameters after it, exactly like a regular function does. `ride(self, distance)` needs `self` to know which object it's working with, and it needs `distance` to know how far that object is travelling. When you call `boda1.ride(10)`, `self` becomes `boda1` automatically, and `10` fills the `distance` parameter, supplied by you as an argument, same as any normal function call.

**Methods can read attributes, and can also change them**

```python
def ride(self, distance):
    self.fuel = self.fuel - distance
```

This line reads `self.fuel`, whatever that object's current fuel is, subtracts `distance` from it, and writes the result straight back into `self.fuel`. This is something only a method can do easily, reach into an object's own stored data and permanently update it. A method isn't just describing an action in the abstract, it's an action that has real, lasting effects on that specific object's attributes.

**Every object built from the class shares the same methods, but acts on its own data**

```python
boda1 = Boda("John", "UAA 123A", 50)
boda2 = Boda("Gad", "UAN 765D", 30)

boda1.start()   # self = boda1, prints John's details
boda2.start()   # self = boda2, prints Gad's details
```

There is only one `start` method, written once, inside the class. But every object built from `Boda` can call it, and each time, `self` points to a different object, so the exact same code produces different results depending on who called it.

**One sentence**

A method is a function living inside a class, always taking `self` as its first parameter so it can reach into a specific object's attributes, describing something that object can actively do, as opposed to an attribute, which only describes something the object has.