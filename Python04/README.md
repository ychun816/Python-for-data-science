
### Recommended Learning Resources for Python04

1. **Python Functions & Arguments**

   * *Concepts*: `*args`, `**kwargs`, default values, error handling
   * Resources: [Real Python – Python Functions](https://realpython.com/defining-your-own-python-function/)

2. **Decorators**

   * *Concepts*: Function wrappers, `@decorator` syntax, limiting function calls
   * Resources: [Python Docs – Decorators](https://docs.python.org/3/glossary.html#term-decorator)

3. **Closures**

   * *Concepts*: Functions returning functions, state retention, nonlocal variables
   * Resources: [Programiz – Python Closures](https://www.programiz.com/python-programming/closure)

4. **Data Classes**

   * *Concepts*: `@dataclass`, `field()`, immutable fields, auto-generated `__init__`
   * Resources: [Python Docs – Data Classes](https://docs.python.org/3/library/dataclasses.html)

5. **Random & String Operations**

   * *Concepts*: `random.choices`, string manipulation
   * Resources: [Python Docs – Random Module](https://docs.python.org/3/library/random.html)

---

### Key Concepts by Exercise

| Exercise | Task                                                     | Key Python Concepts                                         | Notes for Learning                                                                         |
| -------- | -------------------------------------------------------- | ----------------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| 00       | Calculate statistics (mean, median, quartiles, std, var) | `*args`, `**kwargs`, error handling, basic math             | Learn how to handle variable arguments and compute statistics manually                     |
| 01       | Outer/Inner functions                                    | Functions, closures, returning callable objects             | Understand how inner functions retain state and can be called repeatedly                   |
| 02       | Call limit decorator                                     | Decorators, `@decorator` syntax, function wrappers          | Learn to write a decorator that tracks function calls and enforces limits                  |
| 03       | Student dataclass                                        | `@dataclass`, `field()`, random ID generation, immutability | Learn how to auto-generate `__init__`, use default values, and restrict certain attributes |

---

## ex00
Notes for this exercise
----------------------


Formulas
| Statistic | Formula / Method                         |
| --------- | ---------------------------------------- |
| Mean      | sum(numbers) / len(numbers)              |
| Median    | middle value after sorting               |
| Quartile  | Q1 = 25%, Q3 = 75% (sort + pick indices) |
| Variance  | sum((x - mean)^2)/n                      |
| Std Dev   | sqrt(variance)                           |

```
          +----------------+
          |  ft_statistics |
          +----------------+
                   |
                   v
         +-------------------+
         | Filter numeric    |
         | args -> numbers   |
         +-------------------+
                   |
                   v
          +----------------+
          | Sort numbers    |
          +----------------+
                   |
                   v
   +------------------------------+
   | Process **kwargs requests     |
   +------------------------------+
        |        |       |      |
        v        v       v      v
     mean()    median() quartile() ...
        |        |       |      |
        +--------+-------+------+
                   |
                   v
            Print results
                   |
               End function

```
1. Input numbers and kwargs enter ft_statistics.
4. Each requested statistic in kwargs is calculated using the mapped helper function.
5. Results are printed.


## **1️⃣ Summary Table – Python Ex00 Functions & Syntax**
| `mean(nums)`                                                                    | Average of numbers                             | 平均數 / 平均值            | Add all numbers, divide by count                       |
| `median(nums)`                                                                  | Middle value after sorting                     | 中位數                  | If odd: pick middle; even: average two middle          |
| `quartile(nums)`                                                                | 25% (Q1) & 75% (Q3) positions                  | 四分位數                 | Q1 = n//4 index, Q3 = 3n//4 index                      |
| `variance(nums)`                                                                | How far numbers are from mean                  | 變異數                  | sum((x-mean)^2)/n                                      |
| `std_dev(nums)`                                                                 | Typical distance from mean                     | 標準差                  | sqrt(variance) (iterative)                             |
| `for j in range(0, n-i-1): numbers[j], numbers[j+1] = numbers[j+1], numbers[j]` | Swap two numbers if out of order (Bubble Sort) | 冒泡排序交換               | Loops over array indexes, swaps if needed              |
| `mid = n // 2`                                                                  | Find middle index                              | 取整數除法找中間索引           | Used for median                                        |
| `return (nums[mid-1] + nums[mid]) / 2`                                          | Median for even count                          | 偶數個數字取中間兩個平均         | Example: [1,3,5,7] → (3+5)/2=4                         |
| `return nums[mid]`                                                              | Median for odd count                           | 奇數個數字直接取中間數          | Example: [1,3,5] → 3                                   |
| `sum((x - m)**2 for x in nums) / len(nums)`                                     | Compute variance                               | 計算平方差平均              | Each x subtract mean, square, sum, divide by n         |
| `for key in kwargs: ...`                                                        | Process requested statistics                   | 處理 keyword arguments | Lookup stat in dictionary, call function, print result |


## **2️⃣ ASCII Diagram – How Each Number is Processed**

Imagine we have numbers: `[2, 4, 6]`

```
Step 1: Input Numbers
[2, 4, 6]

Step 2: Mean Calculation
total = 0
Add 2 -> total=2
Add 4 -> total=6
Add 6 -> total=12
Mean = total / 3 = 4
------------------------

Step 3: Median Calculation
Sort numbers -> [2,4,6] (already sorted)
Length = 3 (odd)
Middle index = 3//2 = 1
Median = nums[1] = 4
------------------------

Step 4: Quartile Calculation
Q1 index = 3//4 = 0 -> Q1 = nums[0] = 2
Q3 index = 3*3//4 = 2 -> Q3 = nums[2] = 6
Quartile = [2,6]
------------------------

Step 5: Variance Calculation
Mean = 4
Differences: [2-4, 4-4, 6-4] -> [-2,0,2]
Squared differences: [4,0,4]
Sum = 8
Variance = 8 / 3 ≈ 2.667
------------------------

Step 6: Standard Deviation
Variance = 2.667
Approximate sqrt using iteration:
x0 = 2.667
Iteration -> converge to √2.667 ≈ 1.632
Std Dev ≈ 1.632
------------------------
```



* Numbers → Mean → Median → Quartiles → Variance → Std Dev
* Bubble sort, indexing, squaring, summing, and square root are all applied manually.

---

## ex01

| Function             | Description                                                                                                                                  |
| -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| `square(x)`          | Returns (x^2) → 平方                                                                                                                           |
| `pow(x)`             | Returns (x^x) → 自身的次方                                                                                                                        |
| `outer(x, function)` | Returns an object (closure) that can be called multiple times. Keeps internal state `count` and applies `function` to `x`. → 外層函數，返回可重複呼叫的物件 |

1. `inner()` is the actual callable returned by `outer()`.
2. No globals allowed, so we must use `closures` (nonlocal keyword) to store state.

Notes for this exercise
----------------------

- Implementation details: `square(x)` returns x * x. `pow(x)` returns x ** x.
- `outer(x, function)` returns a closure that stores an internal `current`
   value initialized to `x`. Each call to the returned `inner()` applies the
   provided `function` to the previous `current` value, updates `current`, and
   returns the new value. This matches the exercise expectation where each
   subsequent call applies the function to the previous result (not to x with
   an increasing exponent).
- No global variables are used; `nonlocal` is used to maintain closure state.
- Style: the module passes `flake8` checks in this environment.

Example behavior (from `tester.py`):

```
my_counter = outer(3, square)        # returns closure
my_counter() -> square(3) -> 9
my_counter() -> square(9) -> 81
my_counter() -> square(81) -> 6561
```



| Function / Concept | English                 | 中文解釋              |
| ------------------ | ----------------------- | ----------------- |
| square             | x^2                     | 平方                |
| pow                | x^x                     | 自身次方              |
| outer              | returns callable object | 外層函數，返回可呼叫物件      |
| inner              | closure function        | 內層函數，記住外層變數狀態     |
| nonlocal           | modifies outer variable | 可以修改外層變數，而不是建立新變數 |

Excellent 👏 — you’re now moving into **Python04 – Ex01: Outer_Inner**, which is about **closures and higher-order functions** (functions returning functions).
Let’s break this down **visually, syntactically, and conceptually** — nice and easy for beginners.

## 🧩 1️⃣ ASCII Workflow Diagram – `square`, `pow`, `outer`, `inner`

```
          +-------------------+
          |     main tester   |
          +-------------------+
                 |
                 v
     +-------------------------+
     | call outer(x, function) |
     +-------------------------+
                 |
                 v
       +-------------------+
       | outer() creates   |
       |   local variable  |
       |   count = 0       |
       | defines inner()   |
       | returns inner     |
       +-------------------+
                 |
                 v
        inner() returned
           as object
                 |
        +--------------------+
        | each call to inner |
        | uses same count    |
        | applies function(x)|
        | updates x = result |
        | increases count    |
        +--------------------+
                 |
                 v
       +--------------------+
       | function used:     |
       |  - square(x)       |
       |  - pow(x)          |
       +--------------------+
                 |
                 v
       +--------------------+
       | square(x): x*x     |
       | pow(x): x**x       |
       +--------------------+
```

**So the “flow” is:**
`outer()` defines → returns → `inner()` remembers `x` and `count`
Each time you call `inner()`, it applies the math function again and again, using the **updated x**.

---

## 🧮 2️⃣ Function Logic Explained Simply

| Function             | English                                           | 中文解釋              | Example                                    |
| -------------------- | ------------------------------------------------- | ----------------- | ------------------------------------------ |
| `square(x)`          | Returns x × x                                     | 平方（乘自己一次）         | 3 → 9                                      |
| `pow(x)`             | Returns x ^ x (x to the power of itself)          | 次方（x 的 x 次方）      | 3 → 27                                     |
| `outer(x, function)` | Creates and returns a “closure” that remembers x  | 外部函數：建立記憶 x 的內部函數 | Returns inner()                            |
| `inner()`            | Uses function on x, remembers new value each time | 內部函數：對 x 運算並保存新結果 | Keeps multiplying or powering on each call |

---

## 🧠 3️⃣ Syntax Explained

### 🔹 `for _ in range(int(x)):`

* The underscore `_` is just a **throwaway variable** — it means:

  > “I need to loop, but I don’t care about the variable name.”

So instead of writing:

```python
for i in range(3):
```

You can write:

```python
for _ in range(3):
```

➡ It loops 3 times but ignores the loop variable.

🈶 中文：
`_` 是「我不需要這個變數」的意思。只是為了執行固定次數的迴圈而用。

---

## 🔄 4️⃣ Relation Between `outer()` and `inner()`

| Concept      | English                                                                | 中文解釋                   |
| ------------ | ---------------------------------------------------------------------- | ---------------------- |
| `outer()`    | Defines a variable (like `x`, `count`) and defines `inner()` inside it | 外部函數建立本地變數並定義內部函數      |
| `inner()`    | Uses the `x` and `count` from `outer()` even after `outer()` finished  | 內部函數記住外部變數（閉包 closure） |
| Relationship | `inner()` **closes over** variables from `outer()`                     | `inner()` 封閉外部變數形成閉包   |

So every time you call:

```python
my_counter = outer(3, square)
print(my_counter())
```

`inner()` runs with access to `x=3` and `function=square`.

Next time you call `my_counter()`,
`x` has already changed → result gets “grown”.

---

## 📝 5️⃣ Example Docstrings (`""" """`) You Can Put

```python
def outer(x: int | float, function):
    """
    Creates a closure that applies a given function
    to a starting number `x` every time it is called.

    Parameters:
        x (int | float): starting value
        function (callable): function to apply repeatedly

    Returns:
        inner (function): callable object that computes the next result each call
    """
```

```python
def inner() -> float:
    """
    Applies the stored function to the stored number `x`,
    updates `x` with the result, and returns the new value.
    """
```

---

## 💡 Visual Example Flow (for 3, square)

```
outer(3, square)  ---> returns inner()
↓
call 1: inner() → 3² = 9
call 2: inner() → 9² = 81
call 3: inner() → 81² = 6561
```

For `outer(1.5, pow)`

```
outer(1.5, pow) → returns inner()
↓
call 1: inner() → 1.5¹·⁵ = 1.837
call 2: inner() → 1.837¹·⁸³⁷ = 3.056
call 3: inner() → 3.056³·⁰⁵⁶ = 30.426
```

---

## ex02 

Step-by-step breakdown
| Layer | Function name                   | Purpose                                             | What it returns                                |
| ----- | ------------------------------- | --------------------------------------------------- | ---------------------------------------------- |
| 1️⃣   | `callLimit(limit)`              | outer function — stores the `limit` value           | returns `callLimiter`                          |
| 2️⃣   | `callLimiter(function)`         | inner function — gets the function to decorate      | returns `limit_function`                       |
| 3️⃣   | `limit_function(*args, **kwds)` | wrapper — controls how many times the function runs | returns result of `function()` or prints error |
- `callLimit(limit)` is a decorator factory: it returns a decorator which,
   when applied to a function, returns a wrapper that allows the function to
   run `limit` times. Subsequent calls print an error message and the original
   function is not executed.
- The implementation uses a `nonlocal` counter in the closure returned by
   `callLimit(limit)` so each decorated function keeps its own call count.
- Error message formatting matches the subject: "Error: <function ...> call too many times".
- No global variables are used; the state is kept in the closure.


Workflow Diagram
```
@callLimit(3)
   │
   ├── callLimit(limit=3)
   │      ↓
   │   returns callLimiter
   │
   ├── callLimiter(function=f)
   │      ↓
   │   defines limit_function()
   │   count = 0
   │      ↓
   └── returns limit_function (the wrapped f)
           ↓
        f() → count++ until 3, then error printed
```

🔸 `nonlocal`
- Lets inner function modify variable defined in an outer (non-global) scope.
- Without nonlocal, count inside limit_function would create a new local variable.

🔸 `*args, **kwds`
- Allows your decorator to handle any number of arguments the decorated function may have.

Iteration Table
```
Step | Function Called | count before | count after | Output
-----|----------------|--------------|------------|---------
 1   | f()            | 0            | 1          | f()
 2   | g()            | 0            | 1          | g()
 3   | f()            | 1            | 2          | f()
 4   | g()            | 1            | 1 (no change) | Error: <function g ...> call too many times
 5   | f()            | 2            | 3          | f()
 6   | g()            | 1            | 1 (no change) | Error: <function g ...> call too many times

```
Visual flow:
```
f() -> [count=0] -> f() executed -> count=1
f() -> [count=1] -> f() executed -> count=2
f() -> [count=2] -> f() executed -> count=3
f() -> [count=3] -> limit reached -> Error
g() -> [count=0] -> g() executed -> count=1
g() -> [count=1] -> limit reached -> Error
```

ASCII Visual Flow — Memory Allocation Step by Step
```
Step 1: callLimit(3) for f
┌─────────────┐
│ limit = 3   │  ← Layer 1 frame
│ callLimiter │  ← returns this
└─────────────┘

Step 2: callLimiter(f)
┌─────────────┐
│ function=f  │  ← Layer 2 frame
│ count=0     │
│ limit_function -> wrapper function │
└─────────────┘
f now points to limit_function

Step 3: call f()
┌─────────────┐
│ limit_function call frame │ ← Layer 3
│ count (nonlocal) = 0     │
│ executes f()              │
└─────────────┘
count increments → count=1

Step 4: repeat calls → count increments until limit

```
- Each decorated function has its own count variable in memory.
- `nonlocal` ensures the wrapper can update count in its enclosing scope.


💾 Memory Layout after Decoration
```
Memory (simplified view)
─────────────────────────────────────────────
callLimit(3) → returns callLimiter
f = callLimiter(f) → limit_function wrapper
─────────────────────────────────────────────
f (name) ──────► limit_function (wrapper)
                   │
                   │ nonlocal count = 0
                   │ points to original function f()
                   ▼
               f() code (original function)
─────────────────────────────────────────────
callLimit(1) → returns callLimiter
g = callLimiter(g) → limit_function wrapper
─────────────────────────────────────────────
g (name) ──────► limit_function (wrapper)
                   │
                   │ nonlocal count = 0
                   │ points to original function g()
                   ▼
               g() code (original function)
─────────────────────────────────────────────

```


🧱 Summary Table
| Concept                                           | Meaning                                                  | Example in code                 |
| ------------------------------------------------- | -------------------------------------------------------- | ------------------------------- |
| `decorator`                                       | A function that modifies another function’s behavior     | `@callLimit(3)`                 |
| `closure`                                         | Inner function remembering variables from outer function | `count` inside `limit_function` |
| `nonlocal`                                        | Lets inner function modify variable from parent scope    | `nonlocal count`                |
| `*args, **kwds`                                   | Flexible arguments for wrapper                           | `limit_function(*args, **kwds)` |
| `print(f"Error: {function} call too many times")` | Error message                                            | printed after limit exceeded    |


🔹 How it works during calls
Step 1: f() called
```
f() called
┌─────────────┐
│ limit_function wrapper │
│ count = 0 → 1         │
│ executes original f() │
└─────────────┘
```
Step 2: g() called
```
g() called
┌─────────────┐
│ limit_function wrapper │
│ count = 0 → 1         │
│ executes original g() │
└─────────────┘
```
Step 3: g() called again
```
g() called
┌─────────────┐
│ limit_function wrapper │
│ count = 1             │
│ limit reached → prints │
│ "Error: <function g ...> call too many times" │
└─────────────┘
```

--- 

## ex03

ASCII Memory / Workflow Diagram

```
Student(name='Edward', surname='agle')
│
├─ auto __init__ sets: name='Edward', surname='agle', active=True
│
├─ __post_init__ runs:
│   ├─ login = surname.capitalize() → 'Agle'
│   └─ id = generate_id() → 'trannxhndgtolvh'
│
└─ Student object created:
    ┌─────────────────────────────┐
    │ name='Edward'               │
    │ surname='agle'              │
    │ active=True                 │
    │ login='Agle'                │
    │ id='trannxhndgtolvh'        │
    └─────────────────────────────┘

```

Perfect! Let’s create a **detailed lifecycle diagram** for a single `Student` object, showing **memory boxes** for the class, `__init__`, `__post_init__`, and the final object state.

---

### Example: Creating `student = Student(name="Edward", surname="agle")`

```
Step 0: Class Definition in Memory
────────────────────────────────────────────
Student class:
┌─────────────────────────────┐
│ Fields:                     │
│  name: str                  │
│  surname: str               │
│  active: bool = True        │
│  login: str (init=False)    │
│  id: str (init=False)       │
│ Methods:                    │
│  __init__ (auto-generated)  │
│  __post_init__              │
└─────────────────────────────┘

Step 1: Call __init__
────────────────────────────────────────────
student = Student(name="Edward", surname="agle")
┌─────────────────────────────┐
│ __init__ execution frame     │
│ name = "Edward"             │
│ surname = "agle"            │
│ active = True               │
│ login = <uninitialized>     │
│ id = <uninitialized>        │
└─────────────────────────────┘

Step 2: __post_init__ runs
────────────────────────────────────────────
__post_init__ frame:
┌─────────────────────────────┐
│ login = surname.capitalize()│ → "Agle"
│ id = generate_id()          │ → random string e.g. "trannxhndgtolvh"
└─────────────────────────────┘
Memory updated for student object:
┌─────────────────────────────┐
│ student                     │
├─ name='Edward'              │
├─ surname='agle'             │
├─ active=True                │
├─ login='Agle'               │
└─ id='trannxhndgtolvh'       │
└─────────────────────────────┘
```

Notes for this exercise
----------------------

Implementation summary
- Prototype (core parts):

```python
import random
import string
from dataclasses import dataclass, field

def generate_id() -> str:
      return "".join(random.choices(string.ascii_lowercase, k=15))

@dataclass
class Student:
      name: str
      surname: str
      active: bool = True
      login: str = field(init=False)
      id: str = field(init=False)

      def __post_init__(self):
            # set login and id here
            ...
```

- Login rule: the login is created by taking the first letter of `name`,
   uppercasing it, and concatenating the full `surname` (example: name="Edward",
   surname="agle" → login="Eagle"). This exact rule is implemented in
   `__post_init__`.
- ID generation: `generate_id()` returns a random 15-letter lowercase string
   using `random.choices(string.ascii_lowercase, k=15)`.
- `login` and `id` are declared with `field(init=False)`, so they are not
   arguments of the generated `__init__` and attempts to pass them (for
   example `Student(..., id='toto')`) raise a `TypeError`.
- No custom `__repr__` / `__str__` methods are provided; the dataclass's
   default representation is used by `print(student)` and matches the
   exercise output format.
- Only the allowed standard modules are used: `dataclasses`, `random`, and
   `string`.

Tester note
- The exercise tester now creates a Student and prints it:

```python
student = Student(name="Edward", surname="agle")
print(student)
```

This prints a line similar to:
`Student(name='Edward', surname='agle', active=True, login='Eagle', id='<random>')`

Linting
- The module passes `flake8` in this environment.


---

### 🔹 Lifecycle Summary

1. **Class loaded** → stores field definitions and methods.
2. **`__init__` called** → sets user-provided fields (`name`, `surname`) and default (`active`), leaves `login` and `id` uninitialized.
3. **`__post_init__` called** → sets derived fields (`login`, `id`) after `__init__`.
4. **Final Student object** → all fields are initialized, ready to use.
5. **Attempts to initialize `login` or `id` in `__init__`** → `TypeError` because `init=False`.


✅ Summary Table
| Feature             | Purpose                                           | Implementation                                          |
| ------------------- | ------------------------------------------------- | ------------------------------------------------------- |
| `@dataclass`        | Auto-generates `__init__`                         | `@dataclass` decorator                                  |
| `field(init=False)` | Prevent user from initializing certain attributes | `login` and `id`                                        |
| `__post_init__`     | Run code after auto `__init__`                    | Set login & id                                          |
| `generate_id()`     | Create random ID                                  | `"".join(random.choices(string.ascii_lowercase, k=15))` |
| `login`             | Derived from surname                              | `self.login = self.surname.capitalize()`                |


