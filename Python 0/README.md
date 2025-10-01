# Python 

### Tutorial vids
- Python for Beginners – Full Course [Programming Tutorial]
https://www.youtube.com/watch?v=eWRfhZUzrAc

- Python Tutorial for Beginners - Learn Python in 5 Hours [FULL COURSE]
https://www.youtube.com/watch?v=t8pPdKYpowI

### Documentation
- Python Tutorial
https://www.w3schools.com/python/

- Beginner's Guide to Python
https://wiki.python.org/moin/BeginnersGuide



## Python 0

Python has a few basic built-in data types that are **super important**:
- **List** 📋  
- **Tuple** 🎁  
- **Set** 🔀  
- **Dictionary (dict)** 📖  

### List 📋
- **Definition**: An ordered, changeable collection that can hold duplicates.
- **Syntax**: Use square brackets `[]`.
- **features**:
Ordered (keeps order).
Mutable (can be changed).
Allows duplicates.
```python
# Example
fruits = ["apple", "banana", "cherry"]
print(fruits[0])   # apple (first item, index 0)

# Change value
fruits[1] = "blueberry"
print(fruits)      # ['apple', 'blueberry', 'cherry']

# Add new value
fruits.append("orange")
print(fruits)      # ['apple', 'blueberry', 'cherry', 'orange']
```

### Tuple 🎁
- Definition: An ordered, unchangeable collection that can hold duplicates.
- Syntax: Use parentheses ().
- **features**:
Ordered (like list).
Immutable (cannot change after creation).
Allows duplicates.
```python
# Example
point = (10, 20)
print(point[0])   # 10
print(point[1])   # 20

# Tuples cannot be changed
# point[0] = 50   ❌ ERROR

# To "modify", you must create a new tuple
point = (50, point[1])
print(point)      # (50, 20)

```

### Set 🔀
- Definition: An unordered collection with no duplicates.
- Syntax: Use curly braces {}.
- features:
Unordered (no index, order may change).
Mutable (can add/remove).
No duplicates.

```python
# Example
colors = {"red", "green", "blue"}
print(colors)        # {'green', 'blue', 'red'} (order is random!)

# Add item
colors.add("yellow")
print(colors)        # {'yellow', 'green', 'blue', 'red'}

# No duplicates
colors.add("red")
print(colors)        # {'yellow', 'green', 'blue', 'red'} (no change)

```

### Dictionary (dict) 📖
- Definition: A collection of key → value pairs.
- Syntax: Use curly braces {} with key: value.
- features: 
Stores key → value pairs.
Keys must be unique.
Values can be changed.
Ordered since Python 3.7 (insertion order kept).


## Summary Table

| Data Type    | Syntax Example          | Ordered? | Mutable? | Allows Duplicates? | How to Access / Modify                                          |
| ------------ | ----------------------- | -------- | -------- | ------------------ | --------------------------------------------------------------- |
| **List** 📋  | `["Hello", "World!"]`   | ✅ Yes    | ✅ Yes    | ✅ Yes              | By index → `list[0]` <br> Change → `list[1] = "Hi"`             |
| **Tuple** 🎁 | `("Hello", "France!")`  | ✅ Yes    | ❌ No     | ✅ Yes              | By index → `tuple[0]` <br> (cannot modify, must recreate)       |
| **Set** 🔀   | `{"Hello", "Paris!"}`   | ❌ No     | ✅ Yes    | ❌ No (only unique) | Check membership → `"Hello" in set` <br> Add → `set.add("new")` |
| **Dict** 📖  | `{"Hello": "42Paris!"}` | ✅ Yes*   | ✅ Yes    | Keys ❌, Values ✅   | By key → `dict["Hello"]` <br> Change → `dict["Hello"] = "Hi"`   |



> ℹ️ *Dictionaries keep insertion order in Python 3.7+ (so order is predictable now).

