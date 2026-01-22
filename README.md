# Python 

## Table of Contents

- [Tutorial videos](#tutorial-vids)
- [Documentation](#documentation)
- [Basic Concept Correcting](#Basic-Concept-Correcting)

### Index 
- [Python00 (Basics)](Python00/README.md)
- [Python01 (Array)](Python01/README.md)
- [Python02 (Data & CSV)](Python02/README.md)
- [Python03 (OOP)](Python03/README.md)
- [Python04 (Functions & Decorators)](Python04/README.md)
---

## Tutorial videos
- Python Tutorial for Beginners 1: [Install and Setup for Mac and Windows](https://www.youtube.com/watch?v=YYXdXT2l-Gg)
- [Python Tutorials](https://www.youtube.com/playlist?list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU)
- Python for Beginners – Full Course [Programming Tutorial](https://www.youtube.com/watch?v=eWRfhZUzrAc)
- Python Tutorial for Beginners - Learn Python in 5 Hours [FULL COURSE](https://www.youtube.com/watch?v=t8pPdKYpowI)

## Documentation
- [Python Standard Library](https://docs.python.org/3/library/)

- [Python Tutorial](https://www.w3schools.com/python/)

- [Beginner's Guide to Python](https://wiki.python.org/moin/BeginnersGuide)

---

## python env setup
- check if installed (version , path)
```bash
# Windows
python --version
which python

# macOS / Linux
python3 --version
which python3
```
- create environment for running python
> Create a new folder named `.venv` inside current directory.
> This folder will contain a standalone copy of Python and pip.
```bash
# Windows
python -m venv .venv

# macOS / Linux
python3 -m venv .venv
```
- Activate the Environment
> "Activating" tells terminal to stop using the global Python installed on computer and start using the local one inside the `.venv` folder.
```bash
# window
.venv\Scripts\activate
# macOS / Linux
source .venv/bin/activate
```
- Verify terminal is actually using the virtual environment.
```bash
# Windows
where python

# macOS / Linux
which python
```
- check & exit(deactivate)
```bash
python --version # python3 --version
deactivate
```

## Basic Concept Correcting

### “No code in the global scope”

##### 🔹 English

You should **not execute code** directly in the file’s top level (global scope).
Only define functions or classes there.

When your file is imported (`import myfile`), no code should automatically run.

✅ Correct:

```python
def say_hello():
    print("Hello!")

def main():
    say_hello()

if __name__ == "__main__":
    main()
```

❌ Wrong:

```python
print("Hello!")  # runs immediately when imported
```

##### 🔹 中文（繁體）

不要在「全域範圍（global scope）」直接執行程式。
只能在這裡**定義函式或類別**。

當別人 `import` 你的檔案時，不應該自動執行程式。

---

### `if __name__ == "__main__":`

##### 🔹 English

* Every Python file has a built-in variable `__name__`.
* When the file is **run directly**, Python sets `__name__ = "__main__"`.
* When it’s **imported**, `__name__ = "filename"`.

✅ Example:

```python
def main():
    print("Hello from main!")

if __name__ == "__main__":
    main()
```

* Run directly → will print
* Import → will not print

##### 🔹 中文（繁體）

每個 Python 檔案都有內建變數 `__name__`。

* 當你直接執行該檔案時，`__name__` 會等於 `"__main__"`。
* 當你從別的檔案匯入（import）時，`__name__` 會等於該檔案的名稱。

這樣可以讓程式區分「被執行」和「被匯入」的情況。

---

### “Any exception not caught will invalidate the exercise”

##### 🔹 English

You must handle errors with `try/except`.
If a runtime error happens and is not caught → ❌ exercise invalid.

✅ Example:

```python
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Error: cannot divide by zero.")
        return None
```

##### 🔹 中文（繁體）

必須用 `try / except` 處理例外（error）。
如果執行時發生錯誤但沒有被捕捉 → 作業算無效。

---

### “All your functions must have a documentation (**doc**)”

###### 🔹 English

`__doc__` is the **docstring** (文字文件註解) of your function.
It explains what the function does, its parameters, and its return value.

✅ Example:

```python
def add(a, b):
    """
    Adds two numbers together.

    Parameters:
        a (int | float): first number
        b (int | float): second number
    Returns:
        int | float: the sum of a and b
    """
    return a + b

print(add.__doc__)
```

###### 🔹 中文（繁體）

`__doc__` 是 Python 函式的**文件字串（docstring）**。
用來說明：

* 函式的功能
* 參數的型別與用途
* 回傳值的說明

所有函式都必須有這樣的說明註解。

---

### Python *can* run code globally

✅ **Fact:**
In Python, when you write code directly in the file (outside any function or class), it will **run immediately** when the file is executed or imported.

Example:

```python
# file: hello.py
print("This runs immediately")
```

### When you execute:

```
python hello.py
```

Output:

```
This runs immediately
```

### When you import:

```python
import hello
```

Still outputs:

```
This runs immediately
```

That means — **global code always runs**, even if you just import the file!

---

### 🚫 Why the subject forbids global code

Because when someone imports your file (for testing or reuse),
you **don’t want your code to execute automatically** — it should only run when you *explicitly* tell it to.

So they require:

```python
def main():
    # your program here

if __name__ == "__main__":
    main()
```

✅ **This ensures controlled execution.**

---

### How `__name__` and `"__main__"` work

Python automatically sets a special variable:

* `__name__ = "__main__"` when you **run** the file directly.
* `__name__ = "filename"` when you **import** it.

So this condition:

```python
if __name__ == "__main__":
```

means “run the next block **only when this file is executed directly**”.

---

#### 🧠 English Explanation Summary

| Situation                            | `__name__` value | Code under `if __name__ == "__main__":` runs? |
| ------------------------------------ | ---------------- | --------------------------------------------- |
| Run directly with `python myfile.py` | `"__main__"`     | ✅ Yes                                         |
| Imported into another file           | `"myfile"`       | ❌ No                                          |

---

### 🧱 ASCII Workflow Diagram

#### ❌ Without `main()` — global code (bad)

```
┌───────────────┐
│ hello.py      │
│ print("Run!") │
└──────┬────────┘
       │
       ▼
When imported → still prints "Run!"
```

### ✅ With `main()` and `__name__` check (good)

```
┌──────────────────────────────────────┐
│ def main():                          │
│     print("Run!")                    │
│                                      │
│ if __name__ == "__main__":           │
│     main()                           │
└─────────────┬────────────────────────┘
              │
              │ Run directly  → execute main()
              │
              ▼
         import → does nothing
```

---

### 🧩 Summary

| Concept         | English                                         | 中文說明                      |
| --------------- | ----------------------------------------------- | ------------------------- |
| Global code     | Executes anytime file is imported or run        | 全域程式碼在匯入時也會執行             |
| Main function   | Groups the program logic                        | 用來包住主程式邏輯                 |
| `__name__`      | Special variable = `"__main__"` if run directly | 特殊變數，直接執行時等於 `"__main__"` |
| Rule in subject | Restrict all execution inside `main()`          | 作業要求所有執行都放在 main() 裡面     |


---

### `__main__` and Double Underscores (`__name__`, etc.)

Python uses **double underscores** (`__like_this__`) for *special built-in names* — also known as **dunder names** ("double underscore").
They’re not just decoration — they have special meanings in the Python runtime.


| Syntax                   | Name                                     | When It’s Used / What It Means                                                                             | Example                                          |
| :----------------------- | :--------------------------------------- | :--------------------------------------------------------------------------------------------------------- | :----------------------------------------------- |
| `__main__`               | **Module name for the main script**      | When a Python file is run directly (e.g. `python myfile.py`), its `__name__` variable becomes `"__main__"` | `if __name__ == "__main__":`                     |
| `__name__`               | Current module’s name                    | Automatically set by Python: `"__main__"` if run directly, or the module name if imported                  | `print(__name__)`                                |
| `__init__`               | Constructor method in a class            | Called when you create a new instance                                                                      | `def __init__(self):`                            |
| `__str__`                | String representation for humans         | Used when you call `print(obj)`                                                                            | `def __str__(self): return "Nice!"`              |
| `__repr__`               | String representation for debugging      | Used in interactive shells or `repr(obj)`                                                                  | `def __repr__(self): return "Obj(...)"`          |
| `__len__`                | Length of an object                      | Lets you use `len(obj)`                                                                                    | `def __len__(self): return len(self.data)`       |
| `__getitem__`            | Index access                             | Enables `obj[i]` syntax                                                                                    | `def __getitem__(self, i): return self.items[i]` |
| `__setattr__`            | Called when setting attributes           | Controls `obj.x = 5` behavior                                                                              | Used in ORM models, dataclasses, etc.            |
| `__getattr__`            | Called when accessing missing attributes | Lets you define fallback lookups                                                                           | `def __getattr__(self, name): ...`               |
| `__call__`               | Makes an object callable                 | Lets you use `obj()` as if it were a function                                                              | `def __call__(self, *a): ...`                    |
| `__iter__` / `__next__`  | Iteration protocol                       | Enables `for x in obj`                                                                                     | Used in custom iterator classes                  |
| `__enter__` / `__exit__` | Context manager protocol                 | Used in `with` statements                                                                                  | `with MyContext():`                              |
| `__file__`               | Path to the current module file          | Used to build relative paths                                                                               | `os.path.dirname(__file__)`                      |
| `__doc__`                | Module or function docstring             | The first triple-quoted string in a file or function                                                       | `print(myfunc.__doc__)`                          |

---

### 🧩 The most common “main guard” pattern:

```python
if __name__ == "__main__":
    # Only runs if this file is executed directly,
    # not when imported from another module.
    main()
```

✅ Purpose:

* Prevents accidental execution of test or CLI code when imported.
* Makes scripts reusable both as **modules** and **standalone programs**.

---

###  Single Underscore Prefix (`_name`)

This is **not special syntax** like `__main__` — it’s a **naming convention** meaning **“internal use”** or **“private”** within that file or module.

| Syntax      | Meaning                                 | Behavior                                                                                                                        |
| :---------- | :-------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------ |
| `_name`     | Internal/private function or variable   | Shouldn’t be used outside the module; Python doesn’t enforce this strictly, but by convention it means “for internal use only.” |
| `__name`    | Name-mangled attribute (inside classes) | Python changes its name internally to prevent accidental access (`_ClassName__name`)                                            |
| `_` (alone) | Common throwaway variable               | Used when you don’t care about the value (e.g., `for _, v in data:` or `_tick` in your code)                                    |

### Example:

```python
def _call_loader(csv_path):
    """Internal helper — not meant to be imported elsewhere."""
    ...
```

→ The underscore tells readers:

> “This is a helper function for internal logic; don’t import or rely on it outside this module.”

It still works normally — Python won’t forbid access — but it signals **intent**.

---

## 🔹 Summary Table — Underscore Usage in Python

| Form                     | Meaning                         | Example                                  |
| ------------------------ | ------------------------------- | ---------------------------------------- |
| `_variable`              | Private/internal use            | `_temp = 5`                              |
| `__variable`             | Name-mangled (inside classes)   | `self.__count` → becomes `_Class__count` |
| `__var__`                | Special system-defined name     | `__init__`, `__main__`, `__file__`       |
| `_`                      | Unused/throwaway placeholder    | `for _, value in pairs:`                 |
| `__name__ == "__main__"` | Check if script is run directly | Typical entrypoint guard                 |

---

## 🧠 Quick Analogy

Think of it like:

* `__double__` = “Python’s reserved words”
* `_single` = “private helper”
* `no underscore` = “public interface”

