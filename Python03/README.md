# OOP (Object Oriented Programming)
[Back to Index](../README.md)

## 🧠 Python vs C++ — Object-Oriented Programming Comparison

| **Concept / Feature**      | **Python**                                       | **C++**                                           | **Explanation (English + 中文說明)**                                                                                                                                    |
| -------------------------- | ------------------------------------------------ | ------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Language Type**          | Dynamically typed, interpreted                   | Statically typed, compiled                        | **English:** Python is interpreted and dynamically typed. C++ is compiled and statically typed. <br> **中文:** Python 是直譯語言、動態型別；C++ 是編譯語言、靜態型別。                      |
| **Class Definition**       | `class MyClass:`                                 | `class MyClass { ... };`                          | **English:** Python defines classes using indentation. C++ uses curly braces `{}` and ends with a semicolon. <br> **中文:** Python 使用縮排定義類別；C++ 使用 `{}` 並以分號結尾。       |
| **Object Creation**        | `obj = MyClass()`                                | `MyClass obj;` or `MyClass *obj = new MyClass();` | **English:** Python allocates memory automatically. C++ can create on stack or heap manually. <br> **中文:** Python 自動配置記憶體；C++ 需手動或使用 `new/delete`。                  |
| **Constructor**            | `def __init__(self):`                            | `MyClass() { ... }`                               | **English:** Python uses `__init__`. C++ uses a constructor with the same name as the class. <br> **中文:** Python 使用 `__init__()`；C++ 使用類別名相同的建構子。                   |
| **Destructor**             | `def __del__(self):`                             | `~MyClass() { ... }`                              | **English:** Python has automatic garbage collection. C++ requires manual cleanup. <br> **中文:** Python 自動垃圾回收；C++ 需手動釋放記憶體。                                         |
| **Inheritance**            | `class Child(Parent):`                           | `class Child : public Parent { ... };`            | **English:** Python uses parentheses; C++ uses colon with access type. <br> **中文:** Python 使用括號；C++ 使用冒號指定繼承類型 (`public`, `private`)。                               |
| **Multiple Inheritance**   | Allowed, resolved by MRO                         | Allowed, may cause diamond problem                | **English:** Python solves conflicts using *Method Resolution Order (MRO)*; C++ may suffer diamond issues. <br> **中文:** Python 透過「方法解析順序 (MRO)」解決衝突；C++ 可能出現菱形繼承問題。 |
| **Encapsulation**          | `_protected`, `__private` (by naming convention) | `private:`, `protected:`, `public:`               | **English:** Python only suggests privacy by naming; C++ enforces it syntactically. <br> **中文:** Python 靠命名規則暗示封裝；C++ 有明確的語法控制權限。                                   |
| **Polymorphism**           | Dynamic typing allows easy method override       | Function overloading + virtual functions          | **English:** Python uses dynamic typing for polymorphism. C++ uses static overloading and virtual dispatch. <br> **中文:** Python 的多型靠動態型別；C++ 使用多載與虛擬函式。             |
| **Abstract Classes**       | `from abc import ABC, abstractmethod`            | `virtual void func() = 0;`                        | **English:** Python uses the `abc` module. C++ uses pure virtual functions. <br> **中文:** Python 使用 `abc` 模組；C++ 用純虛擬函式定義抽象類別。                                       |
| **Static / Class Methods** | `@staticmethod`, `@classmethod`                  | `static void func();`                             | **English:** Python uses decorators; C++ uses the `static` keyword. <br> **中文:** Python 用裝飾器；C++ 用 `static` 關鍵字。                                                    |
| **Access to Instance**     | `self` keyword                                   | `this` pointer                                    | **English:** Python passes `self` explicitly. C++ has implicit `this` pointer. <br> **中文:** Python 明確傳入 `self`；C++ 的 `this` 是隱含指標。                                  |
| **Memory Management**      | Automatic (Garbage Collector)                    | Manual (`new`, `delete`)                          | **English:** Python uses automatic memory cleanup. C++ requires manual allocation/deallocation. <br> **中文:** Python 自動管理記憶體；C++ 需手動配置與釋放。                           |
| **Operator Overloading**   | `__add__`, `__eq__`, etc.                        | `operator+`, `operator==`, etc.                   | **English:** Both support operator overloading; Python uses special methods. <br> **中文:** 兩者皆支援運算子多載，但語法不同。                                                         |
| **Type Safety**            | Dynamic (runtime check)                          | Static (compile-time check)                       | **English:** Python checks type at runtime; C++ checks before compilation. <br> **中文:** Python 在執行期檢查型別；C++ 在編譯期檢查。                                                 |
| **Templates / Generics**   | Duck typing (no templates)                       | `template<typename T>`                            | **English:** Python uses duck typing instead of templates. <br> **中文:** Python 使用「鴨子型別」而非模板泛型。                                                                      |
| **Performance**            | Slower (interpreted)                             | Faster (compiled)                                 | **English:** Python trades speed for simplicity. <br> **中文:** Python 執行較慢但簡潔；C++ 效能高但複雜。                                                                            |
| **Code Simplicity**        | Fewer lines, very readable                       | Verbose but powerful                              | **English:** Python code is shorter and clearer. <br> **中文:** Python 程式簡潔易懂；C++ 冗長但功能強大。                                                                            |

