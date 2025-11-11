
[Back to Index](../README.md)

# Python00 — Introductory exercises

This folder contains small, self-contained Python exercises aimed at beginners. Each `exNN` directory focuses on a single concept or a few related concepts. Below are short notes for each exercise: important notions, libraries used (if any), and quick syntax or usage tips.

## How to use these exercises

- Open the exercise file (for example `ex00/Hello.py`) in an editor or run it from the command line with `python3 path/to/file`.
- Each example is intentionally small — read the source to see the idiomatic usage shown.

---

## ex00 — Hello.py

- Notions: program entry point, printing to stdout, basic string literals.
- Libraries: none.
- Syntax tips: use `print("Hello")` for output. If you need a script-style entry point, add:

	if __name__ == "__main__":
			main()

	This guards execution when the file is imported as a module.

## ex01 — format_ft_time.py

- Notions: formatting strings, working with time/dates, `str.format()` or f-strings.
- Libraries: `time` or `datetime` (check the file for which is used). For modern code prefer `datetime`.
- Syntax tips: use f-strings for clarity: `f"{hours:02d}:{minutes:02d}:{seconds:02d}"`.

## ex02 — find_ft_type.py

- Notions: type checking, `isinstance`, conditional logic.
- Libraries: none typically — builtins only.
- Syntax tips: prefer `isinstance(x, (list, tuple))` over `type(x) == list` when you want to allow subclasses.

## ex03 — NULL_not_found.py

- Notions: handling `None`, truthiness, guarding against missing values.
- Libraries: none.
- Syntax tips: check for `None` explicitly when necessary: `if x is None:`. Avoid `if not x:` when `0`, `''`, or `False` are valid values.

## ex04 — whatis.py

- Notions: introspection (`type()`, `dir()`, `help()`), printing metadata about values.
- Libraries: none (uses builtins introspection functions).
- Syntax tips: `help(obj)` and `dir(obj)` are useful during exploration; use `type(obj)` to get the object's class.

## ex05 — building.py

- Notions: likely demonstrates building data structures or a simple class — check code for `class` usage or function composition.
- Libraries: none expected.
- Syntax tips: if classes are present, add a `__repr__` or `__str__` for readable debug output.

## ex06 — filterstring.py / ft_filter.py

- Notions: higher-order functions (`map`, `filter`), lambdas, string processing.
- Libraries: none required — uses builtins.
- Syntax tips: use list comprehensions for readable filters: `[s for s in seq if condition(s)]`. For lazy evaluation use `filter()` or generator comprehensions.

## ex07 — sos.py

- Notions: perhaps recursion, simple algorithms, or string parsing (filename suggests a small utility).
- Libraries: none expected.
- Syntax tips: keep functions small and pure where possible, and add docstrings describing inputs/outputs.

## ex08 — Loading.py

- Notions: module importing, file I/O, or dynamic loading of resources.
- Libraries: likely uses `open()` for file reading or `importlib` for dynamic imports.
- Syntax tips: use `with open(path, 'r') as f:` to ensure files are closed safely. For importing by name, use `importlib.import_module("module_name")`.

## ex09 — ft_package (package example)

- Notions: Python package structure, `__init__.py`, creating reusable modules, `pyproject.toml` metadata.
- Libraries: none required; the directory `ft_package` is an example module with `count_in_list.py`.
- Syntax tips:
	- Import sibling modules inside the package with absolute imports from the package root, e.g. `from ft_package.count_in_list import count_in_list`.
	- If a `pyproject.toml` is present, the project can be made installable with modern build tools (PEP 517/518).
