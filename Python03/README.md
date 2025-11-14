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

Here is a clear and structured explanation to help you understand the code *and* the important Python notions the exercise aims to teach.

### **What important Python notions this exercise teaches**

This exercise is introducing several **core Object-Oriented Programming concepts** in Python:

#### **✓ 1. Abstract Base Classes (ABC)**

* Using `from abc import ABC, abstractmethod`.
* You learn that abstract classes:

  * Cannot be instantiated.
  * Exist to define required behavior for subclasses.

#### **✓ 2. The `@abstractmethod` decorator**

* Forces every subclass to implement the method.
* Creates a proper interface-style constraint.

#### **✓ 3. Class Inheritance**

* `Stark` *inherits* from `Character`.
* It gains attributes and structure from the parent class.
* It customizes behavior by implementing its own `die()`.

#### **✓ 4. Constructors (`__init__`)**

* How to define instance attributes.
* How to call a parent constructor with `super()`.

#### **✓ 5. Instance attributes and `__dict__`**

* Objects store their attributes in a dictionary accessible via `__dict__`.
* Printing `Ned.__dict__` shows all attributes dynamically attached to the instance.

#### **✓ 6. Docstrings**

* The exercise checks:

  * Class docstring
  * Constructor docstring
  * Method docstring
* This teaches **documentation style and best practice**.

#### **✓ 7. Encapsulation of object state**

* `is_alive` is the character’s state.
* Only the `die()` method should change it.

---


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

Here is a clear and structured explanation of your code, and a summary of the important Python notions this exercise teaches.

---

# **1. What Your Code Does**

You create two families — **Baratheon** and **Lannister** — both inheriting from the abstract base class **Character**.

Each class:

* Calls the parent constructor with `super()`
* Defines character-specific physical traits
  (`family_name`, `eyes`, `hairs`)
* Implements the required `die()` method (from the abstract class)
* Implements `__str__` (human-readable)
* Implements `__repr__` (developer/debug view)
* Implements a `@classmethod create(...)`
  (to allow chain-style creation)

You also write a **helper function**:

```python
def create_lannister(first_name, is_alive=True):
    return Lannister(first_name, is_alive)
```

This allows creating a Lannister without calling the class directly, depending on the exercise requirements.

---

# **2. Explanation of the Code**

## **Baratheon Class**

### **Constructor**

```python
def __init__(self, first_name: str, is_alive: bool = True):
    super().__init__(first_name, is_alive)
    self.family_name = "Baratheon"
    self.eyes = "brown"
    self.hairs = "dark"
```

* Calls the `Character` constructor to set `first_name` and `is_alive`
* Adds Baratheon-specific features

### **`__str__`**

```python
def __str__(self):
    return f"{self.first_name} {self.family_name}"
```

* Used in `print(object)`
* Must return a readable string

### **`__repr__`**

```python
def __repr__(self):
    return f"<Character: {self.first_name} {self.family_name}>"
```

* Used in debugging / console inspections
* Must return a clear developer-style representation

### **`die`**

```python
def die(self):
    self.is_alive = False
```

### **Class Method**

```python
@classmethod
def create(cls, first_name, is_alive=True):
    return cls(first_name, is_alive)
```

* A method that belongs to the *class*, not the instance
* Allows instantiation like:

  ```python
  Baratheon.create("Robert")
  ```

---

## **Lannister Class**

Implemented the same way, with different traits:

```python
self.family_name = "Lannister"
self.eyes = "blue"
self.hairs = "light"
```

Everything else mirrors Baratheon.

---

## **Helper Function**

```python
def create_lannister(first_name, is_alive=True):
    return Lannister(first_name, is_alive)
```

This is a *function decorator alternative* for quickly creating Lannister characters depending on exercise requirements.

---

### **3. What the Exercise Is Teaching You (Key Takeaway Notions)**


#### **✓ 1. Inheritance**

Two classes inherit from `Character` and extend it with their own attributes.

You learn how to:

* Reuse parent logic
* Add family-specific behavior
* Implement required abstract methods


#### **✓ 2. Using `super()`**

