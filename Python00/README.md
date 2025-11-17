
# Python00

[Back to Index](../README.md)

---
## Super Basics : Types

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


### Summary Table of all types

| Data Type    | Syntax Example          | Ordered? | Mutable? | Allows Duplicates? | How to Access / Modify                                          |
| ------------ | ----------------------- | -------- | -------- | ------------------ | --------------------------------------------------------------- |
| **List** 📋  | `["Hello", "World!"]`   | ✅ Yes    | ✅ Yes    | ✅ Yes              | By index → `list[0]` <br> Change → `list[1] = "Hi"`             |
| **Tuple** 🎁 | `("Hello", "France!")`  | ✅ Yes    | ❌ No     | ✅ Yes              | By index → `tuple[0]` <br> (cannot modify, must recreate)       |
| **Set** 🔀   | `{"Hello", "Paris!"}`   | ❌ No     | ✅ Yes    | ❌ No (only unique) | Check membership → `"Hello" in set` <br> Add → `set.add("new")` |
| **Dict** 📖  | `{"Hello": "42Paris!"}` | ✅ Yes*   | ✅ Yes    | Keys ❌, Values ✅   | By key → `dict["Hello"]` <br> Change → `dict["Hello"] = "Hi"`   |

> ℹ️ *Dictionaries keep insertion order in Python 3.7+ (so order is predictable now).


### Common Built-in Exceptions (Python predefined errors)**


| Exception Name      | When it Happens                | Example                          |
| ------------------- | ------------------------------ | -------------------------------- |
| `FileNotFoundError` | When file path does not exist  | `open("no_file.txt")`            |
| `ValueError`        | Wrong value type               | `int("abc")`                     |
| `TypeError`         | Wrong data type used           | `"hi" + 5`                       |
| `IndexError`        | List index out of range        | `[1,2][5]`                       |
| `KeyError`          | Dictionary key not found       | `d = {"a":1}; d["b"]`            |
| `ZeroDivisionError` | Dividing by zero               | `10 / 0`                         |
| `ImportError`       | Import fails                   | `import not_existing_module`     |
| `AttributeError`    | Object has no attribute        | `"hi".append(3)`                 |
| `NameError`         | Variable not defined           | `print(x)`                       |
| `RuntimeError`      | Generic runtime error          | `raise RuntimeError("oops")`     |
| `SyntaxError`       | Invalid Python syntax          | `if True print("hi")`            |
| `IndentationError`  | Wrong indentation              | (bad spacing)                    |
| `OSError`           | System-related error           | File or OS issue                 |
| `MemoryError`       | Out of memory                  | Very large data                  |
| `StopIteration`     | When iterator runs out         | `next(it)` on exhausted iterator |
| `EOFError`          | End of file input unexpectedly | `input()` from empty stdin       |


### Packaging
- Python Package setup :
https://hackmd.io/@QBrv51OvRPqs9dJjL2YIig/rkA5azaall


---

## Brief on each exercise 

### ex00 — Hello.py

- Notions: program entry point, printing to stdout, basic string literals.
- Libraries: none.
- Syntax tips: use `print("Hello")` for output. If you need a script-style entry point, add:

	if __name__ == "__main__":
			main()

	This guards execution when the file is imported as a module.

### ex01 — format_ft_time.py

- Notions: formatting strings, working with time/dates, `str.format()` or f-strings.
- Libraries: `time` or `datetime` (check the file for which is used). For modern code prefer `datetime`.
- Syntax tips: use f-strings for clarity: `f"{hours:02d}:{minutes:02d}:{seconds:02d}"`.

### ex02 — find_ft_type.py

- Notions: type checking, `isinstance`, conditional logic.
- Libraries: none typically — builtins only.
- Syntax tips: prefer `isinstance(x, (list, tuple))` over `type(x) == list` when you want to allow subclasses.

### ex03 — NULL_not_found.py

- Notions: handling `None`, truthiness, guarding against missing values.
- Libraries: none.
- Syntax tips: check for `None` explicitly when necessary: `if x is None:`. Avoid `if not x:` when `0`, `''`, or `False` are valid values.

### ex04 — whatis.py

- Notions: introspection (`type()`, `dir()`, `help()`), printing metadata about values.
- Libraries: none (uses builtins introspection functions).
- Syntax tips: `help(obj)` and `dir(obj)` are useful during exploration; use `type(obj)` to get the object's class.

### ex05 — building.py

- Notions: likely demonstrates building data structures or a simple class — check code for `class` usage or function composition.
- Libraries: none expected.
- Syntax tips: if classes are present, add a `__repr__` or `__str__` for readable debug output.

### ex06 — filterstring.py / ft_filter.py

- Notions: higher-order functions (`map`, `filter`), lambdas, string processing.
- Libraries: none required — uses builtins.
- Syntax tips: use list comprehensions for readable filters: `[s for s in seq if condition(s)]`. For lazy evaluation use `filter()` or generator comprehensions.

### ex07 — sos.py

- Notions: perhaps recursion, simple algorithms, or string parsing (filename suggests a small utility).
- Libraries: none expected.
- Syntax tips: keep functions small and pure where possible, and add docstrings describing inputs/outputs.

### ex08 — Loading.py

- Notions: module importing, file I/O, or dynamic loading of resources.
- Libraries: likely uses `open()` for file reading or `importlib` for dynamic imports.
- Syntax tips: use `with open(path, 'r') as f:` to ensure files are closed safely. For importing by name, use `importlib.import_module("module_name")`.

### ex09 — ft_package (package example)

- Notions: Python package structure, `__init__.py`, creating reusable modules, `pyproject.toml` metadata.
- Libraries: none required; the directory `ft_package` is an example module with `count_in_list.py`.
- Syntax tips:
	- Import sibling modules inside the package with absolute imports from the package root, e.g. `from ft_package.count_in_list import count_in_list`.
	- If a `pyproject.toml` is present, the project can be made installable with modern build tools (PEP 517/518).
