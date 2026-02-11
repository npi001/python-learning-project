#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
01_basics/examples.py
Python基础语法示例 - 专为C++程序员设计

运行方式:
python examples.py
"""

def print_separator(title):
    """打印分隔符"""
    print(f"\n{'='*60}")
    print(f" {title}")
    print(f"{'='*60}")

def demo_variables_and_types():
    """演示变量和数据类型"""
    print_separator("1. 变量和数据类型")
    
    # Python是动态类型语言，不需要声明类型
    # 相比C++: int age = 25;
    age = 25
    name = "Alice"
    height = 1.68
    is_student = True
    
    print(f"age = {age}, type: {type(age)}")
    print(f"name = {name}, type: {type(name)}")
    print(f"height = {height}, type: {type(height)}")
    print(f"is_student = {is_student}, type: {type(is_student)}")
    
    # 动态类型 - 可以重新赋值不同类型
    # C++中这是不允许的
    variable = "Hello"
    print(f"variable = {variable}, type: {type(variable)}")
    variable = 42
    print(f"variable = {variable}, type: {type(variable)}")
    
    # 类型转换
    str_num = "123"
    num = int(str_num)
    print(f"int('123') = {num}, type: {type(num)}")
    
    float_num = float(num)
    print(f"float({num}) = {float_num}, type: {type(float_num)}")

def demo_operators():
    """演示运算符"""
    print_separator("2. 运算符")
    
    a = 10
    b = 3
    
    # 算术运算符
    print(f"a = {a}, b = {b}")
    print(f"a + b = {a + b}")      # 13
    print(f"a - b = {a - b}")      # 7
    print(f"a * b = {a * b}")      # 30
    print(f"a / b = {a / b}")      # 3.333... (浮点数除法)
    print(f"a // b = {a // b}")    # 3 (整数除法)
    print(f"a % b = {a % b}")       # 1 (取余)
    print(f"a ** b = {a ** b}")    # 1000 (幂运算)
    
    # 比较运算符
    print(f"a == b: {a == b}")     # False
    print(f"a != b: {a != b}")     # True
    print(f"a > b: {a > b}")       # True
    print(f"a <= b: {a <= b}")     # False
    
    # 逻辑运算符
    x = True
    y = False
    print(f"x and y: {x and y}")  # False
    print(f"x or y: {x or y}")      # True
    print(f"not x: {not x}")        # False
    
    # 字符串运算
    str1 = "Hello"
    str2 = "World"
    print(f"'{str1}' + '{str2}' = '{str1 + str2}'")  # 字符串连接
    print(f"'{str1}' * 3 = '{str1 * 3}'")           # 字符串重复

def demo_statements():
    """演示条件语句和循环"""
    print_separator("3. 条件语句和循环")
    
    # if语句 - 注意使用缩进而不是大括号
    score = 85
    print(f"Score: {score}")
    
    if score >= 90:
        grade = "A"
        comment = "Excellent"
    elif score >= 80:
        grade = "B"
        comment = "Good"
    elif score >= 70:
        grade = "C"
        comment = "Average"
    elif score >= 60:
        grade = "D"
        comment = "Below Average"
    else:
        grade = "F"
        comment = "Fail"
    
    print(f"Grade: {grade}, Comment: {comment}")
    
    # for循环
    print("\nfor循环示例:")
    for i in range(5):  # range(5) = [0, 1, 2, 3, 4]
        print(f"  Count: {i}")
    
    # 遍历列表
    fruits = ["apple", "banana", "orange"]
    print("\n遍历水果列表:")
    for fruit in fruits:
        print(f"  Fruit: {fruit}")
    
    # 带索引的遍历
    print("\n带索引遍历:")
    for index, fruit in enumerate(fruits):
        print(f"  {index}: {fruit}")
    
    # while循环
    print("\nwhile循环示例:")
    count = 0
    while count < 3:
        print(f"  Count: {count}")
        count += 1  # Python没有++或--运算符
    
    # break和continue
    print("\nbreak和continue示例:")
    for i in range(10):
        if i == 3:
            continue  # 跳过3
        if i == 7:
            break     # 遇到7就退出
        print(f"  {i}")

def demo_functions():
    """演示函数定义和调用"""
    print_separator("4. 函数定义和调用")
    
    # 基本函数定义
    def greet(name):
        """简单的问候函数"""
        return f"Hello, {name}!"
    
    print(greet("Alice"))
    print(greet("Bob"))
    
    # 带默认参数的函数
    def greet_with_title(name, title="Mr."):
        """带默认参数的问候函数"""
        return f"Hello, {title} {name}!"
    
    print(greet_with_title("Smith"))          # 使用默认值
    print(greet_with_title("Johnson", "Dr.")) # 指定值
    
    # 带多个返回值的函数
    def get_name_parts(full_name):
        """将全名分解为名和姓"""
        parts = full_name.split()
        if len(parts) >= 2:
            return parts[0], " ".join(parts[1:])
        else:
            return full_name, ""
    
    first, last = get_name_parts("John Doe")
    print(f"First name: {first}, Last name: {last}")
    
    # 可变参数函数
    def sum_numbers(*args):
        """可变参数求和"""
        return sum(args)
    
    print(f"sum_numbers(1, 2, 3, 4, 5) = {sum_numbers(1, 2, 3, 4, 5)}")
    
    # 关键字参数
    def create_person(name, age, **kwargs):
        """创建人物信息字典"""
        person = {"name": name, "age": age}
        person.update(kwargs)
        return person
    
    person = create_person("Alice", 25, city="Beijing", job="Engineer")
    print(f"Person: {person}")
    
    # Lambda函数
    square = lambda x: x * x
    print(f"square(5) = {square(5)}")
    
    # 使用lambda和内置函数
    numbers = [1, 2, 3, 4, 5]
    squared = list(map(lambda x: x ** 2, numbers))
    print(f"Original: {numbers}")
    print(f"Squared: {squared}")

def demo_strings():
    """演示字符串操作"""
    print_separator("5. 字符串操作")
    
    text = "Hello, Python Programming!"
    
    # 基本操作
    print(f"Original: '{text}'")
    print(f"Length: {len(text)}")
    print(f"Upper: '{text.upper()}'")
    print(f"Lower: '{text.lower()}'")
    print(f"Title: '{text.title()}'")
    
    # 查找和替换
    print(f"Contains 'Python': {'Python' in text}")
    print(f"Find 'Python': {text.find('Python')}")
    print(f"Replace 'Python' with 'Java': '{text.replace('Python', 'Java')}'")
    
    # 分割和连接
    sentence = "This is a sample sentence"
    words = sentence.split()
    print(f"Split: {words}")
    print(f"Join with '-': {'-'.join(words)}")
    
    # 切片操作 - 这比C++的字符串操作强大得多
    text = "0123456789"
    print(f"Original: '{text}'")
    print(f"text[2:5] = '{text[2:5]}'")     # '234'
    print(f"text[:3] = '{text[:3]}'")       # '012'
    print(f"text[7:] = '{text[7:]}'")       # '789'
    print(f"text[::2] = '{text[::2]}'")     # '02468' (步长为2)
    print(f"text[::-1] = '{text[::-1]}'")   # '9876543210' (反转)
    
    # f-string格式化 (Python 3.6+)
    name = "Alice"
    age = 25
    height = 1.68
    
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Height: {height:.2f}")  # 保留两位小数
    print(f"Formatted: {name:10s} | {age:3d} | {height:6.2f}")
    
    # 字符串方法
    email = "  alice@example.com  "
    print(f"Original email: '{email}'")
    print(f"Stripped: '{email.strip()}'")
    print(f"Starts with 'alice': {email.strip().startswith('alice')}")
    print(f"Ends with '.com': {email.strip().endswith('.com')}")
    
    # 多行字符串
    multiline = """This is a
