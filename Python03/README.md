# OOP (Object Oriented Programming)

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
