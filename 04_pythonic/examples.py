#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
04_pythonic/examples.py
Python特色功能示例 - 专为C++程序员设计

运行方式:
python examples.py
"""

def print_separator(title):
    """打印分隔符"""
    print(f"\n{'='*60}")
    print(f" {title}")
    print(f"{'='*60}")

def demo_list_comprehensions():
    """演示列表推导式"""
    print_separator("1. 列表推导式")
    
    # 基本列表推导式
    # 传统方式 vs 推导式
    print("传统方式:")
    squares_traditional = []
    for i in range(10):
        squares_traditional.append(i * i)
    print(f"squares_traditional = {squares_traditional}")
    
    print("\n推导式方式:")
    squares_comprehension = [i * i for i in range(10)]
    print(f"squares_comprehension = {squares_comprehension}")
    
    # 带条件的推导式
    print("\n带条件的推导式:")
    even_squares = [i * i for i in range(10) if i % 2 == 0]
    print(f"even_squares = {even_squares}")
    
    # 多层嵌套推导式
    print("\n嵌套推导式:")
    matrix = [[i * j for j in range(1, 4)] for i in range(1, 4)]
    print(f"multiplication table = {matrix}")
    
    # 函数调用推导式
    print("\n函数调用推导式:")
    words = ["hello", "world", "python", "programming"]
    word_lengths = [len(word) for word in words]
    word_upper = [word.upper() for word in words]
    print(f"words = {words}")
    print(f"word_lengths = {word_lengths}")
    print(f"word_upper = {word_upper}")
    
    # 复杂表达式
    print("\n复杂表达式:")
    numbers = list(range(-5, 6))
    abs_squares = [abs(x) ** 2 for x in numbers if x != 0]
    print(f"numbers = {numbers}")
    print(f"abs_squares = {abs_squares}")
    
    return squares_comprehension, even_squares

def demo_dict_comprehensions():
    """演示字典推导式"""
    print_separator("2. 字典推导式")
    
    # 基本字典推导式
    print("基本字典推导式:")
    word_lengths = {word: len(word) for word in ["hello", "world", "python", "programming"]}
    print(f"word_lengths = {word_lengths}")
    
    # 条件字典推导式
    print("\n条件字典推导式:")
    scores = {"Alice": 85, "Bob": 92, "Charlie": 78, "David": 95}
    excellent_scores = {name: score for name, score in scores.items() if score >= 90}
    print(f"scores = {scores}")
    print(f"excellent_scores = {excellent_scores}")
    
    # 值转换
    print("\n值转换:")
    temperature_celsius = {"Monday": 20, "Tuesday": 22, "Wednesday": 25}
    temperature_fahrenheit = {day: temp * 9/5 + 32 for day, temp in temperature_celsius.items()}
    print(f"celsius = {temperature_celsius}")
    print(f"fahrenheit = {temperature_fahrenheit}")
    
    # 键值互换
    print("\n键值互换:")
    original = {"a": 1, "b": 2, "c": 3}
    swapped = {v: k for k, v in original.items()}
    print(f"original = {original}")
    print(f"swapped = {swapped}")
    
    return word_lengths, temperature_fahrenheit

def demo_set_comprehensions():
    """演示集合推导式"""
    print_separator("3. 集合推导式")
    
    # 基本集合推导式
    print("基本集合推导式:")
    squares = {x ** 2 for x in range(10)}
    print(f"squares = {squares}")
    
    # 字符串去重
    print("\n字符串字符去重:")
    text = "abracadabra"
    unique_chars = {char for char in text}
    print(f"text = '{text}'")
    print(f"unique_chars = {unique_chars}")
    
    # 条件过滤
    print("\n条件过滤:")
    numbers = range(1, 21)
    primes_less_than_20 = {n for n in numbers if n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))}
    print(f"primes_less_than_20 = {primes_less_than_20}")
    
    return unique_chars

def demo_generators():
    """演示生成器"""
    print_separator("4. 生成器")
    
    # 生成器函数
    def fibonacci(n):
        """斐波那契数列生成器"""
        a, b = 0, 1
        for _ in range(n):
            yield a
            a, b = b, a + b
    
    print("生成器函数:")
    fib = fibonacci(10)
    print(f"fibonacci numbers: {list(fib)}")
    
    # 生成器表达式
    print("\n生成器表达式:")
    squares_gen = (x ** 2 for x in range(10))
    print(f"squares_gen = {list(squares_gen)}")
    
    # 惰性求值演示
    print("\n惰性求值:")
    import time
    
    def expensive_operation(n):
        print(f"Performing expensive operation on {n}...")
        time.sleep(0.1)  # 模拟耗时操作
        return n * n
    
    # 列表推导式 - 立即求值
    start = time.time()
    squares_list = [expensive_operation(x) for x in range(5)]
    list_time = time.time() - start
    print(f"列表推导式耗时: {list_time:.2f}秒")
    
    # 生成器表达式 - 按需求值
    start = time.time()
    squares_gen = (expensive_operation(x) for x in range(5))
    gen_time = time.time() - start
    print(f"生成器表达式创建耗时: {gen_time:.2f}秒")
    
    # 无限生成器
    def infinite_counter():
        """无限计数器"""
        count = 0
        while True:
            yield count
            count += 1
    
    print("\n无限生成器 (只显示前5个):")
    counter = infinite_counter()
    first_five = [next(counter) for _ in range(5)]
    print(f"first_five = {first_five}")
    
    return fibonacci

def demo_decorators():
    """演示装饰器"""
    print_separator("5. 装饰器")
    
    # 基本装饰器
    def timing_decorator(func):
        """计时装饰器"""
        import time
        def wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            print(f"{func.__name__} 耗时: {end - start:.4f}秒")
            return result
        return wrapper
    
    # 使用装饰器
    @timing_decorator
    def slow_function():
        """慢函数"""
        import time
        time.sleep(0.5)
        return "Function completed"
    
    print("计时装饰器:")
    result = slow_function()
    print(f"结果: {result}")
    
    # 带参数的装饰器
    def repeat_decorator(times):
        """重复执行装饰器"""
        def decorator(func):
            def wrapper(*args, **kwargs):
                results = []
                for i in range(times):
                    print(f"第 {i+1} 次执行 {func.__name__}")
                    result = func(*args, **kwargs)
                    results.append(result)
                return results
            return wrapper
        return decorator
    
    @repeat_decorator(3)
    def greet(name):
        """问候函数"""
        return f"Hello, {name}!"
    
    print("\n重复执行装饰器:")
    greetings = greet("Alice")
    print(f"greetings = {greetings}")
    
    # 类装饰器
    def add_method(cls):
        """添加方法的装饰器"""
        def new_method(self):
            return f"This is a dynamically added method to {self.__class__.__name__}"
        
        cls.dynamic_method = new_method
        return cls
    
    @add_method
    class MyClass:
        def __init__(self, name):
            self.name = name
        
        def original_method(self):
            return f"Original method: {self.name}"
    
    print("\n类装饰器:")
    obj = MyClass("Test")
    print(f"original_method: {obj.original_method()}")
    print(f"dynamic_method: {obj.dynamic_method()}")
    
    # 属性装饰器
    class LazyProperty:
        """懒加载属性装饰器"""
        def __init__(self, func):
            self.func = func
        
        def __get__(self, instance, owner):
            if instance is None:
                return self
            value = self.func(instance)
            setattr(instance, self.func.__name__, value)
            return value
    
    class ExpensiveClass:
        def __init__(self):
            self._expensive_data = None
        
        @LazyProperty
        def expensive_data(self):
            """懒加载的昂贵数据"""
            print("计算昂贵数据...")
            import time
            time.sleep(0.2)
            self._expensive_data = [i ** 2 for i in range(1000)]
            return self._expensive_data
    
    print("\n懒加载属性装饰器:")
    expensive_obj = ExpensiveClass()
    print("第一次访问expensive_data:")
    data1 = expensive_obj.expensive_data
    print(f"数据长度: {len(data1)}")
    
    print("第二次访问expensive_data:")
    data2 = expensive_obj.expensive_data
    print(f"数据长度: {len(data2)}")
    
    return timing_decorator, repeat_decorator

def demo_context_managers():
    """演示上下文管理器"""
    print_separator("6. 上下文管理器")
    
    # 基本with语句
    print("文件操作with语句:")
    import os
    
    # 写文件
    try:
        with open("test_file.txt", "w", encoding="utf-8") as f:
            f.write("Hello, World!\n")
            f.write("这是测试文件\n")
            f.write("Python上下文管理器示例\n")
        print("文件写入成功")
        
        # 读文件
        with open("test_file.txt", "r", encoding="utf-8") as f:
            content = f.read()
        print(f"文件内容:\n{content}")
        
    finally:
        # 清理测试文件
        if os.path.exists("test_file.txt"):
            os.remove("test_file.txt")
    
    # 自定义上下文管理器
    class Timer:
        """计时器上下文管理器"""
        def __init__(self, name="Operation"):
            self.name = name
        
        def __enter__(self):
            import time
            self.start = time.time()
            print(f"开始 {self.name}")
            return self
        
        def __exit__(self, exc_type, exc_val, exc_tb):
            import time
            self.end = time.time()
            elapsed = self.end - self.start
            print(f"{self.name} 完成，耗时: {elapsed:.4f}秒")
            return False  # 不抑制异常
    
    print("\n自定义上下文管理器:")
    with Timer("数据处理"):
        import time
        time.sleep(0.3)
        # 模拟数据处理
        data = [i ** 2 for i in range(1000)]
    
    # 数据库连接模拟
    class DatabaseConnection:
        """数据库连接上下文管理器"""
        def __init__(self, db_url):
            self.db_url = db_url
            self.connection = None
        
        def __enter__(self):
            print(f"连接到数据库: {self.db_url}")
            self.connection = f"Connection to {self.db_url}"
            return self.connection
        
        def __exit__(self, exc_type, exc_val, exc_tb):
            print("关闭数据库连接")
            self.connection = None
            return False
    
    print("\n数据库连接上下文管理器:")
    with DatabaseConnection("postgresql://localhost/mydb") as conn:
        print(f"使用连接: {conn}")
        # 执行数据库操作
        print("执行查询...")
    
    # contextlib.contextmanager装饰器
    from contextlib import contextmanager
    
    @contextmanager
    def temp_change_directory(path):
        """临时改变目录的上下文管理器"""
        import os
        old_path = os.getcwd()
        print(f"切换到目录: {path}")
        os.chdir(path)
        try:
            yield
        finally:
            print(f"恢复到原目录: {old_path}")
            os.chdir(old_path)
    
    print("\n使用contextmanager装饰器:")
    import tempfile
    import os
    
    with tempfile.TemporaryDirectory() as temp_dir:
        print(f"创建临时目录: {temp_dir}")
        
        # 在临时目录中工作
        original_cwd = os.getcwd()
        print(f"当前目录: {original_cwd}")
        
        with temp_change_directory(temp_dir):
            current_cwd = os.getcwd()
            print(f"在上下文中，当前目录: {current_cwd}")
            # 在临时目录中创建文件
            with open("temp_file.txt", "w") as f:
                f.write("Temporary file content")
            
            if os.path.exists("temp_file.txt"):
                print("临时文件创建成功")
        
        print(f"退出上下文后，当前目录: {os.getcwd()}")
    
    return Timer, DatabaseConnection

def demo_exception_handling():
    """演示异常处理"""
    print_separator("7. 异常处理")
    
    # 基本异常处理
    def divide_numbers(a, b):
        """除法函数"""
        try:
            result = a / b
        except ZeroDivisionError:
            print("错误: 除数不能为零")
            return None
        except TypeError as e:
            print(f"错误: 类型错误 - {e}")
            return None
        else:
            print(f"计算成功: {a} / {b} = {result}")
            return result
        finally:
            print("除法操作完成")
    
    print("基本异常处理:")
    divide_numbers(10, 2)
    divide_numbers(10, 0)
    divide_numbers("10", 2)
    
    # 多异常捕获
    print("\n多异常捕获:")
    def process_data(data):
        """数据处理函数"""
        try:
            # 尝试转换为整数
            num = int(data)
            # 尝试除法
            result = 100 / num
            return result
        except (ValueError, TypeError) as e:
            print(f"数据转换错误: {e}")
            return None
        except ZeroDivisionError:
            print("错误: 不能除以零")
            return None
        except Exception as e:
            print(f"未知错误: {e}")
            return None
    
    print(process_data("50"))
    print(process_data("abc"))
    print(process_data("0"))
    
    # 异常链
    print("\n异常链:")
    def validate_and_process(data):
        """验证并处理数据"""
        try:
            if not isinstance(data, (int, float)):
                raise ValueError("数据必须是数字")
            if data < 0:
                raise ValueError("数据不能为负数")
            return data ** 2
        except ValueError as e:
            raise RuntimeError(f"数据处理失败: {data}") from e
    
    try:
        result = validate_and_process(-5)
    except RuntimeError as e:
        print(f"捕获异常: {e}")
        print(f"原始异常: {e.__cause__}")
    
    # 自定义异常
    class CustomError(Exception):
        """自定义异常类"""
        def __init__(self, message, error_code):
            super().__init__(message)
            self.error_code = error_code
        
        def __str__(self):
            return f"Error {self.error_code}: {self.args[0]}"
    
    def risky_operation(operation_type):
        """有风险的操作"""
        if operation_type == "invalid":
            raise CustomError("无效的操作类型", 400)
        elif operation_type == "forbidden":
            raise CustomError("禁止的操作", 403)
        else:
            return "操作成功"
    
    print("\n自定义异常:")
    for op_type in ["valid", "invalid", "forbidden"]:
        try:
            result = risky_operation(op_type)
            print(f"{op_type}: {result}")
        except CustomError as e:
            print(f"{op_type}: {e}")
    
    return divide_numbers, validate_and_process

def demo_pythonic_patterns():
    """演示Pythonic编程模式"""
    print_separator("8. Pythonic编程模式")
    
    # 条件表达式 (三元运算符)
    print("条件表达式:")
    age = 20
    # 传统方式
    if age >= 18:
        status_traditional = "成年人"
    else:
        status_traditional = "未成年"
    
    # Pythonic方式
    status_pythonic = "成年人" if age >= 18 else "未成年"
    
    print(f"年龄: {age}")
    print(f"传统方式: {status_traditional}")
    print(f"Pythonic方式: {status_pythonic}")
    
    # 解包赋值
    print("\n解包赋值:")
    # 变量交换
    a, b = 5, 10
    print(f"交换前: a = {a}, b = {b}")
    a, b = b, a
    print(f"交换后: a = {a}, b = {b}")
    
    # 函数返回多值
    def get_user_info():
        return "Alice", 25, "Beijing"
    
    name, age, city = get_user_info()
    print(f"用户信息: 姓名={name}, 年龄={age}, 城市={city}")
    
    # 扩展解包
    numbers = [1, 2, 3, 4, 5]
    first, *middle, last = numbers
    print(f"列表解包: first={first}, middle={middle}, last={last}")
    
    # 枚举和zip
    print("\n枚举和zip:")
    fruits = ["apple", "banana", "orange"]
    prices = [1.2, 0.8, 1.5]
    
    # 枚举
    print("枚举:")
    for index, fruit in enumerate(fruits):
        print(f"  {index}: {fruit}")
    
    # zip
    print("\nzip:")
    for fruit, price in zip(fruits, prices):
        print(f"  {fruit}: ${price}")
    
    # 组合使用
    print("\n枚举和zip组合:")
    for index, (fruit, price) in enumerate(zip(fruits, prices)):
        print(f"  {index+1}. {fruit}: ${price}")
    
    # 列表切片技巧
    print("\n列表切片技巧:")
    data = list(range(10))
    print(f"原列表: {data}")
    print(f"前3个元素: {data[:3]}")
    print(f"后3个元素: {data[-3:]}")
    print(f"每隔2个元素: {data[::2]}")
    print(f"反转列表: {data[::-1]}")
    
    # 使用any和all
    print("\n使用any和all:")
    numbers = [2, 4, 6, 8, 10]
    print(f"列表: {numbers}")
    print(f"都是偶数? {all(x % 2 == 0 for x in numbers)}")
    print(f"有大于9的数? {any(x > 9 for x in numbers)}")
    
    # 使用collections模块
    from collections import Counter, defaultdict
    
    print("\n使用collections.Counter:")
    words = ["apple", "banana", "apple", "orange", "banana", "apple"]
    word_count = Counter(words)
    print(f"单词计数: {word_count}")
    print(f"最常见单词: {word_count.most_common(2)}")
    
    print("\n使用collections.defaultdict:")
    d = defaultdict(list)
    d['fruits'].extend(['apple', 'banana'])
    d['vegetables'].extend(['carrot', 'broccoli'])
    print(f"defaultdict: {dict(d)}")
    
    return None

def main():
    """主函数 - 运行所有Pythonic功能示例"""
    print("Python特色功能示例 - 专为C++程序员设计")
    print("=" * 60)
    
    demo_list_comprehensions()
    demo_dict_comprehensions()
    demo_set_comprehensions()
    demo_generators()
    demo_decorators()
    demo_context_managers()
    demo_exception_handling()
    demo_pythonic_patterns()
    
    print_separator("总结")
    print("Pythonic编程 vs C++ 主要差异:")
    print("✓ 推导式 - 简洁的集合构建方式")
    print("✓ 生成器 - 惰性求值和内存优化")
    print("✓ 装饰器 - 优雅的函数/类增强")
    print("✓ 上下文管理器 - 自动资源管理")
    print("✓ 异常处理 - 更简洁的错误处理")
    print("✓ 条件表达式 - 简化条件逻辑")
    print("✓ 解包赋值 - 优雅的变量赋值")
    print("✓ 内置函数 - 丰富的工具函数")
    
    print("\n学习建议:")
    print("• 多使用推导式 - 让代码更简洁")
    print("• 掌握生成器 - 优化内存使用")
    print("• 理解装饰器 - 学会函数式编程思维")
    print("• 拥抱上下文管理器 - 避免资源泄漏")
    print("• 使用内置函数 - 不要重新发明轮子")
    print("• 追求Pythonic - 写出优雅的Python代码")

if __name__ == "__main__":
    main()