You call the parent constructor properly:

```python
super().__init__(first_name, is_alive)
```

This reinforces how inheritance chains operate.

---

#### **✓ 3. Magic Methods (`__str__` and `__repr__`)**

You learn the difference:

| Method     | Purpose                        | Example Usage                  |
| ---------- | ------------------------------ | ------------------------------ |
| `__str__`  | Human-readable output          | `print(obj)`                   |
| `__repr__` | Developer/debug representation | `repr(obj)` or in Python shell |

The exercise specifically asks that these return **strings**, not objects.


#### **✓ 4. Class Methods (`@classmethod`)**

You create factory-style constructors:

```python
Jaine = Lannister.create("Jaine")
```

This teaches “chainable” or “alternative constructors”.


#### **✓ 5. Namespace and Attributes (`__dict__`)**

By printing `.__dict__`, you see the **internal attribute storage** of your objects:

```python
{
 'first_name': 'Robert',
 'is_alive': True,
 'family_name': 'Baratheon',
 'eyes': 'brown',
 'hairs': 'dark'
}
```

This shows how Python stores instance data.


### **✓ 6. Abstaction (Carried over from previous exercise)**

Even though you don’t use `Character` directly, you respect its contract:
every subclass must implement `die()`.

---
## ex02

This exercise (ex02) implements a DiamondTrap-style class that demonstrates
multiple inheritance (a diamond pattern) and how Python's Method Resolution
Order (MRO) resolves constructor and method calls. The `DiamondTrap` class
inherits behavior from `ScavTrap` and `FragTrap` (which themselves inherit
from `ClapTrap`). It uses `@property` and corresponding setters/getters to
manage attributes (for example `eyes` and `hairs`) while providing small
compatibility wrappers (like `set_eyes` / `get_eyes`) required by the
exercise tester.

Key points:
- Multiple inheritance resolved via MRO (C3 linearization).
- Use `super()` to correctly initialize the MRO chain.
- Use `@property` and `@<prop>.setter` to control attribute access and keep
  the instance `__dict__` consistent for the tester output.

| Concept                 | Meaning                                       | Usage                    |
| ----------------------- | --------------------------------------------- | ------------------------ |
| `@property`             | Turns a method into attribute-like getter     | `obj.eyes`               |
| `@eyes.setter`          | Defines how the attribute is modified         | `obj.eyes = "blue"`      |
| `set_eyes` / `get_eyes` | Old-style wrappers required by Piscine tester | Simply call the property |


```sql
            Character (ABC)
                 │
         ┌───────┴────────┐
         │                │
     Baratheon        Lannister
         │                │
         └───────┬────────┘
                 │
               King
          (a DiamondTrap)

```
```
   Caller: Joffrey.set_eyes("blue")
              │
              ▼
        set_eyes wrapper
              │
              ▼
        property setter (eyes)
              │
    self.__dict__["eyes"] = "blue"
              │
              ▼
        instance __dict__ updated
```

- DiamondTrap inherits from both ScavTrap and FragTrap, which themselves inherit from ClapTrap.
- This forms the diamond problem, handled in Python by MRO (Method Resolution Order).
- Uses properties to safely manage attributes like name, hit_points, etc.

✅ Key Takeaways from the Diagrams
1. ABC + Abstract Methods → Forces subclasses to implement key functionality (Exercise 00).
2. Single Inheritance → Simple parent-child relationships (Exercise 01).
3. Multiple Inheritance + Diamond Problem → Python resolves conflicts using MRO (Exercise 02).
4. @property and @setter → Manage access to sensitive attributes safely.


### **1. What the Exercise Wants**

You must create **Joffrey Baratheon**, a character who inherits from **both**:

* `Baratheon`
* `Lannister`

This is **multiple inheritance** (a “diamond” pattern).

But Joffrey is “weird,” so:

* You must change his physical characteristics **using Properties**.
* The tester uses:

  * `Joffrey.set_eyes("blue")`
  * `Joffrey.set_hairs("light")`
  * `Joffrey.get_eyes()`
  * `Joffrey.get_hairs()`

