#variables in pyhton day 1

"""
[In Python, variables are used as named containers for storing data values.]

Dynamic typing means that you we don’t need to declare the type of a variable when you create it.

Python automatically figures out the type at runtime based on the value assigned.


Naming Rules:

1. Variable names must start with a letter (a-z, A-Z) or an underscore (_).
2. They cannot start with a number.
3. They can contain letters, numbers, and underscores.
4. Variable names are case-sensitive (myVar and myvar are different).
5. Keywords (reserved words like if, for, while) cannot be used as variable names.


Memory Management:
A variable acts as a reference or pointer to a memory location where the actual data value is stored.


Types of variables:

1. Numeric Types

| Type      | Description                      | Example      |
| --------- | -------------------------------- | ------------ |
| `int`     | Integer numbers                  | `x = 10`     |
| `float`   | Floating-point (decimal) numbers | `pi = 3.14`  |
| `complex` | Complex numbers                  | `z = 2 + 3j` |


2. Text Type:

| Type  | Description                     | Example            |
| ----- | ------------------------------- | ------------------ |
| `str` | String (sequence of characters) | `name = "Pranith"` |


3. Boolean Type:

| Type   | Description    | Example       |
| ------ | -------------- | ------------- |
| `bool` | Logical values | `flag = True` |


4. Sequence Types:

| Type    | Description                   | Example             |
| ------- | ----------------------------- | ------------------- |
| `list`  | Ordered, mutable collection   | `nums = [1, 2, 3]`  |
| `tuple` | Ordered, immutable collection | `coords = (10, 20)` |
| `range` | Immutable sequence of numbers | `r = range(1, 5)`   |

5. Set Types:

| Type        | Description                       | Example                     |
| ----------- | --------------------------------- | --------------------------- |
| `set`       | Unordered, mutable, no duplicates | `s = {1, 2, 3}`             |
| `frozenset` | Immutable version of set          | `fs = frozenset([1, 2, 3])` |

6. Mapping Types:

| Type   | Description     | Example                                    |
| ------ | --------------- | ------------------------------------------ |
| `dict` | Key-value pairs | `student = {"name": "Pranith", "age": 20}` |

7. None Types:

| Type       | Description           | Example    |
| ---------- | --------------------- | ---------- |
| `NoneType` | Represents null value | `x = None` |




"""
# x = 10 #integer 
# y = "hello pranith!" # string

# z = 1.0 #float




# print(id(x))
# print(id(y))

# print(id(z))

# print(type(x))

"""
Multiple Assignments
Python allows multiple variables to be assigned values in a single line.

Assigning Different Values
We can assign different values to multiple variables simultaneously, making the code concise and easier to read.


"""

# x , y , z = 1 , 1.5 , "Hello Pranith"

# print(x,"\n",y)

# a = b =c = 10
# a =a+1
# print(a)
# print(b)
# print(c)


a =10
b = 10

print( a == b )