multiline string
that spans multiple
lines"""
    print(f"Multiline string:\n{multiline}")

def demo_list_operations():
    """演示列表基础操作"""
    print_separator("6. 列表基础操作")
    
    # 创建列表
    numbers = [1, 2, 3, 4, 5]
    mixed = [1, "hello", 3.14, True]
    print(f"Numbers: {numbers}")
    print(f"Mixed: {mixed}")
    
    # 列表操作
    print(f"Length: {len(numbers)}")
    print(f"First element: {numbers[0]}")
    print(f"Last element: {numbers[-1]}")
    print(f"Slice [1:3]: {numbers[1:3]}")
    
    # 修改列表
    numbers.append(6)
    print(f"After append(6): {numbers}")
    
    numbers.insert(0, 0)
    print(f"After insert(0, 0): {numbers}")
    
    numbers[3] = 99
    print(f"After numbers[3] = 99: {numbers}")
    
    # 删除元素
    removed = numbers.pop()
    print(f"After pop(): {numbers}, removed: {removed}")
    
    numbers.remove(99)
    print(f"After remove(99): {numbers}")
    
    # 列表方法
    more_numbers = [6, 7, 8, 9, 10]
    numbers.extend(more_numbers)
    print(f"After extend: {numbers}")
    
    print(f"Count of 3: {numbers.count(3)}")
    print(f"Index of 5: {numbers.index(5)}")
    
    numbers.sort()
    print(f"After sort: {numbers}")
    
    numbers.reverse()
    print(f"After reverse: {numbers}")

def demo_input_output():
    """演示输入输出"""
    print_separator("7. 输入输出")
    
    # 格式化输出
    name = "Alice"
    age = 25
    
    # 多种格式化方式
    print("Hello, %s! You are %d years old." % (name, age))
    print("Hello, {}! You are {} years old.".format(name, age))
    print(f"Hello, {name}! You are {age} years old.")  # f-string (推荐)
    
    # 对齐输出
    items = ["Apple", "Banana", "Orange"]
    prices = [1.99, 0.99, 2.49]
    
    print("\nPrice List:")
    for item, price in zip(items, prices):
        print(f"{item:10s}: ${price:6.2f}")
    
    # 读取用户输入
    print("\nInput examples (commented out to avoid interactive pause):")
    print("# name = input('Enter your name: ')")
    print("# age = int(input('Enter your age: '))")
    print("# print(f'Hello {name}, you are {age} years old!')")

def demo_error_handling():
    """演示错误处理"""
    print_separator("8. 错误处理")
    
    # try-except结构
    try:
        result = 10 / 0
    except ZeroDivisionError as e:
        print(f"Error: {e}")
        result = 0
    
    print(f"Result after error handling: {result}")
    
    # 多个异常
    try:
        value = int("abc")
    except ValueError as e:
        print(f"ValueError: {e}")
    except Exception as e:
        print(f"General Error: {e}")
    else:
        print("No error occurred")
    finally:
        print("This always executes")
    
    # 自定义异常处理
    def divide(a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
    
    try:
        result = divide(10, 0)
    except ValueError as e:
        print(f"Custom error: {e}")

def main():
    """主函数 - 运行所有示例"""
    print("Python基础语法示例 - 专为C++程序员设计")
    print("=" * 60)
    
    demo_variables_and_types()
    demo_operators()
    demo_statements()
    demo_functions()
    demo_strings()
    demo_list_operations()
    demo_input_output()
    demo_error_handling()
    
    print_separator("总结")
    print("C++ vs Python 主要差异:")
    print("✓ 动态类型 - 无需声明变量类型")
    print("✓ 缩进代替大括号 - 代码更简洁")
    print("✓ 无分号 - 减少语法噪音")
    print("✓ 强大的字符串操作 - 特别是切片功能")
    print("✓ 丰富的内置数据类型和函数")
    print("✓ 函数式编程特性 - lambda, map等")
    print("✓ 异常处理更简洁")
    
    print("\n学习建议:")
    print("• 忘掉变量类型声明")
    print("• 拥抱缩进，享受代码的简洁")
    print("• 多使用Python内置功能")
    print("• 练习f-string格式化")
    print("• 掌握切片操作")

if __name__ == "__main__":
    main()