---

## 🧩 **Summary Insight**

| **Category**       | **Python**                             | **C++**                                 | **Explanation (English + 中文說明)**                                                                                                         |
| ------------------ | -------------------------------------- | --------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| **Philosophy**     | Easy, readable, developer-friendly     | Powerful, performant, low-level control | **English:** Python values simplicity and readability; C++ values precision and performance. <br> **中文:** Python 強調簡潔與可讀性；C++ 強調效能與底層控制。 |
| **OOP Model**      | Fully dynamic, everything is an object | Hybrid procedural + OOP                 | **English:** Python is fully object-oriented; C++ can mix procedural and OOP. <br> **中文:** Python 一切皆物件；C++ 可混合程序與物件導向風格。                |
| **Error Handling** | `try/except`                           | `try/catch`                             | **English:** Both support exception handling, but syntax differs slightly. <br> **中文:** 兩者都支援例外處理，語法略有不同。                                |
| **Compile vs Run** | Runs immediately (interpreted)         | Needs compilation (machine code)        | **English:** Python executes code line by line; C++ compiles first. <br> **中文:** Python 即時執行；C++ 需先編譯成機器碼。                               |

---

## 🧩 **Memory Model Diagram — Python vs C++**

Here’s a side-by-side ASCII diagram showing how **object storage and references** differ:

```
        🐍 Python (Reference-based)
        ----------------------------
        Stack (variable name)
        ┌──────────────┐
        │ obj ---------|------------------┐
        └──────────────┘                  │
                                           ▼
                                   Heap (Object in Memory)
                                   ┌──────────────────────┐
                                   │ MyClass instance     │
                                   │ id=0x1234ABCD        │
                                   │ attributes, methods  │
                                   └──────────────────────┘
        # Python stores a *reference* (pointer) to the object.
        # The garbage collector frees it when no references remain.


        ⚙️ C++ (Stack vs Heap allocation)
        ---------------------------------
        Stack:
        ┌──────────────────────┐
        │ MyClass obj;         │  → Object data stored directly here
        └──────────────────────┘

        OR (Heap allocation):
        ┌──────────────┐
        │ MyClass *ptr │────────────┐
        └──────────────┘            ▼
                                 Heap:
                                 ┌──────────────────────┐
                                 │ new MyClass()        │
                                 │ (explicit delete req)│
                                 └──────────────────────┘
        # C++ distinguishes between stack (auto memory)
        # and heap (manual memory). Developer must manage it.
```

---

### 🧠 Summary of the Memory Difference

