# Python 

## Table of Contents

- [Tutorial videos](#tutorial-vids)
- [Documentation](#documentation)
- [Python00 (Basics)](Python00/README.md)
- [Python01 (Exercises)](Python01/README.md)
- [Python02 (Data & CSV)](Python02/README.md)
- [Python03 (OOP)](Python03/README.md)
- [Python04 (Functions & Decorators)](Python04/README.md)
---

## Tutorial videos
- Python for Beginners – Full Course [Programming Tutorial]
https://www.youtube.com/watch?v=eWRfhZUzrAc

- Python Tutorial for Beginners - Learn Python in 5 Hours [FULL COURSE]
https://www.youtube.com/watch?v=t8pPdKYpowI

## Documentation
- Python Standard Library
https://docs.python.org/3/library/

- Python Tutorial
https://www.w3schools.com/python/

- Beginner's Guide to Python
https://wiki.python.org/moin/BeginnersGuide

---

## 0️⃣ Python00
### Basic Types
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

```
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
```

### Packaging
- Python Package setup :
https://hackmd.io/@QBrv51OvRPqs9dJjL2YIig/rkA5azaall

---

## 1️⃣ Python01
### libraries
- numbPy explain : https://hackmd.io/@QBrv51OvRPqs9dJjL2YIig/rkWhZSaaxx
- PIL(Pillow) explain : https://hackmd.io/@QBrv51OvRPqs9dJjL2YIig/r1b6q_C6eg
- Brief on image handling libraries : https://hackmd.io/@QBrv51OvRPqs9dJjL2YIig/Sk13McAaee

### Concept Correcting

#### 🧱 1️⃣ “No code in the global scope”

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

#### ⚙️ 2️⃣ `if __name__ == "__main__":`

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

#### ⚡ 3️⃣ “Any exception not caught will invalidate the exercise”

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

#### 📖 4️⃣ “All your functions must have a documentation (**doc**)”

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

#### 🧰 5️⃣ Flake8 — the “norm” checker

##### 🔹 English

`flake8` is a **style and syntax checker**.
It ensures your code follows the official **Python coding standard (PEP 8)**.

Install and use:

```bash
pip install flake8
alias norminette=flake8
norminette yourfile.py
```

It checks:

* Indentation (4 spaces)
* Line too long (>79 chars)
* Missing docstrings
* Unused imports
* Code in global scope (forbidden)

##### 🔹 中文（繁體）

`flake8` 是一個 **Python 程式規範檢查工具**。
會自動幫你檢查程式是否符合 Python 標準（PEP8）。

它會檢查：

* 縮排（4 個空白）
* 每行長度
* 是否有文件字串（docstring）
* 是否有未使用的變數或 import
* 是否有在全域範圍直接執行程式

---

#### 🧠 Special Variables Explained

| Name       | English Explanation                                      | 中文解釋                         |
| ---------- | -------------------------------------------------------- | ---------------------------- |
| `__name__` | Identifier of the module; `"__main__"` when run directly | 模組名稱；當直接執行檔案時等於 `"__main__"` |
| `__main__` | The name Python assigns to the top-level script          | Python 對主程式檔案給的名稱            |
| `__doc__`  | String containing the function’s documentation           | 函式或模組的文件字串（說明文字）             |


#### 🧭 Summary Table

| Concept        | Rule                                       | Example                           | 中文說明               |
| -------------- | ------------------------------------------ | --------------------------------- | ------------------ |
| No global code | Only define functions, no direct execution | `main()` only                     | 不要在全域範圍執行程式        |
| Entry point    | `if __name__ == "__main__":`               | Run only if executed directly     | 只在被直接執行時才呼叫 main() |
| Documentation  | Use `"""..."""` docstring                  | Inside every function             | 每個函式必須有說明文字        |
| Error Handling | `try / except`                             | Catch all possible runtime errors | 必須處理所有例外錯誤         |
| Code Style     | `flake8`                                   | Check style and docstrings        | 程式必須符合 PEP8 規範     |

---

#### 🧩 Python *can* run code globally

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

#### 🚫 Why the subject forbids global code

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

#### ⚙️ 2️⃣ How `__name__` and `"__main__"` work

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

###### 🇹🇼 中文（繁體）

#### ✅ Python 可以在全域範圍執行程式碼

當你在檔案最外層（非函式或類別中）寫程式碼時，
它會 **立即被執行**，無論是直接執行或是被匯入。

範例：

```python
# 檔案：hello.py
print("這行會直接執行")
```

執行：

```
python hello.py
```

結果：

```
這行會直接執行
```

當你在別的檔案：

```python
import hello
```

也會輸出同樣內容（因為全域程式碼會被執行）。

---

#### 🚫 為什麼題目要求不要用全域程式碼？

因為如果別的程式或測試檔匯入你的模組，
它就會「不小心」執行到你的程式。
所以題目要求把所有邏輯都放在 `main()` 裡面，
並用：

```python
if __name__ == "__main__":
    main()
```

## Exercise learner notes (moved from exercise source files)

These concise learner notes were moved from inline comment blocks in
the exercise source files into this central location. They summarize
the important libraries, Python idioms, and behaviors used in each
exercise so you can quickly review them while working through the
materials.

ex00 — BMI utilities (ex00/give_bmi.py)
- Uses the standard library only (``sys`` for CLI integration).
- Concepts: type hints (``list[int | float]``), list comprehensions,
    ``zip`` to pair corresponding items, ``isinstance`` checks and
    explicit ``raise`` for input validation, and the ``if __name__ == '__main__'``
    guard to keep modules import-safe.

ex01 — 2D array slicing (ex01/array2D.py)
- NumPy (``import numpy as np``) provides ndarrays, fast numeric ops
    and convenient slicing. Use ``np.array(list_of_lists)`` to convert
    Python lists, inspect ``.ndim`` and ``.shape``, slice rows with
    ``arr[start:end]``, and convert back to Python lists with
    ``.tolist()`` when needed.

ex02 — Image loader (ex02/load_image.py)
- Pillow (PIL) for image I/O and NumPy for numeric arrays; ``Path``
    from pathlib improves cross-platform path handling.
- Patterns: ``Image.open(path)`` and ``.convert('RGB')`` to ensure
    3-channel images; ``np.array(img)`` yields a (H, W, C) ndarray.
    The loader uses a repository-local fallback path and returns ``None``
    (and prints to stderr) on failure to keep demos simple.

ex03 — Zoom & grayscale (ex03/zoom.py)
- Uses NumPy for array math, Pillow for resizing (``Image.fromarray``),
    and matplotlib for display.
- Key syntax: ``rgb[..., :3]`` to select channels, ``np.dot`` with
    luminance weights to convert RGB→grayscale, and ``astype(np.uint8)``
    to cast floats to byte-range values. The code defends against ``None``
    inputs and handles ``KeyboardInterrupt`` cleanly during display.

ex04 — Crop / transpose (ex04/rotate.py)
- Same loader pattern (Pillow + NumPy). Cropping uses array slicing to
    extract centered squares; transposing uses ``.T`` to swap axes. For
    color images the example converts to grayscale so the transpose is 2D.

ex05 — Filters and display (ex05/pimp_image.py)
- Demonstrates NumPy filters: inversion (``255 - arr``), channel masking
    (``arr[:, :, 1] = 0``), and grayscale stacking.
- Shows process helpers: module-level collection of results, ``atexit.register``
    to display on normal exit, and SIGINT handling to close GUI windows on Ctrl+C.


來控制只在「直接執行」時執行，不在匯入時執行。

---

### ⚙️ `__name__` 與 `"__main__"` 的關係

Python 會自動設定一個特殊變數：

* 當直接執行檔案時 → `__name__ = "__main__"`
* 當被匯入時 → `__name__ = "檔案名稱"`

所以：

```python
if __name__ == "__main__":
```

代表「僅當此檔案被直接執行時，才執行以下程式」。

---

#### 🧠 中文摘要表

| 狀況                      | `__name__` 的值 | 是否執行 `if __name__ == "__main__"` |
| ----------------------- | ------------- | -------------------------------- |
| 直接執行檔案 (`python 檔案.py`) | `"__main__"`  | ✅ 會執行                            |
| 被匯入成模組 (`import 檔案`)    | `"檔案名稱"`      | ❌ 不執行                            |

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

## 2️⃣ Python02 
Excellent question — this gets into some of Python’s most important conventions and special syntax.
Let’s go step-by-step so it’s crystal clear.

---

## 🔹 1. `__main__` and Double Underscores (`__name__`, etc.)

Python uses **double underscores** (`__like_this__`) for *special built-in names* — also known as **dunder names** ("double underscore").
They’re not just decoration — they have special meanings in the Python runtime.

Here’s a clear table of the **most relevant ones** you’ll see often:

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

## 🔹 2. Single Underscore Prefix (`_name`)

Now, about `_call_loader` and that **underscore prefix**.

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

---


## 3️⃣ Python03
## 4️⃣ Python04



```bash
¬_¬　ᙏ̤̫　ᕑᗢᓫ 　　. ̫ .　ꪔ̤̮　ꈍꈊꈍ ꪔ̤̥

ꪔ̤̱　ᴗ ·̫ ᴗ　･o･　˃̵ᴗ˂̵　·ꙫ·　˙³˙　˙Ⱉ˙ 　

◞‸◟　•ᴥ•　`з´　˘ᗜ˘　ᵔᴥᵔ　°⌓°　 •̆₃•̑ 

˃̵ ֊ ˂̵　˶’ᵕ‘˶　´••` 　ᵔ⤙ᵔ 　 ͒•∘̬• ͒　•᎔•　՞••՞

ᵒ̴̶̷̥́ ·̫ ᵒ̴̶̷̣̥̀　•᷄ࡇ•᷅⠀ꃋᴖꃋ　ˆ𐃷ˆ　

> 𐢭 <　'ㅅ'　ᵔᴗᵔ　˃ᴗ˂　ᴖ.ᴖ⠀'

•⤙•　• ﻌ -　•︿•̀　 >ᯅ<　 •͈ ₃ •͈

>ヮ<⠀ ⠀ ˃̵ᴗ˂̵⠀⠀ ᴖ ᴈ ᴖ ⠀⠀ ᵔᴗᵔ 

ꃋᴖꃋ ⠀⠀ ˘ᵕ˘⠀⠀ ˘͈ᵕ˘͈⠀⠀ •᷄ࡇ•᷅ 

⇀‸↼‶ ⠀⠀⎚-⎚⠀ ⠀ `⎚⩊⎚´⠀ ⠀ >ㅅ<

ˆ𐃷ˆ ⠀⠀ ⪩. .⪨⠀⠀ ＞ᨓ＜ ⠀ ⠀ᯣ_ᯣ
```