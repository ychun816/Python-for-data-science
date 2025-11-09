# Python 

### Tutorial vids
- Python for Beginners – Full Course [Programming Tutorial]
https://www.youtube.com/watch?v=eWRfhZUzrAc

- Python Tutorial for Beginners - Learn Python in 5 Hours [FULL COURSE]
https://www.youtube.com/watch?v=t8pPdKYpowI

### Documentation
- Python Standard Library
https://docs.python.org/3/library/

- Python Tutorial
https://www.w3schools.com/python/

- Beginner's Guide to Python
https://wiki.python.org/moin/BeginnersGuide



## Python 00
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


## Python 01
### libraries
- numbPy explain : https://hackmd.io/@QBrv51OvRPqs9dJjL2YIig/rkWhZSaaxx
- PIL(Pillow) explain : https://hackmd.io/@QBrv51OvRPqs9dJjL2YIig/r1b6q_C6eg
- Brief on image handling libraries : https://hackmd.io/@QBrv51OvRPqs9dJjL2YIig/Sk13McAaee

### Concept Correcting

非常好 🌟 這是學習專業 Python 開發的重要一步。
以下我會用 **英文 + 繁體中文對照** 詳細說明每個重點。

---

## 🧱 1️⃣ “No code in the global scope”

### 🔹 English

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

### 🔹 中文（繁體）

不要在「全域範圍（global scope）」直接執行程式。
只能在這裡**定義函式或類別**。

當別人 `import` 你的檔案時，不應該自動執行程式。

---

## ⚙️ 2️⃣ `if __name__ == "__main__":`

### 🔹 English

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

### 🔹 中文（繁體）

每個 Python 檔案都有內建變數 `__name__`。

* 當你直接執行該檔案時，`__name__` 會等於 `"__main__"`。
* 當你從別的檔案匯入（import）時，`__name__` 會等於該檔案的名稱。

這樣可以讓程式區分「被執行」和「被匯入」的情況。

---

## ⚡ 3️⃣ “Any exception not caught will invalidate the exercise”

### 🔹 English

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

### 🔹 中文（繁體）

必須用 `try / except` 處理例外（error）。
如果執行時發生錯誤但沒有被捕捉 → 作業算無效。

---

## 📖 4️⃣ “All your functions must have a documentation (**doc**)”

### 🔹 English

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

### 🔹 中文（繁體）

`__doc__` 是 Python 函式的**文件字串（docstring）**。
用來說明：

* 函式的功能
* 參數的型別與用途
* 回傳值的說明

所有函式都必須有這樣的說明註解。

---

## 🧰 5️⃣ Flake8 — the “norm” checker

### 🔹 English

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

### 🔹 中文（繁體）

`flake8` 是一個 **Python 程式規範檢查工具**。
會自動幫你檢查程式是否符合 Python 標準（PEP8）。

它會檢查：

* 縮排（4 個空白）
* 每行長度
* 是否有文件字串（docstring）
* 是否有未使用的變數或 import
* 是否有在全域範圍直接執行程式

---

## 🧠 Special Variables Explained

| Name       | English Explanation                                      | 中文解釋                         |
| ---------- | -------------------------------------------------------- | ---------------------------- |
| `__name__` | Identifier of the module; `"__main__"` when run directly | 模組名稱；當直接執行檔案時等於 `"__main__"` |
| `__main__` | The name Python assigns to the top-level script          | Python 對主程式檔案給的名稱            |
| `__doc__`  | String containing the function’s documentation           | 函式或模組的文件字串（說明文字）             |

---

## 🧭 Summary Table

| Concept        | Rule                                       | Example                           | 中文說明               |
| -------------- | ------------------------------------------ | --------------------------------- | ------------------ |
| No global code | Only define functions, no direct execution | `main()` only                     | 不要在全域範圍執行程式        |
| Entry point    | `if __name__ == "__main__":`               | Run only if executed directly     | 只在被直接執行時才呼叫 main() |
| Documentation  | Use `"""..."""` docstring                  | Inside every function             | 每個函式必須有說明文字        |
| Error Handling | `try / except`                             | Catch all possible runtime errors | 必須處理所有例外錯誤         |
| Code Style     | `flake8`                                   | Check style and docstrings        | 程式必須符合 PEP8 規範     |

---

## 🧩 1️⃣ Yes — Python *can* run code globally

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

## 🚫 Why the subject forbids global code

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

## ⚙️ 2️⃣ How `__name__` and `"__main__"` work

Python automatically sets a special variable:

* `__name__ = "__main__"` when you **run** the file directly.
* `__name__ = "filename"` when you **import** it.

So this condition:

```python
if __name__ == "__main__":
```

means “run the next block **only when this file is executed directly**”.

---

## 🧠 English Explanation Summary

| Situation                            | `__name__` value | Code under `if __name__ == "__main__":` runs? |
| ------------------------------------ | ---------------- | --------------------------------------------- |
| Run directly with `python myfile.py` | `"__main__"`     | ✅ Yes                                         |
| Imported into another file           | `"myfile"`       | ❌ No                                          |

---

## 🇹🇼 中文（繁體）

### ✅ Python 可以在全域範圍執行程式碼

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

### 🚫 為什麼題目要求不要用全域程式碼？

因為如果別的程式或測試檔匯入你的模組，
它就會「不小心」執行到你的程式。
所以題目要求把所有邏輯都放在 `main()` 裡面，
並用：

```python
if __name__ == "__main__":
    main()
```

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

### 🧠 中文摘要表

| 狀況                      | `__name__` 的值 | 是否執行 `if __name__ == "__main__"` |
| ----------------------- | ------------- | -------------------------------- |
| 直接執行檔案 (`python 檔案.py`) | `"__main__"`  | ✅ 會執行                            |
| 被匯入成模組 (`import 檔案`)    | `"檔案名稱"`      | ❌ 不執行                            |

---

## 🧱 ASCII Workflow Diagram

### ❌ Without `main()` — global code (bad)

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

## 🧩 Summary

| Concept         | English                                         | 中文說明                      |
| --------------- | ----------------------------------------------- | ------------------------- |
| Global code     | Executes anytime file is imported or run        | 全域程式碼在匯入時也會執行             |
| Main function   | Groups the program logic                        | 用來包住主程式邏輯                 |
| `__name__`      | Special variable = `"__main__"` if run directly | 特殊變數，直接執行時等於 `"__main__"` |
| Rule in subject | Restrict all execution inside `main()`          | 作業要求所有執行都放在 main() 裡面     |

---

✅ **So your understanding is correct:**
Yes — Python *can* run code globally,
but in this project, they require you to **delimit (限制)** all execution to run **only inside `main()`** using

```python
if __name__ == "__main__":
    main()
```


---



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