| **Aspect**      | **Python**                    | **C++**                                     |
| --------------- | ----------------------------- | ------------------------------------------- |
| Variable stores | Reference to object           | Either the object (stack) or pointer (heap) |
| Memory cleanup  | Automatic (Garbage Collector) | Manual (`delete`) or automatic (stack)      |
| Ownership       | Shared by references          | Explicit control                            |
| Lifetime        | Until all references are gone | Until scope ends or `delete` is called      |

---

## ex00

```sql
      ┌────────────┐
      │ Character  │  <-- Abstract Base Class (ABC)
      │------------│
      │ first_name │
      │ is_alive   │
      │ die()      │  <-- Abstract method
      └─────┬──────┘
            │
      ┌─────▼──────┐
      │   Stark    │  <-- Concrete Class
      │------------│
      │ die()      │  <-- Implements Character.die()
      └────────────┘

```
- Character: Cannot be instantiated; defines die() as abstract.
- Stark: Inherits Character and implements die().

## ex01

```sql
      ┌────────────┐
      │ Character  │
      │------------│
      │ first_name │
      │ is_alive   │
      │ die()      │
      └─────┬──────┘
            │
   ┌────────▼────────┐
   │   Stark         │
   │----------------│
   │ __str__/__repr__│
   │ classmethods    │
   └─────────────────┘

```
- Adds `__str__`, `__repr__`, and classmethods to create chained family members.

## ex02

```sql
      ┌───────────────┐
      │    ClapTrap    │
      └─────┬─────────┘
            │
      ┌─────▼─────────┐
      │   ScavTrap     │
      └─────┬─────────┘
            │
      ┌─────▼─────────┐
      │ FragTrap      │
      └─────┬─────────┘
            │
      ┌─────▼─────────┐
      │ DiamondTrap   │
      │---------------│
      │ multiple inh. │
      │ @property     │
      │ setter/getter │
      └───────────────┘

```
- DiamondTrap inherits from both ScavTrap and FragTrap, which themselves inherit from ClapTrap.
- This forms the diamond problem, handled in Python by MRO (Method Resolution Order).
- Uses properties to safely manage attributes like name, hit_points, etc.

✅ Key Takeaways from the Diagrams
1. ABC + Abstract Methods → Forces subclasses to implement key functionality (Exercise 00).
2. Single Inheritance → Simple parent-child relationships (Exercise 01).
3. Multiple Inheritance + Diamond Problem → Python resolves conflicts using MRO (Exercise 02).
4. @property and @setter → Manage access to sensitive attributes safely.

---

# RANDOM NOTES TO SORT

## ex00-ex01 syntax 

questions:

- what's self?
- what's super?
- what's difference: @classmethod @abstractmethod
- syntax meaning and usage example :
__main__
__file__
__init__
__repr__
__str__
__dict__

- what's create "chain creation"?:
    @classmethod
    def create(cls, first_name, is_alive=True):
        """Class method to create a new Baratheon instance."""
        return cls(first_name, is_alive)  # cls represents the class itself (Baratheon)
        # This allows chained creation, like: Baratheon.create("Robert").create(...)

- @property @[property].setter : like c++ getter() and setter()? 



class Character(ABC):
    def __init__(self, first_name: str, is_alive: bool = True):
    self.first_name = first_name      # Store the provided 
    self.is_alive = is_alive          # Store the provided is_alive 


    @abstractmethod

class Stark(Character):
    def __init__(self, first_name: str, is_alive: bool = True):



class Baratheon(Character):
    @classmethod



class Lannister(Character):
    super().__init__(first_name, is_alive)



## NOTES

### ex01

