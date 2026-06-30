# Programming Fundamentals Assignment (Assignment 3)

Language used: **Python**

---

## 1. Operators

An **operator** is a symbol that tells the computer to perform a specific action (math, comparison, logic, or assignment) on one or more values.

### a) Arithmetic Operators
Used to perform math calculations.

| Operator | Meaning | Example | Result |
|---|---|---|---|
| `+` | Addition | `5 + 3` | `8` |
| `-` | Subtraction | `5 - 3` | `2` |
| `*` | Multiplication | `5 * 3` | `15` |
| `/` | Division | `5 / 2` | `2.5` |
| `%` | Modulus (remainder) | `5 % 2` | `1` |
| `**` | Exponent (power) | `5 ** 2` | `25` |
| `//` | Floor division | `5 // 2` | `2` |

**Example 1:**
```python
a = 10
b = 3
print(a + b)   # 13
print(a % b)   # 1 (remainder of 10/3)
```

**Example 2:**
```python
length = 4
width = 5
area = length * width
print("Area:", area)   # Area: 20
print("Power:", 2 ** 3)   # Power: 8
```

### b) Comparison (Relational) Operators
Used to compare two values. They always return `True` or `False`.

| Operator | Meaning |
|---|---|
| `==` | Equal to |
| `!=` | Not equal to |
| `>` | Greater than |
| `<` | Less than |
| `>=` | Greater than or equal to |
| `<=` | Less than or equal to |

**Example 1:**
```python
x = 7
y = 10
print(x == y)   # False
print(x < y)    # True
```

**Example 2:**
```python
age = 18
print(age >= 18)   # True (eligible to vote)
print(age != 18)   # False
```

### c) Logical Operators
Used to combine multiple conditions.

| Operator | Meaning |
|---|---|
| `and` | True if both conditions are True |
| `or` | True if at least one condition is True |
| `not` | Reverses the result |

**Example 1:**
```python
age = 20
has_id = True
print(age >= 18 and has_id)   # True
```

**Example 2:**
```python
is_raining = False
is_sunny = True
print(is_raining or is_sunny)   # True
print(not is_raining)           # True
```

### d) Assignment Operators
Used to assign or update values stored in variables.

| Operator | Meaning | Example | Same as |
|---|---|---|---|
| `=` | Assign value | `x = 5` | — |
| `+=` | Add and assign | `x += 3` | `x = x + 3` |
| `-=` | Subtract and assign | `x -= 3` | `x = x - 3` |
| `*=` | Multiply and assign | `x *= 3` | `x = x * 3` |
| `/=` | Divide and assign | `x /= 3` | `x = x / 3` |

**Example 1:**
```python
score = 10
score += 5
print(score)   # 15
```

**Example 2:**
```python
total = 100
total -= 20
total *= 2
print(total)   # 160
```

---

## 2. Data Types

A **data type** describes the kind of value a variable holds and what operations can be done on it.

### a) Integer (`int`)
A whole number, with no decimal point.

**Example 1:**
```python
age = 25
print(type(age))   # <class 'int'>
```

**Example 2:**
```python
students = 40
print(students)   # 40
```

### b) Float (`float`)
A number with a decimal point.

**Example 1:**
```python
price = 9.99
print(type(price))   # <class 'float'>
```

**Example 2:**
```python
temperature = 36.6
print(temperature)   # 36.6
```

### c) String (`str`)
A sequence of characters (text), enclosed in quotes.

**Example 1:**
```python
name = "Alice"
print(name)   # Alice
```

**Example 2:**
```python
greeting = "Hello, " + "World!"
print(greeting)   # Hello, World!
```

### d) Boolean (`bool`)
Represents one of two values: `True` or `False`.

**Example 1:**
```python
is_student = True
print(type(is_student))   # <class 'bool'>
```

**Example 2:**
```python
is_passing = 60 >= 50
print(is_passing)   # True
```

### e) List (`list`)
An ordered, **changeable** collection of items, written in square brackets `[]`.

