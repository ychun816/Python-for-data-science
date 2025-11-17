# Python04 | Dod (Data Oriented Design)
[Back to Index](../README.md)
---
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

Formulas
| Statistic | Formula / Method                         |
| --------- | ---------------------------------------- |
| Mean      | sum(numbers) / len(numbers)              |
| Median    | middle value after sorting               |
| Quartile  | Q1 = 25%, Q3 = 75% (sort + pick indices) |
| Variance  | sum((x - mean)^2)/n                      |
| Std Dev   | sqrt(variance)                           |


| Name         | Explanation                                                                  | Formula                           | Example                                    |
| ------------ | ---------------------------------------------------------------------------- | --------------------------------- | ------------------------------------------ |
| **mean**     | The average of all numbers.                                                  | sum(nums) / n                     | `[1,2,3] → 2`                              |
| **median**   | The middle value in a sorted list. Average of 2 middle values if even count. | —                                 | `[1,3,5] → 3`; `[1,2,3,4] → (2+3)/2 = 2.5` |
| **quartile** | The 25% (Q1) and 75% (Q3) positions in sorted data. Simplified by index.     | Q1 = nums[n//4], Q3 = nums[3n//4] | For 8 values: Q1 = index 2, Q3 = index 6   |
| **variance** | Average of squared distance from the mean. Measures spread.                  | Σ(x−m)² / n                       | `[1,3,5] → 2.666...`                       |
| **std_dev**  | Square root of variance. Same units as data.                                 | √variance                         | sqrt(2.666) → 1.632                        |


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
                   v
               End function

```
1. Input numbers and kwargs enter ft_statistics.
2. Non-numeric values are filtered out.
3. The remaining numbers are sorted for median/quartile.
4. Each requested statistic in kwargs is calculated using the mapped helper function.
5. Results are printed.


## ** Summary Table – Python Ex00 Functions & Syntax**

| Function / Syntax                                                               | English Description                            | 中文解釋                 | Example / Notes                                        |
| ------------------------------------------------------------------------------- | ---------------------------------------------- | -------------------- | ------------------------------------------------------ |
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

| Syntax / Function                             | Explanation                                                                          | Usage Example                                            |
| --------------------------------------------- | ------------------------------------------------------------------------------------ | -------------------------------------------------------- |
| `*args: Any`                                  | Collects unlimited **positional arguments** into a tuple. Accepts any data type.     | `def f(*args): print(args)` → `f(1, 2, 3)` → `(1, 2, 3)` |
| `**kwargs: Any`                               | Collects unlimited **keyword arguments** into a dict, mapping key → value.           | `def f(**k): print(k)` → `f(a=1, b=2)` → `{'a':1,'b':2}` |
| `sorted()`                                    | Returns a **new sorted list** from any iterable.                                     | `sorted([3,1,2])` → `[1,2,3]`                            |
| `sqrt()`                                      | Square root function from `math`.                                                    | `math.sqrt(9)` → `3.0`                                   |
| `//` (floor division)                         | Integer division that **removes decimals**. Used for indexing.                       | `5 // 2` → `2`                                           |
| `sum()`                                       | Adds all elements of an iterable.                                                    | `sum([1,2,3])` → `6`                                     |
| `sum((x - m) ** 2 for x in nums) / len(nums)` | Formula for **population variance**. Generates squared deviations and averages them. | For `nums=[1,3,5]`, computes average of `(x-m)²`.        |
| `math.sqrt(variance(nums))`                   | Computes **standard deviation** (square root of variance).                           | `std = math.sqrt(var)`                                   |
| `stat_map = { "mean": mean, ... }`            | A **dispatcher dictionary** mapping text → function object.                          | `stat_map["mean"](nums)` calls the `mean` function       |
| `.values()`                                   | Gets all values from a dictionary (e.g., `"mean"`, `"median"`).                      | `{"a":1,"b":2}.values()` → `[1,2]`                       |
| `func()`                                      | Executes the function stored in `func`. Dynamic function call.                       | `func = mean; func([1,2,3])`                             |


## **2️⃣ ASCII Diagram**

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


---

## ex01


### 🧮 Function Logic & Explain

| Function / Concept | English                 | 中文解釋              |
| ------------------ | ----------------------- | ----------------- |
| square             | x^2                     | 平方                |
| pow                | x^x                     | 自身次方              |
| outer              | returns callable object | 外層函數，返回可呼叫物件      |
| inner              | closure function        | 內層函數，記住外層變數狀態     |
| nonlocal           | modifies outer variable | 可以修改外層變數，而不是建立新變數 |


| Function             | English                                           | 中文解釋              | Example                                    |
| -------------------- | ------------------------------------------------- | ----------------- | ------------------------------------------ |
| `square(x)`          | Returns x × x                                     | 平方（乘自己一次）         | 3 → 9                                      |
| `pow(x)`             | Returns x ^ x (x to the power of itself)          | 自身次方（x 的 x 次方）      | 3 → 27                                     |
| `outer(x, function)` | Returns callable object. Creates and returns a “closure” that remembers x  | 外部函數：建立記憶 x 的內部函數 | Returns inner()                            |
| `inner()`            | Uses function on x, remembers new value each time | 內部函數：對 x 運算並保存新結果 | Keeps multiplying or powering on each call |
| ` nonlocal`            | Modifies outer variable | 可以修改外層變數，而不是建立新變數 | - |


1. `inner()` is the actual callable returned by `outer()`.
2. No globals allowed, so we must use `closures` (nonlocal keyword) to store state.



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

## 📝 5️⃣ Example Docstrings (`""" """`) To put for `outer()` and `inner()`

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

Below is a **clean, structured, professional explanation** of **Ex01** in both **English and Traditional Chinese**, followed by a **summary table**, and then a **line-by-line commented explanation** of your provided code.

Everything is formatted so you can paste into `README.md`.

---

# ✅ **Summary Table — Key Takeaways (ENG + 繁中)**

### 📘 **Ex01 Core Concepts Summary**

| Concept / 概念                 | Explanation (English)                                                                  | 解說（繁體中文）                                      |
| ---------------------------- | -------------------------------------------------------------------------------------- | --------------------------------------------- |
| **Pure functions**           | `square()` and `pow()` return deterministic mathematical results with no side effects. | `square()` 與 `pow()` 是純函式，每次輸入相同，輸出也相同，沒有副作用。 |
| **Exponentiation**           | `x ** x` means "x to the power of x".                                                  | `x ** x` 表示「x 的 x 次方」。                        |
| **Closures**                 | An inner function (`inner()`) capturing variables from an outer function (`outer()`).  | 閉包：`inner()` 能使用 `outer()` 中的變數。              |
| **Function as argument**     | `outer(x, function)` receives a function and uses it dynamically.                      | `outer(x, function)` 接收一個函式並動態使用它。            |
| **Nonlocal variable**        | `nonlocal current` allows the inner function to modify variables from outer scope.     | `nonlocal current` 讓內層函式可修改外層區域變數。            |
| **Stateful function object** | The returned `inner()` keeps its own internal state (`current`).                       | 回傳的 `inner()` 保持自己的內部狀態 (`current`)。          |
| **No globals allowed**       | You must store state *inside* the closure, not in global variables.                    | 禁止使用 global，狀態必須放在閉包中。                        |
| **Repeated computation**     | Each call updates `current` using the provided function.                               | 每次呼叫都根據給定函式更新 `current`。                      |

---

# 📚 **Required Knowledge (ENG + 繁中)**

| Area / 領域                           | What you must understand (ENG)                                   | 必須理解（繁體中文）              |
| ----------------------------------- | ---------------------------------------------------------------- | ----------------------- |
| **Functions**                       | How to define, return, and pass functions.                       | 如何定義、回傳與傳遞函式。           |
| **Closures / Inner functions**      | Inner functions remember variables from the outer scope.         | 內部函式會記住外部函式的變數。         |
| **Nonlocal keyword**                | Allows modification of a variable defined in the outer function. | `nonlocal` 允許修改外層函式的變數。 |
| **Mathematics**                     | Square, exponentiation, iterative transformations.               | 平方、次方、重複運算邏輯。           |
| **Functional programming concepts** | Function returned as an object with state.                       | 函式回傳具有「狀態」的物件。          |

| Concept   | Explanation                                                                                                        | Example                                                                |
| --------- | ------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------- |
| `outer()` | A function that **contains** another function. It prepares data or logic, then returns the inner function.         | It may compute initial values, create closures, or configure behavior. |
| `inner()` | A function **defined inside** `outer()`. It can access variables from `outer()` even after `outer()` has finished. | Often used for decorators, closures, and customizing functions.        |
| Closure   | A mechanism where `inner()` keeps using variables defined in `outer()`.                                            | `inner()` can still read `x` defined in `outer()`.                     |
| Purpose   | Encapsulation, dynamic behavior, decorators, reusable logic patterns.                                              | Decorators wrap functions; closures generate custom functions.         |

| 概念          | 說明                                                     | 範例                                 |
| ----------- | ------------------------------------------------------ | ---------------------------------- |
| `outer()`   | **外層函式**，其內部定義 `inner()`。通常用來準備資料或設定行為，最後回傳 `inner()`。 | 可以在裡面建立初始數值、設定參數或配置邏輯。             |
| `inner()`   | **內層函式**，定義在 `outer()` 裡，因此可使用 `outer()` 的變數。          | 常見於 decorators、closures，以及客製化函式行為。 |
| 閉包（closure） | `inner()` 能夠持續使用 `outer()` 的變數，即使 `outer()` 已經結束執行。    | `inner()` 可以使用 `outer()` 裡的 x。     |
| 目的          | 封裝邏輯、動態產生函式、自訂行為、裝飾器模式。                                | 裝飾器包裹函式；閉包可產生特製的函式。                |


# 🧮 **What the Subject Wants You to Learn (ENG + 繁中)**

| Core Skill                 | ENG – What you learn                                         | 繁中 – 學到什麼      |
| -------------------------- | ------------------------------------------------------------ | -------------- |
| **Higher-order functions** | Passing functions into other functions.                      | 將函式傳給另一個函式。    |
| **Closures**               | Returning an inner function that captures and retains state. | 回傳具備記憶功能的內部函式。 |
| **State without globals**  | Using closure variables instead of global variables.         | 使用閉包變數代替全域變數。  |
| **Iterative computation**  | Applying a mathematical transformation repeatedly.           | 重複套用數學函式進行運算。  |

---

# 🧩 **ASCII Diagrams **

### **ASCII Workflow: Relationship Between `outer()` and `inner()` **

```
outer(x, function)
    |
    |--- creates variable: current = x
    |
    |--- creates inner() ----------------------+
    |                                          |
    +--> returns inner() ----------------------+
```

```
          ┌─────────────────────────┐
          │        outer()          │
          │  - receives arguments   │
          │  - defines inner()      │
          │  - may return inner()   │
          └───────────┬────────────┘
                      │
                      ▼
          ┌─────────────────────────┐
          │        inner()          │
          │  - uses outer’s data    │
          │  - performs operation   │
          │  - produces result      │
          └─────────────────────────┘
```
```
outer() called
    ├─ prepare data
    ├─ define inner()       ← inner has access to outer’s variables
    ├─ optionally modify behaviour
    └─ return inner()

At runtime/Each call:
    inner() executes
        ├─ uses values captured in outer()
        ├─ performs calculations
        └─ returns result

```

Simple Examle 
```python
def outer(x):
    def inner(y):
        return x + y
    return inner

add10 = outer(10)
print(add10(5))   # 15

```












---

## ex02 

Step-by-step breakdown
| Layer | Function name                   | Purpose                                             | What it returns                                |
| ----- | ------------------------------- | --------------------------------------------------- | ---------------------------------------------- |
| 1️⃣   | `callLimit(limit)`              | outer function — stores the `limit` value           | returns `callLimiter`                          |
| 2️⃣   | `callLimiter(function)`         | inner function — gets the function to decorate      | returns `limit_function`                       |
| 3️⃣   | `limit_function(*args, **kwds)` | wrapper — controls how many times the function runs | returns result of `function()` or prints error |

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


| Concept                                              | Meaning                                                                            | Why the Subject Teaches It                                  |
| ---------------------------------------------------- | ---------------------------------------------------------------------------------- | ----------------------------------------------------------- |
| **Decorator Factory**                                | A function (`callLimit`) that *returns* a decorator.                               | To understand how decorators can be dynamically configured. |
| **Nested Functions (`outer → decorator → wrapper`)** | Three layers controlling behavior: `callLimit` → `callLimiter` → `limit_function`. | Teaches how decorators wrap functions and pass arguments.   |
| **Closure / Capturing State**                        | `count` is stored inside the decorator and persists across calls.                  | Demonstrates how decorators can maintain state.             |
| **Call Limiting Logic**                              | Only allow the wrapped function to run a fixed number of times.                    | Shows manipulation of execution flow.                       |
| **`*args` and `**kwargs`**                           | Allows the decorator to work with **any function signature**.                      | Teaches general-purpose decorator design.                   |
| **`nonlocal` keyword**                               | Allows writing to the `count` variable defined in an enclosing scope.              | Essential to modify state stored in a closure.              |
| **Printing an Error Message**                        | Matches the expected Piscine output.                                               | Reinforces strict output format discipline.                 |
| 概念                           | 說明                                                   | 為何題目要教            |
| ---------------------------- | ---------------------------------------------------- | ----------------- |
| **裝飾器工廠（Decorator Factory）** | `callLimit` 是一個會「回傳裝飾器」的函式。                          | 讓你理解裝飾器可以被動態設定。   |
| **巢狀函式（外層 → 裝飾器 → 包裝器）**     | 三層結構：`callLimit` → `callLimiter` → `limit_function`。 | 教你裝飾器如何包覆函式並傳遞參數。 |
| **閉包 / 狀態保持（Closure）**       | `count` 被保存在 decorator 內，多次呼叫依然存在。                   | 示範裝飾器如何保存狀態。      |
| **呼叫次數限制邏輯**                 | 限制 wrapped function 只能執行固定次數。                        | 讓你學習如何控制函式執行流程。   |
| **`*args` / `**kwargs`**     | 讓裝飾器能套用在任何函式上。                                       | 教你寫出泛用型裝飾器。       |
| **`nonlocal` 關鍵字**           | 允許修改外層函式的變數（例如 `count`）。                             | 是修改閉包內狀態的必要語法。    |
| **錯誤訊息輸出**                   | 必須完全符合題目格式。                                          | 訓練嚴格遵守輸出規範的能力。    |

- High-Level Flow Summary
```python
🟥 Layer 1 — callLimit(limit)
    • Receives: limit
    • Creates: count = 0
    • Returns: callLimiter

🟧 Layer 2 — callLimiter(function)
    • Receives: the function to decorate
    • Returns: limit_function

🟩 Layer 3 — limit_function(*args, **kwargs)
    • Receives: actual runtime arguments
    • Uses: nonlocal count
    • Behavior:
        - If count < limit → run function
        - Else → print "Error: ... call too many times"

```


```
 ┌──────────────────────────────────────────────────────────┐
 │                  Layer 1 — callLimit(limit)              │
 │  • Input : limit                                         │
 │  • Output: callLimiter  (a decorator)                    │
 │  • Stores the closure variable: count = 0                │
 └───────────────┬──────────────────────────────────────────┘
                 │ returns decorator
                 ▼
 ┌──────────────────────────────────────────────────────────┐
 │           Layer 2 — callLimiter(function)                │
 │  • Input : the function being decorated (f, g, ...)      │
 │  • Output: limit_function (a wrapper)                    │
 │  • Captures: limit, count (from Layer 1 closure)         │
 └───────────────┬──────────────────────────────────────────┘
                 │ returns wrapper
                 ▼
 ┌──────────────────────────────────────────────────────────┐
 │     Layer 3 — limit_function(*args, **kwargs)            │
 │  • Input : whatever arguments the wrapped function uses  │
 │  • Logic :                                               │
 │       if count < limit:                                  │
 │            - increase count                              │
 │            - call the real function                      │
 │       else:                                              │
 │            - print error                                 │
 │  • Output: Either the real function result or error msg  │
 │  • Uses: nonlocal count                                  │
 └──────────────────────────────────────────────────────────┘


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

| Concept                              | Explanation (English)                                                                                                 | 解說（繁體中文）                                                         |
| ------------------------------------ | --------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------- |
| **Dataclass**                        | `@dataclass` automatically generates `__init__`, `__repr__`, `__eq__`, and more.                                      | `@dataclass` 自動生成 `__init__`、`__repr__`、`__eq__` 等方法。            |
| **field(init=False)**                | Marks a variable so it is **not settable during initialization**; must be set later.                                  | 標記欄位不能在初始化時設定，需在 `__post_init__` 或其他方法設定。                        |
| **`__post_init__()`**                | Special method that runs **after the autogenerated `__init__`**. Allows computed or derived attributes.               | 自動生成的 `__init__` 後執行，可用於計算或衍生屬性設定。                               |
| **Random ID Generation**             | `generate_id()` creates a 15-character random lowercase string using `random.choices()` and `string.ascii_lowercase`. | 使用 `random.choices()` 與 `string.ascii_lowercase` 產生 15 個字母的隨機字串。 |
| **Immutable / Protected Attributes** | `login` and `id` cannot be initialized by caller; attempting to do so raises `TypeError`.                             | `login` 與 `id` 不能被外部初始化，違規會產生 `TypeError`。                       |
| **Computed login**                   | `login` is derived from first letter of `name` (capitalized) + `surname`.                                             | `login` 由名字首字母大寫 + 姓氏組成，例如 `Edward` + `agle` → `Eagle`。          |

---

## Conclusion : Why important?


Here’s a **professional, concise explanation** of the importance of `outer() / inner()`, decorators, and wrappers, in both **English** and **Traditional Chinese**.

---

# 1. **outer() and inner()**

| Concept    | Importance (English)                                                                                                                                                                                   | 重要性（繁體中文）                                          |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------- |
| `outer()`  | The **outer function** sets up the environment, initial state, or parameters that will be used by `inner()`. It can accept arguments and prepare data for repeated use.                                | 外層函式用來設定環境、初始狀態或參數，供內層函式使用。它可以接收參數並準備重複使用的資料。      |
| `inner()`  | The **inner function** is the closure that captures variables from `outer()`. It performs the actual computation or action while maintaining access to `outer()`’s data even after `outer()` finishes. | 內層函式（閉包）捕捉外層函式的變數。它執行實際計算或操作，並且即使外層函式已結束，仍可使用外層資料。 |
| Importance | Enables **stateful functions**, **dynamic behavior**, and **encapsulation** without using globals.                                                                                                     | 讓函式具有「狀態記憶」、動態行為及封裝能力，而不需要使用全域變數。                  |

Example 
```
outer(x)               ← called by user
 │
 ├─ prepares data / state
 │
 └─ defines inner()    ← inner captures outer’s variables (closure)
       │
       ▼
inner()                ← executed when returned
 │  accesses outer()’s variables
 │  performs computation
 ▼
returns result
---------------------------------------------------------

outer(x)               ← 使用者呼叫
 │
 ├─ 準備資料 / 狀態
 │
 └─ 定義 inner()      ← inner 捕捉 outer 變數（閉包）
       │
       ▼
inner()                ← 執行時呼叫
 │  使用 outer 變數
 │  執行運算
 ▼
回傳結果


```


# 2. **Decorator**

| Concept    | Importance (English)                                                                                                          | 重要性（繁體中文）                                |
| ---------- | ----------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------- |
| Decorator  | A function that **modifies or enhances another function** without changing its code.                                          | 裝飾器是一個函式，可以在不改變原函式程式碼的情況下，修改或增強該函式功能。    |
| Use        | Enables **reusable logic**, **cross-cutting concerns**, and **code separation** (e.g., logging, call limits, authentication). | 可實現「重複使用邏輯」、交叉關注點（如日誌、呼叫次數限制、驗證）以及程式碼分離。 |
| Importance | Central to **Python functional programming** and **clean, DRY code design**.                                                  | 是 Python 函式式程式設計及乾淨、避免重複程式碼設計的核心工具。      |


Example 
```
@decorator           ← decorator syntax
function_to_wrap()
 │
 ├─ decorator(outer)  ← outer sets up state or configuration
 │
 └─ returns wrapper(inner)
       │
       ▼
wrapper()             ← called instead of original function
 │  applies extra logic (pre/post)
 │  optionally calls original function
 ▼
original function executes
-------------------------------------------------------------
@decorator           ← 裝飾器語法
function_to_wrap()
 │
 ├─ decorator(outer)  ← outer 設定狀態或配置
 │
 └─ 回傳 wrapper(inner)
       │
       ▼
wrapper()             ← 呼叫 wrapper 取代原函式
 │  增加前置/後置邏輯
 │  可選擇呼叫原函式
 ▼
原函式執行

```

# 3. **Wrapper**

| Concept    | Importance (English)                                                                                                                        | 重要性（繁體中文）                                           |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------- |
| Wrapper    | The **inner function returned by a decorator** that wraps the original function. Controls behavior before/after the original function runs. | 包裝器是裝飾器回傳的內層函式，用來包覆原函式。可在原函式執行前或後控制行為。              |
| Use        | - Modify arguments<br>- Add pre/post logic<br>- Enforce rules (e.g., call limits)<br>- Maintain state                                       | - 修改參數<br>- 增加前置/後置邏輯<br>- 執行規則檢查（例如呼叫限制）<br>- 保存狀態 |
| Importance | Allows **dynamic enhancement** of functions **without altering their core logic**.                                                          | 允許在不改變函式核心邏輯下，動態增強函式功能。                             |

Example 
```
wrapper(*args, **kwargs)   ← replaces original function
 │
 ├─ access closure variables (from outer / decorator)
 │
 ├─ pre-processing logic
 │
 ├─ call original function
 │
 └─ post-processing logic / return result
-----------------------------------------------------------
wrapper(*args, **kwargs)   ← 取代原函式
 │
 ├─ 使用閉包變數（來自 outer / 裝飾器）
 │
 ├─ 前置處理邏輯
 │
 ├─ 呼叫原函式
 │
 └─ 後置處理 / 回傳結果

```

### Combined Flow: outer → inner → decorator → wrapper → original function
```
User calls decorated function
       │
       ▼
outer()                ← Layer 1 / decorator factory
 │  sets up state, arguments
 └─ returns inner() / wrapper

inner() / wrapper()     ← Layer 2 / Layer 3
 │  captures outer() variables (closure)
 │  performs extra logic (pre/post)
 │  calls original function if needed
 ▼
Original function executes
 │  returns result
 ▼
wrapper returns result to user
----------------------------------------------------
使用者呼叫已裝飾函式
       │
       ▼
outer()                ← 第1層 / 裝飾器工廠
 │  設定狀態與參數
 └─ 回傳 inner() / wrapper

inner() / wrapper()     ← 第2層 / 第3層
 │  捕捉 outer() 變數（閉包）
 │  執行前置/後置邏輯
 │  視需要呼叫原函式
 ▼
原函式執行
 │  回傳結果
 ▼
wrapper 回傳結果給使用者

```



---

# 🔑 Summary Concept

* **outer() → inner()**: enables closures, captures state, avoids globals
* **decorator**: reusable enhancement mechanism for functions
* **wrapper**: executes extra logic around the original function while preserving signature