```
| Concept              | Explanation                                | Example                                  |
| -------------------- | ------------------------------------------ | ---------------------------------------- |
| `super().__init__()` | Calls the parent (`Character`) constructor | `super().__init__(first_name, is_alive)` |
| `__str__`            | Human-readable display (`print(obj)`)      | `"Robert Baratheon"`                     |
| `__repr__`           | Developer-readable display (`obj`)         | `"<Character: Robert Baratheon>"`        |
| `@classmethod`       | Alternative constructor that uses `cls`    | `Baratheon.create("Robert")`             |
| `Decorator function` | Function that returns a new object         | `create_lannister("Cersei")`             |

```

### 02 multiple inheritance

```
| Concept                           | Description                                     | Why it matters                                    |
| --------------------------------- | ----------------------------------------------- | ------------------------------------------------- |
| **Multiple Inheritance**          | Inherit from multiple parents.                  | Simulates “mixed lineage” of Joffrey.             |
| **MRO (Method Resolution Order)** | Defines which parent’s methods run first.       | Baratheon before Lannister.                       |
| **@property**                     | Defines controlled access to private variables. | Prevents direct modification, ensures validation. |
| **Encapsulation**                 | Hide attributes behind getters/setters.         | Keeps code cleaner and safer.                     |
| **super()**                       | Calls next class in MRO.                        | Avoids calling base constructors manually.        |

```

#### Class Hierarchy Overview
```
          ┌──────────────────────────┐
          │      Character (ABC)     │
          │ ───────────────────────  │
          │ + first_name             │
          │ + is_alive               │
          │ + die()   (abstract)     │
          └──────────────┬───────────┘
                         │
      ┌──────────────────┴──────────────────┐
      │                                     │
┌───────────────┐                   ┌───────────────┐
│  Baratheon    │                   │   Lannister   │
│───────────────│                   │───────────────│
│ + family_name │                   │ + family_name │
│ + eyes        │                   │ + eyes        │
│ + hairs       │                   │ + hairs       │
│ + die()       │                   │ + die()       │
│ + __str__()   │                   │ + __str__()   │
│ + __repr__()  │                   │ + __repr__()  │
└───────────────┘                   └───────────────┘
      │                                     │
      └──────────────────┬──────────────────┘
                         │
              ┌────────────────────┐
              │     King (Joffrey) │
              │────────────────────│
              │ + eyes (property)  │
              │ + hairs (property) │
              │ + get/set methods  │
              └────────────────────┘

```

#### Memory Reference Flow
```
+----------------------------------------------+
| Variable: Joffrey                            |
|  (reference on stack)                        |
+----------------------------------------------+
                   │
                   ▼
+-----------------------------------------------------+
| King instance (in heap memory)                      |
|-----------------------------------------------------|
| first_name : 'Joffrey'                              |
| is_alive   : True                                   |
| family_name: 'Baratheon'  ← from Baratheon          |
| _eyes      : 'brown' → later changed to 'blue'      |
| _hairs     : 'dark'  → later changed to 'light'     |
|-----------------------------------------------------|
| MRO chain  : King → Baratheon → Lannister → Character|
+-----------------------------------------------------+

```

#### Execution Flow (when running tester.py)

```
Joffrey = King("Joffrey")
   │
   ▼
King.__init__()
   │
   └── super() → Baratheon.__init__()
         │
         └── Character.__init__()

# Initial dict (from Baratheon defaults)
{'first_name': 'Joffrey', 'is_alive': True, 'family_name': 'Baratheon', '_eyes': 'brown', '_hairs': 'dark'}

Joffrey.set_eyes("blue")
 → property setter → self._eyes = "blue"

Joffrey.set_hairs("light")
 → property setter → self._hairs = "light"

```

⚙️ Method Resolution Order (MRO)
When Python needs to resolve a method (like __init__ or die()),
it searches classes in this order:
```King → Baratheon → Lannister → Character → object```
👉 You can check this directly in code:
```print(King.__mro__)```

Output:
```
(<class 'DiamondTrap.King'>,
 <class 'S1E7.Baratheon'>,
 <class 'S1E7.Lannister'>,
 <class 'S1E9.Character'>,
 <class 'object'>)
```