**Example 1:**
```python
fruits = ["apple", "banana", "cherry"]
print(fruits[0])   # apple
```

**Example 2:**
```python
numbers = [1, 2, 3]
numbers.append(4)
print(numbers)   # [1, 2, 3, 4]
```

### f) Tuple (`tuple`)
An ordered collection of items, written in parentheses `()`, but **unchangeable** (immutable) once created.

**Example 1:**
```python
coordinates = (10, 20)
print(coordinates[1])   # 20
```

**Example 2:**
```python
colors = ("red", "green", "blue")
print(colors)   # ('red', 'green', 'blue')
```

### g) Dictionary (`dict`)
A collection of `key: value` pairs, written in curly braces `{}`.

**Example 1:**
```python
student = {"name": "John", "age": 20}
print(student["name"])   # John
```

**Example 2:**
```python
prices = {"apple": 1.5, "banana": 0.5}
prices["mango"] = 2.0
print(prices)   # {'apple': 1.5, 'banana': 0.5, 'mango': 2.0}
```

---

## 3. Conditional Statements

Conditional statements let a program make decisions and run different code depending on whether a condition is `True` or `False`.

### a) `if` statement
Runs a block of code only if the condition is True.

**Example 1:**
```python
age = 20
if age >= 18:
    print("You are an adult.")
```

**Example 2:**
```python
balance = 500
if balance > 0:
    print("You have funds available.")
```

### b) `if...else` statement
Runs one block if the condition is True, and a different block if it is False.

**Example 1:**
```python
age = 16
if age >= 18:
    print("You can vote.")
else:
    print("You cannot vote yet.")
```

**Example 2:**
```python
number = 7
if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")
```

### c) `if...elif...else` statement
Checks multiple conditions in order and runs the block for the first one that is True.

**Example 1:**
```python
score = 75
if score >= 90:
    print("Grade A")
elif score >= 70:
    print("Grade B")
else:
    print("Grade C")
```

**Example 2:**
```python
weather = "rainy"
if weather == "sunny":
    print("Wear sunglasses")
elif weather == "rainy":
    print("Carry an umbrella")
else:
    print("Check the forecast")
```

---

## 4. Loops

A **loop** is used to repeat a block of code multiple times.

### a) `for` loop
Repeats code for each item in a sequence (like a list, string, or range of numbers).

**Example 1:**
```python
for i in range(5):
    print(i)   # prints 0 1 2 3 4
```

**Example 2:**
```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

### b) `while` loop
Repeats code as long as a condition remains True.

**Example 1:**
```python
count = 0
while count < 5:
    print(count)
    count += 1
```

**Example 2:**
```python
total = 0
n = 1
while n <= 3:
    total += n
    n += 1
print("Total:", total)   # Total: 6
```

### c) Nested loops
A loop placed inside another loop. The inner loop completes all its iterations for each single iteration of the outer loop.

**Example 1:**
```python
for i in range(1, 3):
    for j in range(1, 3):
        print(i, j)
# Output: 1 1, 1 2, 2 1, 2 2
```

**Example 2:**
```python
for row in range(3):
    for col in range(3):
        print("*", end=" ")
    print()   # moves to a new line after each row
```

### d) `break` and `continue`
- `break` stops the loop completely.
- `continue` skips the current iteration and moves to the next one.

**Example 1 (`break`):**
```python
for number in range(1, 10):
    if number == 5:
        break
    print(number)   # prints 1 2 3 4, then stops
```

**Example 2 (`continue`):**
```python
for number in range(1, 6):
    if number == 3:
        continue
    print(number)   # prints 1 2 4 5 (skips 3)
```

---

## Summary

| Concept | Key Idea |
|---|---|
| Operators | Perform actions on values (math, comparison, logic, assignment) |
| Data Types | Define the kind of value a variable stores |
| Conditional Statements | Allow a program to make decisions |
| Loops | Allow a program to repeat actions |

All examples above are written in Python, are runnable as-is, and use simple, beginner-friendly logic.