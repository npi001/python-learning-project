# 04_pythonic - Python特色功能

## 概述
这个模块展示Python的独特功能和"Pythonic"编程风格，让C++程序员体验Python的魅力。

## 文件说明
- `examples.py` - Python特色功能示例
- `exercises.py` - 练习题
- `README.md` - 本文件

## 学习目标
完成本模块后，你应该能够：
1. 熟练使用各种推导式
2. 掌握生成器和迭代器
3. 理解装饰器的应用
4. 使用上下文管理器
5. 掌握异常处理技巧
6. 编写"Pythonic"的代码

## Python特色功能

### 1. 推导式 (Comprehensions)

#### 列表推导式
```python
# C++风格循环
squares = []
for i in range(10):
    squares.append(i * i)

# Pythonic列表推导式
squares = [i * i for i in range(10)]

# 带条件
even_squares = [i * i for i in range(10) if i % 2 == 0]
```

#### 字典推导式
```python
# 传统方式
word_lengths = {}
for word in ["hello", "world", "python"]:
    word_lengths[word] = len(word)

# Pythonic字典推导式
word_lengths = {word: len(word) for word in ["hello", "world", "python"]}
```

#### 集合推导式
```python
# 获取字符串中的唯一字符
unique_chars = {char for char in "abracadabra"}
# 结果：{'a', 'b', 'c', 'd', 'r'}
```

### 2. 生成器 (Generators)

#### 惰性求值
```python
def fibonacci(n):
    """生成斐波那契数列"""
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# 不会立即计算所有值，按需生成
fib = fibonacci(10)
print(next(fib))  # 0
print(next(fib))  # 1

# 或者用for循环
fib = fibonacci(10)
for num in fib:
    print(num)
```

#### 生成器表达式
```python
# 类似列表推导式，但不创建完整列表
sum_squares = sum(i * i for i in range(1000000))  # 内存友好
```

### 3. 装饰器 (Decorators)

#### 函数装饰器
```python
def timing_decorator(func):
    """计时装饰器"""
    import time
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper

@timing_decorator
def slow_function():
    import time
    time.sleep(1)
    return "Done"

slow_function()  # 会打印执行时间
```

#### 类装饰器
```python
def add_method(cls):
    def new_method(self):
        print("Added method!")
    cls.new_method = new_method
    return cls

@add_method
class MyClass:
    pass

obj = MyClass()
obj.new_method()  # "Added method!"
```

### 4. 上下文管理器 (Context Managers)

#### with语句
```python
# 文件操作 - 自动关闭文件
with open("file.txt", "r") as f:
    content = f.read()
# 文件自动关闭，即使出现异常

# 线程锁
from threading import Lock
lock = Lock()
with lock:
    # 临界区代码
    critical_operation()
# 锁自动释放
```

#### 自定义上下文管理器
```python
class Timer:
    def __enter__(self):
        import time
        self.start = time.time()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        import time
        self.end = time.time()
        print(f"Elapsed: {self.end - self.start:.4f}s")

with Timer():
    import time
    time.sleep(0.5)
# 输出: Elapsed: 0.5000s
```

### 5. 异常处理

#### 多异常捕获
```python
try:
    # 可能出错的代码
    result = 10 / 0
except ZeroDivisionError:
    print("除零错误")
except (ValueError, TypeError) as e:
    print(f"类型错误: {e}")
except Exception as e:
    print(f"未知错误: {e}")
else:
    print("没有异常")
finally:
    print("总是执行")
```

#### 异常链
```python
try:
    try:
        int("abc")
    except ValueError as e:
        raise ValueError("无效的数字格式") from e
except ValueError as e:
    print(f"错误: {e}")
    print(f"原因: {e.__cause__}")
```

### 6. Pythonic编程模式

#### 条件表达式 (三元运算符)
```python
# C++风格
if x > 0:
    result = "positive"
else:
    result = "non-positive"

# Pythonic
result = "positive" if x > 0 else "non-positive"
```

#### 解包赋值
```python
# 交换变量
a, b = b, a

# 函数返回多值
def get_position():
    return 10, 20

x, y = get_position()

# 列表解包
first, *middle, last = [1, 2, 3, 4, 5]
# first=1, middle=[2,3,4], last=5
```

#### 枚举和zip
```python
fruits = ["apple", "banana", "orange"]
prices = [1.2, 0.8, 1.5]

# 同时获取索引和值
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")

# 同时遍历多个序列
for fruit, price in zip(fruits, prices):
    print(f"{fruit}: ${price}")
```

## 运行示例
```bash
python examples.py
```

## 完成练习
```bash
python exercises.py
```

## 预计学习时间
2-3周

## 下一步
完成本模块后，继续学习 `05_advanced` 模块。