So when you call:
```
super().__init__(first_name)
```
It calls Baratheon’s `__init__` first — not Lannister’s — because that’s the first in the MRO chain.


```
| Concept                        | Symbol in Diagram     | Meaning                            |
| ------------------------------ | --------------------- | ---------------------------------- |
| `super()`                      | Arrow →               | Calls next class in MRO            |
| `_eyes`, `_hairs`              | Underscore `_`        | Private attributes (encapsulation) |
| `King → Baratheon → Lannister` | MRO chain             | Defines method lookup order        |
| `__init__()`                   | Constructor           | Initializes object attributes      |
| `@property`                    | Getter/Setter control | Protects and validates data        |

```
---
# step-by-step ASCII memory mutation animation
**step-by-step ASCII memory mutation animation** showing how the `Joffrey` object changes in memory when we modify his properties:

## ⚙️ Step 1 — Object Creation

```python
Joffrey = King("Joffrey")
```

**In Memory:**

```
[STACK]                            [HEAP]
───────────────                    ───────────────────────────────────────────────
Joffrey ─────────────┐              King instance
                     │              ┌───────────────────────────────────────────┐
                     └─────────────►│ first_name : "Joffrey"                    │
                                    │ is_alive   : True                         │
                                    │ family_name: "Baratheon"                  │
                                    │ _eyes      : "brown"     ← default value  │
                                    │ _hairs     : "dark"      ← default value  │
                                    └───────────────────────────────────────────┘
```

📘 *Joffrey is alive, brown-eyed, dark-haired — defaults inherited from Baratheon.*

---

## 🔁 Step 2 — Change Eye Color

```python
Joffrey.set_eyes("blue")
```

**Execution:**

* `set_eyes()` → setter function → modifies `_eyes` attribute.

**In Memory:**

```
[STACK]                            [HEAP]
───────────────                    ───────────────────────────────────────────────
Joffrey ─────────────┐              King instance
                     │              ┌───────────────────────────────────────────┐
                     └─────────────►│ first_name : "Joffrey"                    │
                                    │ is_alive   : True                         │
                                    │ family_name: "Baratheon"                  │
                                    │ _eyes      : "blue"      ← changed ✅     │
                                    │ _hairs     : "dark"                       │
                                    └───────────────────────────────────────────┘
```

📘 *Property successfully updated through setter (encapsulation in action).*

---

## 🔁 Step 3 — Change Hair Color

```python
Joffrey.set_hairs("light")
```

**Execution:**

* `set_hairs()` → setter function → modifies `_hairs` attribute.

**In Memory:**

```
[STACK]                            [HEAP]
───────────────                    ───────────────────────────────────────────────
Joffrey ─────────────┐              King instance
                     │              ┌───────────────────────────────────────────┐
                     └─────────────►│ first_name : "Joffrey"                    │
                                    │ is_alive   : True                         │
                                    │ family_name: "Baratheon"                  │
                                    │ _eyes      : "blue"                       │
                                    │ _hairs     : "light"     ← changed ✅     │
                                    └───────────────────────────────────────────┘
```

📘 *Both attributes updated — Joffrey’s state has mutated in heap memory.*

---

## 🧠 Step 4 — Print `__dict__`

```python
print(Joffrey.__dict__)
```

**Output:**

```python
{'first_name': 'Joffrey',
 'is_alive': True,
 'family_name': 'Baratheon',
 '_eyes': 'blue',
 '_hairs': 'light'}
```

📘 *Shows the final internal state of Joffrey’s instance dictionary.*

---

## 🔍 Recap Summary

| Step | Code                        | Attribute Changed | Description                     |
| ---- | --------------------------- | ----------------- | ------------------------------- |
| 1    | `Joffrey = King("Joffrey")` | —                 | Object created, defaults loaded |
| 2    | `set_eyes("blue")`          | `_eyes`           | Setter updates eye color        |
| 3    | `set_hairs("light")`        | `_hairs`          | Setter updates hair color       |
| 4    | `print(__dict__)`           | —                 | Shows final internal state      |