So your class must support **property-based getters/setters** *and* additional wrapper functions.

Expected output:
The `.eyes` and `.hairs` attributes must change appropriately in `__dict__`.

---

### **2. Explanation of Your Code**

Here is what every part does.

---

### **Class Declaration**

```python
class King(Baratheon, Lannister):
```

* `King` inherits **first** from `Baratheon`, then from `Lannister`.
* The method resolution order (**MRO**) determines which parent initializes first.

---

### **Constructor**

```python
def __init__(self, first_name: str, is_alive: bool = True):
    super().__init__(first_name, is_alive)
```

* `super()` calls the **first parent** in the MRO (`Baratheon.__init__`).
* That parent sets:

  ```python
  family_name = "Baratheon"
  eyes = "brown"
  hairs = "dark"
  ```
* You intentionally **do not override** these attributes, because Joffrey begins with Baratheon features.

---

### **3. Properties**

This exercise introduces **Python properties**, a powerful mechanism for controlling attribute access.

---

### **Property: eyes**

```python
@property
def eyes(self):
    return self.__dict__.get("eyes")
```

* Defines how the attribute `eyes` is *read*.
* `self.eyes` now calls this getter.

### Setter:

```python
@eyes.setter
def eyes(self, color):
    self.__dict__["eyes"] = color
```

* Defines how the attribute `eyes` is *updated*.
* `self.eyes = "blue"` will modify `__dict__` properly.

---

### **Property: hair**

Works exactly like `eyes`.

---

### **4. Wrapper methods (required by tester)**

The tester uses:

```
Joffrey.set_eyes("blue")
Joffrey.get_eyes()
```

So you provide **legacy-style** getters and setters:

```python
def set_eyes(self, color):
    self.eyes = color   # uses the property setter

def get_eyes(self):
    return self.eyes    # uses the property getter
```

These wrappers rely on the property, ensuring clean design.

---

### **5. Why Properties Are Needed Here**

The subject says:

> “You must use the Properties to change the physical characteristics.”

Two reasons:

### **1. Avoid overriding parent attributes incorrectly**

Parents define `eyes` and `hair` differently.
The exercise wants you to **centralize attribute control** in the `King` class.

### **2. Ensure `__dict__` stays correct**

The expected output checks:

* keys must be `"eyes"` and `"hair"`
* values must update correctly

Using the property ensures all changes pass through controlled code.

---

### **6. Why Multiple Inheritance Matters**

The class:

```python
class King(Baratheon, Lannister):
```

Creates the **diamond problem**:

```
      Character
      /      \
Baratheon   Lannister
      \      /
        King
```

Python resolves this using the **Method Resolution Order (MRO)**.
Thus, only one of the parent constructors runs on `super()` → Baratheon’s.

This explains why Joffrey starts as:

```python
{'family_name': 'Baratheon', 'eyes': 'brown', 'hairs': 'dark'}
```

---

### **7. Key Takeaway Notions From This Exercise**

This exercise is specifically designed to teach several advanced Python OOP concepts.


#### **✓ 1. Multiple Inheritance**

You learn how a class can inherit from **two parents** and how MRO determines:

* which constructor runs,
* which methods get priority.

---

#### **✓ 2. Method Resolution Order (MRO)**

In:

```python
class King(Baratheon, Lannister)
```

the order matters:

`King → Baratheon → Lannister → Character → object`

This affects initialization and method lookup.

---

#### **✓ 3. Properties (`@property`, setter)**

You learn how to:

* control access to attributes,
* validate or intercept changes,
* design clean and safe APIs.

Properties allow you to treat methods **as if they were attributes**:

```python
Joffrey.eyes = "blue"   # calls setter
Joffrey.eyes            # calls getter
```

---

#### **✓ 4. Public API vs internal logic**

You create modern property access:

```python
@eyes.setter
@eyes.getter
```

but also support the old “Java-style” methods:

```
set_eyes()
get_eyes()
```

because the tester expects them.

---

#### **✓ 5. Manipulating `__dict__` explicitly**

To guarantee correct tester output, you update attributes directly in `self.__dict__`.

