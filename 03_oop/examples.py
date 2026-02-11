#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
03_oop/examples.py
Python面向对象编程示例 - 专为C++程序员设计

运行方式:
python examples.py
"""

def print_separator(title):
    """打印分隔符"""
    print(f"\n{'='*60}")
    print(f" {title}")
    print(f"{'='*60}")

def demo_basic_class():
    """演示基本类定义"""
    print_separator("1. 基本类定义")
    
    class Person:
        """人类 - 基本类定义示例"""
        
        # 类变量 (类似C++的静态成员变量)
        species = "Homo sapiens"
        count = 0
        
        def __init__(self, name, age):
            """构造函数 - Python中叫初始化方法"""
            # 实例变量
            self.name = name
            self.age = age
            
            # 类变量自增
            Person.count += 1
        
        def greet(self):
            """实例方法"""
            return f"Hello, I'm {self.name} and I'm {self.age} years old."
        
        def celebrate_birthday(self):
            """实例方法 - 修改实例状态"""
            self.age += 1
            return f"Happy birthday {self.name}! Now I'm {self.age} years old."
        
        @classmethod
        def get_species(cls):
            """类方法 - 类似C++的静态方法"""
            return cls.species
        
        @classmethod
        def get_population(cls):
            """类方法"""
            return cls.count
        
        @staticmethod
        def is_adult(age):
            """静态方法 - 不依赖实例或类"""
            return age >= 18
    
    # 创建对象实例
    alice = Person("Alice", 25)
    bob = Person("Bob", 17)
    
    print(f"Alice信息: {alice.greet()}")
    print(f"Bob信息: {bob.greet()}")
    
    print(f"Alice过生日: {alice.celebrate_birthday()}")
    
    print(f"物种: {Person.get_species()}")
    print(f"总人数: {Person.get_population()}")
    
    print(f"Alice是成年人吗? {Person.is_adult(alice.age)}")
    print(f"Bob是成年人吗? {Person.is_adult(bob.age)}")
    
    # 访问实例变量
    print(f"Alice的名字: {alice.name}")
    print(f"Alice的年龄: {alice.age}")
    
    return Person, alice, bob

def demo_inheritance():
    """演示继承"""
    print_separator("2. 继承")
    
    class Animal:
        """动物基类"""
        def __init__(self, name):
            self.name = name
        
        def speak(self):
            """基类方法"""
            return f"{self.name} makes a sound"
        
        def move(self):
            """基类方法"""
            return f"{self.name} moves"
    
    class Dog(Animal):
        """狗类 - 继承自动物类"""
        def __init__(self, name, breed):
            # 调用父类构造函数
            super().__init__(name)
            self.breed = breed
        
        def speak(self):
            """重写父类方法"""
            return f"{self.name} barks: Woof!"
        
        def fetch(self):
            """子类特有方法"""
            return f"{self.name} fetches the ball"
    
    class Cat(Animal):
        """猫类 - 继承自动物类"""
        def __init__(self, name, color):
            super().__init__(name)
            self.color = color
        
        def speak(self):
            """重写父类方法"""
            return f"{self.name} meows: Meow!"
        
        def climb(self):
            """子类特有方法"""
            return f"{self.name} climbs the tree"
    
    # 创建实例
    dog = Dog("Buddy", "Golden Retriever")
    cat = Cat("Whiskers", "Orange")
    
    print(f"狗的行为: {dog.speak()}")
    print(f"狗的行为: {dog.move()}")
    print(f"狗的行为: {dog.fetch()}")
    
    print(f"猫的行为: {cat.speak()}")
    print(f"猫的行为: {cat.move()}")
    print(f"猫的行为: {cat.climb()}")
    
    # 检查继承关系
    print(f"Dog是Animal的子类吗? {issubclass(Dog, Animal)}")
    print(f"dog是Animal的实例吗? {isinstance(dog, Animal)}")
    print(f"dog是Dog的实例吗? {isinstance(dog, Dog)}")
    
    return Animal, Dog, Cat

def demo_multiple_inheritance():
    """演示多重继承"""
    print_separator("3. 多重继承")
    
    class Flyable:
        """可飞行的混入类"""
        def fly(self):
            return f"{self.__class__.__name__} flies through the air"
    
    class Swimmable:
        """可游泳的混入类"""
        def swim(self):
            return f"{self.__class__.__name__} swims in the water"
    
    class Duck(Flyable, Swimmable):
        """鸭子类 - 多重继承"""
        def __init__(self, name):
            self.name = name
        
        def quack(self):
            return f"{self.name} quacks: Quack!"
    
    class Fish(Swimmable):
        """鱼类 - 单继承"""
        def __init__(self, name):
            self.name = name
        
        def bubble(self):
            return f"{self.name} makes bubbles"
    
    # 创建实例
    duck = Duck("Donald")
    fish = Fish("Nemo")
    
    print(f"鸭子: {duck.quack()}")
    print(f"鸭子: {duck.fly()}")
    print(f"鸭子: {duck.swim()}")
    
    print(f"鱼: {fish.bubble()}")
    print(f"鱼: {fish.swim()}")
    
    # 方法解析顺序 (MRO)
    print(f"Duck的方法解析顺序: {[cls.__name__ for cls in Duck.__mro__]}")
    
    return Flyable, Swimmable, Duck, Fish

def demo_special_methods():
    """演示特殊方法 (魔术方法)"""
    print_separator("4. 特殊方法 (魔术方法)")
    
    class Vector2D:
        """二维向量类 - 演示特殊方法"""
        
        def __init__(self, x, y):
            self.x = x
            self.y = y
        
        def __str__(self):
            """字符串表示 - 用于print()"""
            return f"Vector2D({self.x}, {self.y})"
        
        def __repr__(self):
            """官方字符串表示 - 用于调试"""
            return f"Vector2D({self.x}, {self.y})"
        
        def __add__(self, other):
            """加法运算符重载"""
            if isinstance(other, Vector2D):
                return Vector2D(self.x + other.x, self.y + other.y)
            else:
                raise TypeError("Unsupported operand type")
        
        def __sub__(self, other):
            """减法运算符重载"""
            if isinstance(other, Vector2D):
                return Vector2D(self.x - other.x, self.y - other.y)
            else:
                raise TypeError("Unsupported operand type")
        
        def __mul__(self, scalar):
            """乘法运算符重载"""
            if isinstance(scalar, (int, float)):
                return Vector2D(self.x * scalar, self.y * scalar)
            else:
                raise TypeError("Unsupported operand type")
        
        def __len__(self):
            """长度运算 - 类似C++的重载length"""
            return int((self.x ** 2 + self.y ** 2) ** 0.5)
        
        def __getitem__(self, index):
            """索引访问 - v[0], v[1]"""
            if index == 0:
                return self.x
            elif index == 1:
                return self.y
            else:
                raise IndexError("Index out of range")
        
        def __setitem__(self, index, value):
            """索引赋值 - v[0] = new_value"""
            if index == 0:
                self.x = value
            elif index == 1:
                self.y = value
            else:
                raise IndexError("Index out of range")
        
        def __eq__(self, other):
            """相等性比较"""
            if isinstance(other, Vector2D):
                return self.x == other.x and self.y == other.y
            return False
        
        def __bool__(self):
            """布尔值转换"""
            return self.x != 0 or self.y != 0
        
        def __call__(self, scalar):
            """使对象可调用"""
            return Vector2D(self.x * scalar, self.y * scalar)
    
    # 使用特殊方法
    v1 = Vector2D(3, 4)
    v2 = Vector2D(1, 2)
    
    print(f"v1: {v1}")
    print(f"v2: {v2}")
    print(f"v1的长度: {len(v1)}")
    
    # 运算符重载
    v3 = v1 + v2
    print(f"v1 + v2 = {v3}")
    
    v4 = v1 - v2
    print(f"v1 - v2 = {v4}")
    
    v5 = v1 * 2
    print(f"v1 * 2 = {v5}")
    
    # 索引访问
    print(f"v1[0] = {v1[0]}, v1[1] = {v1[1]}")
    v1[0] = 10
    print(f"修改后 v1: {v1}")
    
    # 相等性比较
    v6 = Vector2D(3, 4)
    print(f"v1 == v6: {v1 == v6}")
    print(f"v1 == v2: {v1 == v2}")
    
    # 布尔值
    print(f"v1是零向量吗? {bool(v1)}")
    print(f"Vector2D(0, 0)是零向量吗? {bool(Vector2D(0, 0))}")
    
    # 可调用对象
    v7 = v1(3)
    print(f"v1(3) = {v7}")
    
    return Vector2D

def demo_properties():
    """演示属性和装饰器"""
    print_separator("5. 属性和装饰器")
    
    class Temperature:
        """温度类 - 演示属性"""
        
        def __init__(self, celsius=0):
            self._celsius = celsius  # 受保护的变量
        
        @property
        def celsius(self):
            """摄氏度属性 - 只读"""
            return self._celsius
        
        @property
        def fahrenheit(self):
            """华氏度属性 - 只读"""
            return self._celsius * 9/5 + 32
        
        @fahrenheit.setter
        def fahrenheit(self, value):
            """华氏度设置器"""
            self._celsius = (value - 32) * 5/9
        
        @property
        def kelvin(self):
            """开尔文属性 - 只读"""
            return self._celsius + 273.15
        
        @celsius.setter
        def celsius(self, value):
            """摄氏度设置器"""
            if value < -273.15:
                raise ValueError("Temperature below absolute zero is not possible")
            self._celsius = value
        
        def __str__(self):
            return f"Temperature: {self._celsius:.2f}°C"
    
    class BankAccount:
        """银行账户类 - 演示属性和验证"""
        
        def __init__(self, account_number, initial_balance=0):
            self.account_number = account_number
            self._balance = initial_balance
        
        @property
        def balance(self):
            """余额属性"""
            return self._balance
        
        def deposit(self, amount):
            """存款"""
            if amount <= 0:
                raise ValueError("Deposit amount must be positive")
            self._balance += amount
            return self._balance
        
        def withdraw(self, amount):
            """取款"""
            if amount <= 0:
                raise ValueError("Withdrawal amount must be positive")
            if amount > self._balance:
                raise ValueError("Insufficient funds")
            self._balance -= amount
            return self._balance
        
        def __str__(self):
            return f"Account {self.account_number}: Balance ${self._balance:.2f}"
    
    # 使用温度属性
    temp = Temperature(25)
    print(f"温度: {temp}")
    print(f"摄氏度: {temp.celsius}°C")
    print(f"华氏度: {temp.fahrenheit:.2f}°F")
    print(f"开尔文: {temp.kelvin:.2f}K")
    
    # 通过华氏度设置温度
    temp.fahrenheit = 100
    print(f"设置华氏度为100°F后: {temp}")
    
    # 使用银行账户
    account = BankAccount("12345", 1000)
    print(f"{account}")
    
    account.deposit(500)
    print(f"存款500后: {account}")
    
    account.withdraw(200)
    print(f"取款200后: {account}")
    
    return Temperature, BankAccount

def demo_private_members():
    """演示私有成员"""
    print_separator("6. 私有成员")
    
    class Employee:
        """员工类 - 演示私有成员"""
        
        def __init__(self, name, salary):
            self.name = name                    # 公有成员
            self._salary = salary               # 受保护成员 (约定)
            self.__id = "EMP" + str(hash(name)) # 私有成员 (名称改写)
        
        def get_salary(self):
            """获取薪资"""
            return self._salary
        
        def set_salary(self, new_salary):
            """设置薪资"""
            if new_salary > 0:
                self._salary = new_salary
        
        def __get_id(self):
            """私有方法"""
            return self.__id
        
        def get_employee_id(self):
            """公有方法调用私有方法"""
            return self.__get_id()
        
        def __str__(self):
            return f"Employee: {self.name}, Salary: ${self._salary}"
    
    # 创建员工实例
    emp = Employee("Alice", 50000)
    print(emp)
    
    # 访问公有成员
    print(f"员工姓名: {emp.name}")
    
    # 访问受保护成员 (虽然可以访问，但不推荐)
    print(f"员工薪资: {emp._salary}")
    
    # 尝试访问私有成员
    try:
        print(f"员工ID: {emp.__id}")
    except AttributeError as e:
        print(f"直接访问私有成员失败: {e}")
    
    # 通过名称改写访问私有成员
    print(f"员工ID (名称改写): {emp._Employee__id}")
    
    # 通过公有方法访问私有方法
    print(f"员工ID (通过方法): {emp.get_employee_id()}")
    
    # 展示名称改写
    print(f"Employee类的属性: {[attr for attr in dir(emp) if not attr.startswith('__') and not attr.endswith('__')]}")
    
    return Employee

def demo_polymorphism():
    """演示多态"""
    print_separator("7. 多态")
    
    class Shape:
        """形状基类"""
        def area(self):
            """计算面积 - 抽象方法"""
            raise NotImplementedError("Subclasses must implement area method")
        
        def perimeter(self):
            """计算周长 - 抽象方法"""
            raise NotImplementedError("Subclasses must implement perimeter method")
        
        def __str__(self):
            return f"{self.__class__.__name__}"
    
    class Rectangle(Shape):
        """矩形类"""
        def __init__(self, width, height):
            self.width = width
            self.height = height
        
        def area(self):
            return self.width * self.height
        
        def perimeter(self):
            return 2 * (self.width + self.height)
    
    class Circle(Shape):
        """圆形类"""
        def __init__(self, radius):
            self.radius = radius
        
        def area(self):
            import math
            return math.pi * self.radius ** 2
        
        def perimeter(self):
            import math
            return 2 * math.pi * self.radius
    
    class Triangle(Shape):
        """三角形类"""
        def __init__(self, base, height, side1, side2, side3):
            self.base = base
            self.height = height
            self.side1 = side1
            self.side2 = side2
            self.side3 = side3
        
        def area(self):
            return 0.5 * self.base * self.height
        
        def perimeter(self):
            return self.side1 + self.side2 + self.side3
    
    # 创建不同形状的对象
    shapes = [
        Rectangle(4, 5),
        Circle(3),
        Triangle(6, 4, 5, 5, 6)
    ]
    
    # 多态：同一接口，不同实现
    print("形状信息:")
    for shape in shapes:
        print(f"{shape}:")
        print(f"  面积: {shape.area():.2f}")
        print(f"  周长: {shape.perimeter():.2f}")
        print()
    
    # 鸭子类型 (Duck Typing)
    class Duck:
        def quack(self):
            return "Quack!"
        
        def fly(self):
            return "Duck flies"
    
    class Person:
        def quack(self):
            return "I'm quacking like a duck!"
        
        def fly(self):
            return "Person pretends to fly"
    
    def make_it_quack_and_fly(duck_like_object):
        """不检查类型，只要有quack和fly方法就行"""
        print(f"{duck_like_object.__class__.__name__}:")
        print(f"  {duck_like_object.quack()}")
        print(f"  {duck_like_object.fly()}")
        print()
    
    # 鸭子类型示例
    duck = Duck()
    person = Person()
    
    print("鸭子类型示例:")
    make_it_quack_and_fly(duck)
    make_it_quack_and_fly(person)
    
    return Shape, Rectangle, Circle, Triangle

def demo_dynamic_attributes():
    """演示动态属性"""
    print_separator("8. 动态属性")
    
    class DynamicPerson:
        """动态人员类"""
        
        def __init__(self, name):
            self.name = name
        
        def add_attribute(self, attr_name, attr_value):
            """动态添加属性"""
            setattr(self, attr_name, attr_value)
        
        def remove_attribute(self, attr_name):
            """动态删除属性"""
            if hasattr(self, attr_name):
                delattr(self, attr_name)
        
        def get_all_attributes(self):
            """获取所有属性"""
            return {key: value for key, value in self.__dict__.items() 
                   if not key.startswith('_')}
    
    # 创建动态对象
    person = DynamicPerson("Alice")
    print(f"初始属性: {person.get_all_attributes()}")
    
    # 动态添加属性
    person.add_attribute("age", 25)
    person.add_attribute("city", "Beijing")
    person.add_attribute("email", "alice@example.com")
    
    print(f"添加属性后: {person.get_all_attributes()}")
    
    # 直接动态添加属性
    person.job = "Engineer"
    person.hobby = "Reading"
    
    print(f"直接添加属性后: {person.get_all_attributes()}")
    
    # 访问动态属性
    print(f"年龄: {person.age}")
    print(f"工作: {person.job}")
    
    # 修改动态属性
    person.age = 26
    print(f"修改后年龄: {person.age}")
    
    # 删除动态属性
    person.remove_attribute("city")
    print(f"删除city属性后: {person.get_all_attributes()}")
    
    # 动态方法
    def new_method(self):
        return f"Hello, I'm {self.name} and I'm {self.age} years old!"
    
    # 动态添加方法
    import types
    person.introduce = types.MethodType(new_method, person)
    print(f"动态介绍: {person.introduce()}")
    
    return DynamicPerson

def main():
    """主函数 - 运行所有OOP示例"""
    print("Python面向对象编程示例 - 专为C++程序员设计")
    print("=" * 60)
    
    demo_basic_class()
    demo_inheritance()
    demo_multiple_inheritance()
    demo_special_methods()
    demo_properties()
    demo_private_members()
    demo_polymorphism()
    demo_dynamic_attributes()
    
    print_separator("总结")
    print("Python OOP vs C++ 主要差异:")
    print("✓ 无需头文件分离 - 类定义在一个地方")
    print("✓ 动态类型 - 属性可在运行时添加/删除")
    print("✓ __特殊方法__ - 与Python语言特性集成")
    print("✓ 属性装饰器 - 简化getter/setter")
    print("✓ 多重继承 - 支持继承多个类")
    print("✓ 鸭子类型 - 不依赖显式接口定义")
    print("✓ 更简洁的语法 - 减少样板代码")
    
    print("\n学习建议:")
    print("• 拥抱动态特性 - 不要尝试复制C++的静态类型思维")
    print("• 学习特殊方法 - 让你的类更好地与Python集成")
    print("• 使用属性装饰器 - 替代传统的getter/setter")
    print("• 理解MRO - 掌握多重继承的方法解析顺序")
    print("• 练习鸭子类型 - 关注行为而不是类型")

if __name__ == "__main__":
    main()