---

# detailed ASCII + conceptual diagram 
 **detailed ASCII + conceptual diagram** showing how `@property` and `@setter` actually work internally in Python classes.

This is *exactly* what happens in your `King` class for attributes like `eyes` and `hairs`.


## 🧩 1. Property Flow Overview

```
class King(Baratheon, Lannister):
    def __init__(self, first_name):
        super().__init__(first_name)
        self._eyes = "brown"
        self._hairs = "dark"

    @property
    def eyes(self):
        """Getter"""
        return self._eyes

    @eyes.setter
    def eyes(self, color):
        """Setter"""
        self._eyes = color
```

---

## ⚙️ 2. What Happens Behind the Scenes

### Without property:

If you just had:

```python
Joffrey._eyes = "blue"
```

You’d be directly modifying a variable — no checks, no validation, and *no encapsulation*.

---

### With `@property`:

The `@property` decorator **wraps your getter and setter** into a **property object**.

📦 **Internally, Python transforms it like this:**

```
eyes = property(get_eyes, set_eyes)
```

So, the attribute name `eyes` now refers to a *property descriptor object* that controls access to the internal `_eyes` variable.

---

## 🧠 3. Memory + Function Flow

```
┌──────────────────────────────────────────────┐
│ Joffrey = King("Joffrey")                   │
└──────────────────────────────────────────────┘
                      │
                      ▼
        ┌──────────────────────────────────────────────┐
        │ King instance in memory (heap)               │
        │──────────────────────────────────────────────│
        │ _eyes  = "brown"                             │
        │ _hairs = "dark"                              │
        │                                              │
        │ eyes   → property object (get/set functions) │
        └──────────────────────────────────────────────┘
```

Now when you run:

```python
print(Joffrey.eyes)
```

👉 **This happens internally:**

```
1️⃣ Joffrey.eyes → triggers property getter
2️⃣ property calls King.eyes.fget(self)
3️⃣ returns self._eyes ("brown")
```

---

When you do:

```python
Joffrey.eyes = "blue"
```

👉 **This happens internally:**

```
1️⃣ Python sees assignment to a property
2️⃣ property calls King.eyes.fset(self, "blue")
3️⃣ Setter function runs: self._eyes = "blue"
```

So the property intercepts the operation — giving you full control.

---

## 🔁 4. Visual Flow Diagram

```
              ┌────────────────────┐
 read value → │ Joffrey.eyes       │
              └────────┬───────────┘
                       │
                       ▼
           ┌────────────────────────┐
           │  @property getter       │
           │  def eyes(self):        │
           │      return self._eyes  │
           └────────────────────────┘

 assign value ────────────────┐
 Joffrey.eyes = "blue"        │
                              ▼
           ┌────────────────────────┐
           │  @eyes.setter           │
           │  def eyes(self, color): │
           │      self._eyes = color │
           └────────────────────────┘
```

---

## 🧱 5. Why Use It?

| Feature       | Without Property         | With @property                                     |
| ------------- | ------------------------ | -------------------------------------------------- |
| Encapsulation | ❌ direct variable access | ✅ controlled access                                |
| Validation    | ❌ cannot intercept       | ✅ you can validate input                           |
| Readability   | ✅ simple                 | ✅ same syntax, safer                               |
| Reusability   | ❌ limited                | ✅ you can change logic later without breaking code |

---

## 💬 6. Quick Example with Validation

```python
class King(Baratheon, Lannister):
    @property
    def eyes(self):
        return self._eyes

    @eyes.setter
    def eyes(self, color):
        if color not in ["blue", "green", "brown"]:
            raise ValueError("Invalid eye color")
        self._eyes = color
```

Now:

```python
Joffrey.eyes = "red"
```

💥 Raises `ValueError: Invalid eye color`

