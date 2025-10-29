#! usr/bin/env python3


# square(x) – 平方
def square(x: int | float) -> int | float:
    """square 平方 (x^2)"""
    return x * x

#pow(x) – 自身的次方 (multiply x by itself x times)
def pow(x: int | float) -> int | float:
    """pow 自身次方 (multiply x by itself x times) """
    # result = 1
    # for i in range(int(x)): # 如果是小數，後面會做近似
    #     result *= x
    return x ** x # 如果是小數，可以用簡單乘法近似 #Python supports x ** x directly for floats → 自身次方

# outer() Function (Closure / 外層函數)
# Closure magic: inner() remembers count even after outer() finishes → 閉包記住外層狀態
# - count = 0 → 每次 inner() 被呼叫時，增加 1
# - nonlocal count → 讓 inner() 可以修改外層變數 count
# - function(...) → 用傳入的 function (square 或 pow) 計算結果
# - Return inner → 生成可重複呼叫的物件
def outer(x: int | float, function) -> object: count = 0
    """Closure  外層函數
    Defines a variable (like x, count) and defines inner() inside it
    外部函數建立本地變數並定義內部函數

    inner() closes over variables from outer()
    inner() 封閉外部變數形成閉包
    """
    inner_count = 0  # keep track of how many times inner is called

    def inner() -> float:
        """Uses the x and count from outer() even after outer() finished
        內部函數記住外部變數（閉包 closure）
        """
        nonlocal inner_count  # allow inner() to modify outer() variable
        inner_count += 1
        result = function(x ** inner_count)  # apply function to x raised to count
        return result
    
    return inner # return the callable inner()



### EXAMPLES ####

# my_counter = outer(3, square)
# print(my_counter())  # 第一次呼叫 → count=1 → 3^1=3 → square(3)=9
# print(my_counter())  # 第二次呼叫 → count=2 → 3^2=9 → square(9)=81
# print(my_counter())  # 第三次呼叫 → count=3 → 3^3=27 → square(27)=729


# another_counter = outer(1.5, pow)
# print(another_counter())  # count=1 → 1.5^1=1.5 → pow(1.5)=1.5^1.5≈1.837
# print(another_counter())  # count=2 → 1.5^2=2.25 → pow(2.25)=2.25^2.25≈3.056
# print(another_counter())  # count=3 → 1.5^3=3.375 → pow(3.375)=3.375^3.375≈30.426

###################