This teaches:

* how Python stores instance attributes internally,
* how property decorators interact with instance storage.

---

#### **✓ 6. Avoiding duplication in constructors**

You do **not** redefine attributes—inheritance handles them.
You only override behavior where necessary (with properties).


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


### *1. What Your Code Does**

You created a class `calculator` containing three mathematical vector operations:

* **dotproduct**
* **add_vec**
* **sous_vec** (subtraction)

All three are decorated with:

```python
@staticmethod
```

This means you can call them directly on the class without creating an object.

Example:

```python
calculator.dotproduct(a, b)
```

You **do NOT** need to do this:

```python
calc = calculator()     # No instantiation needed
calc.dotproduct(a, b)
```

This is exactly what the exercise requires.

---

### **2. Detailed Explanation of Each Part**

---

#### **Class Definition**

```python
class calculator:
```

Defines a namespace that contains functions related to vector operations.

No initialization (`__init__`) needed because all methods are static.

---

#### **Decorator: @staticmethod**

Each method is preceded by:

```python
@staticmethod
```

This means:

* The method does NOT take `self`
* The method does NOT depend on instance data
* The method belongs to the class, not the instance

So you can call:

```python
calculator.dotproduct([1,2],[3,4])
```

---

#### **dotproduct**

```python
@staticmethod
def dotproduct(v1, v2):
    result = sum(x * y for x, y in zip(v1, v2))
    print(f"Dot product is: {result}")
```

Calculates:

```
x1*y1 + x2*y2 + x3*y3 + ...
```

`zip` pairs elements from both vectors.

Example for `[5, 10, 2]` and `[2, 4, 3]`:

```
5*2 + 10*4 + 2*3 = 10 + 40 + 6 = 56
```

---

#### **add_vec**

```python
result = [float(x + y) for x, y in zip(v1, v2)]
```

Produces:

```
[5+2, 10+4, 2+3] → [7.0, 14.0, 5.0]
```

Wrapped in a print:

```
Add Vector is : [7.0, 14.0, 5.0]
```

Spacing is made to match the expected output.

---

#### **sous_vec** (subtraction)

```python
result = [float(x - y) for x, y in zip(v1, v2)]
```

Produces:

```
[5-2, 10-4, 2-3] → [3.0, 6.0, -1.0]
```

Correct output format:

```
Sous Vector is: [3.0, 6.0, -1.0]
```

---

### **3. Why @staticmethod Is the Correct Decorator**

The exercise explicitly hints:

> "find a decorator that can help you to use the Methods of the calculator
> class without instantiating this class."

There are three choices:

| Decorator       | Behavior                                         |
| --------------- | ------------------------------------------------ |
| `@staticmethod` | Best for functions not needing class or instance |
| `@classmethod`  | Requires a `cls` argument, not relevant here     |
| No decorator    | Would require instantiation                      |

Because your vector functions:

* do not depend on the class,
* do not depend on any instance attributes,

`@staticmethod` is the perfect choice.

---

### **4. Key Takeaway Notions for This Exercise**


#### **✓ 1. Static Methods**

* Methods that belong to the class, **not** the object
* No `self`, no `cls`
* Called directly on the class
* Perfect for mathematical utilities

This is the core lesson.

---

#### **✓ 2. Decorators in Python**

* You learn how `@something` modifies a function
* In this case, making it "static" (no implicit arguments)

Understanding decorators is essential for future work with:

* properties
* class methods
* abstract methods
* Flask / Django routing
* data validation

---

#### **✓ 3. Encapsulation of Related Logic**

All vector operations belong inside one logical “calculator” class.

This teaches:

* Organization of code
* Namespacing through classes

---

#### **✓ 4. Vector math using `zip`**

* `zip(v1, v2)` pairs elements
* Useful for element-wise operations

---

#### **✓ 5. List comprehensions**

Creating new lists concisely:

```python
[x + y for x, y in zip(v1, v2)]
```

---

#### **✓ 6. Clean formatting with f-strings**

For printing results:

```python
print(f"Dot product is: {result}")
```