---

## ex03

```
| Term     | Meaning                                                 | You should use                    |
| -------- | ------------------------------------------------------- | --------------------------------- |
| `object` | Generic placeholder for the operand                     | ✔️ Rename to `scalar` for clarity |
| `vector` | Your stored list of numbers (`self.vector`)             | Stays inside the class            |
| `scalar` | A single number (int or float) to apply on each element | Passed when doing `v + 5`, etc.   |

```

Excellent 💪 — this **Exercise 03: Calculate My Vector** builds on your Python OOP foundation and introduces a key concept:
👉 **Operator overloading with dunder methods** (`__add__`, `__mul__`, `__sub__`, `__truediv__`).

Let’s break it all down step by step — with code, diagram, and reasoning.

---

## 🧠 1. Concept Overview: Vector × Scalar

You’re asked to create a **`calculator` class** that represents a **vector** (a list of numbers)
and can perform math operations **with a scalar** (single number).

📘 *Each operation should modify and print the new vector.*

---

## ⚙️ 2. Expected Behavior from `tester.py`

```python
from ft_calculator import calculator

v1 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
v1 + 5      # → add 5 to each element → prints new vector
print("---")

v2 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
v2 * 5      # → multiply each element by 5 → prints new vector
print("---")

v3 = calculator([10.0, 15.0, 20.0])
v3 - 5      # → subtract 5 from each element
v3 / 5      # → divide each element by 5
```

🧩 **Expected Output**

```
[5.0, 6.0, 7.0, 8.0, 9.0, 10.0]
---
[0.0, 5.0, 10.0, 15.0, 20.0, 25.0]
---
[5.0, 10.0, 15.0]
[1.0, 2.0, 3.0]
```

---

## 🧩 3. Full Implementation — `ft_calculator.py`

```python
class calculator:
    """A calculator class that performs scalar operations on a vector."""

    def __init__(self, vector):
        """Initialize with a list (vector) of floats."""
        self.vector = vector

    def __add__(self, scalar):
        """Add scalar to each element and print result."""
        result = [x + scalar for x in self.vector]
        print(result)
        return result

    def __mul__(self, scalar):
        """Multiply each element by scalar and print result."""
        result = [x * scalar for x in self.vector]
        print(result)
        return result

    def __sub__(self, scalar):
        """Subtract scalar from each element and print result."""
        result = [x - scalar for x in self.vector]
        print(result)
        return result

    def __truediv__(self, scalar):
        """Divide each element by scalar and print result (handle div by 0)."""
        if scalar == 0:
            print("Error: Division by zero")
            return None
        result = [x / scalar for x in self.vector]
        print(result)
        return result
```

---

## 🔍 4. Line-by-Line Explanation

| Line  | Code                                         | Explanation                                                       |
| ----- | -------------------------------------------- | ----------------------------------------------------------------- |
| 1     | `class calculator:`                          | Defines your class — represents a numeric vector.                 |
| 2     | `"""A calculator class..."""`                | Docstring (required by Piscine norms).                            |
| 4     | `def __init__(self, vector):`                | Constructor — takes a list of floats.                             |
| 5     | `self.vector = vector`                       | Stores the list in the instance.                                  |
| 7     | `def __add__(self, scalar):`                 | Dunder method → called when you do `v + n`.                       |
| 8     | `result = [x + scalar for x in self.vector]` | Adds scalar to each vector element using list comprehension.      |
| 9     | `print(result)`                              | Outputs the resulting list immediately.                           |
| 10    | `return result`                              | Returns the new list (optional).                                  |
| 12–24 | `__mul__`, `__sub__`, `__truediv__`          | Same logic for other arithmetic operations.                       |
| 21    | `if scalar == 0:`                            | Protects against division by zero (only required error handling). |

---

### ⚙️ Operator Overloading Diagram

```
     ┌─────────────────────────────┐
     │       calculator class      │
     ├─────────────────────────────┤
     │ + vector = [floats]         │
     │ + __add__(scalar)           │
     │ + __mul__(scalar)           │
     │ + __sub__(scalar)           │
     │ + __truediv__(scalar)       │
     └───────────────┬─────────────┘
                     │
                     ▼
              [operator overload]
      ┌─────────────────────────────────────────┐
      │  v1 + 5  → calls v1.__add__(5)          │
      │  v1 - 2  → calls v1.__sub__(2)          │
      │  v1 * 3  → calls v1.__mul__(3)          │
      │  v1 / 2  → calls v1.__truediv__(2)      │
      └─────────────────────────────────────────┘
```

---

### 💡 Output Flow Visualization

```
v1 = calculator([0, 1, 2, 3, 4, 5])
        │
        ▼
+----------------------------+
| vector = [0, 1, 2, 3, 4, 5]|
+----------------------------+

v1 + 5  → [5, 6, 7, 8, 9, 10]
v1 * 5  → [0, 5, 10, 15, 20, 25]
v3 - 5  → [5, 10, 15]
v3 / 5  → [1, 2, 3]
```

```
v1 = calculator([0, 1, 2])
v1 + 5
       │
       ▼
Python internally calls:
v1.__add__(5)
        │
        ├── self.vector = [0, 1, 2]
        └── scalar (a.k.a. "object") = 5

```

---

### 🧮 Key Takeaways

Summary
```
| Term     | Meaning                                                 | You should use                    |
| -------- | ------------------------------------------------------- | --------------------------------- |
| `object` | Generic placeholder for the operand                     | ✔️ Rename to `scalar` for clarity |
| `vector` | Your stored list of numbers (`self.vector`)             | Stays inside the class            |
| `scalar` | A single number (int or float) to apply on each element | Passed when doing `v + 5`, etc.   |

```


```
| Concept                | Description                                       | Example                             |
| ---------------------- | ------------------------------------------------- | ----------------------------------- |
| **Dunder methods**     | Special Python methods that override operators    | `__add__` → `+`, `__sub__` → `-`    |
| **List comprehension** | Short syntax to process lists                     | `[x + scalar for x in self.vector]` |
| **Encapsulation**      | Vector stored as `self.vector`, internal to class | Keeps operations organized          |
| **Division check**     | Only error handling required                      | Avoids ZeroDivisionError            |
| **No global code**     | Everything inside class or tester                 | Required by norm                    |
```
---

## ex04

ASCII Diagram — Execution Flow
```
              ┌──────────────────────────────┐
              │         calculator           │
              ├──────────────────────────────┤
              │  @staticmethod               │
              │  def dotproduct(V1, V2)      │
              │  def add_vec(V1, V2)         │
              │  def sous_vec(V1, V2)        │
              └─────────────┬────────────────┘
                            │
                            ▼
     ┌───────────────────────────────────────────────┐
     │  calculator.dotproduct([5,10,2], [2,4,3])     │
     ├───────────────────────────────────────────────┤
     │  Step 1: zip(V1, V2) → [(5,2), (10,4), (2,3)] │
     │  Step 2: multiply → [10, 40, 6]               │
     │  Step 3: sum → 56                             │
     └───────────────────────────────────────────────┘

```
💡 Why it’s good OOP practice
- You group related math operations inside a class (calculator)
- You use static methods because these don’t need internal state (self)
- You keep your code modular and reusable for later exercises

✅ Summary Table
| Concept              | Keyword / Syntax               | Purpose                    |
| -------------------- | ------------------------------ | -------------------------- |
| `@staticmethod`      | Decorator                      | Call method without `self` |
| `zip()`              | Built-in function              | Combine pairs of elements  |
| `sum()`              | Built-in function              | Sum all numbers            |
| `list comprehension` | `[x + y for x, y in zip(...)]` | Vector operations          |
| `print(f"...")`      | f-string formatting            | Clean output               |






