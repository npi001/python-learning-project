# 03_oop - Python面向对象编程

## 概述
这个模块介绍Python的面向对象编程特性，与C++的OOP进行对比。

## 文件说明
- `examples.py` - OOP示例代码
- `exercises.py` - 练习题
- `README.md` - 本文件

## 学习目标
完成本模块后，你应该能够：
1. 定义和使用Python类
2. 理解Python的继承机制
3. 使用特殊方法 (__init__, __str__等)
4. 应用装饰器和属性
5. 理解Python的私有成员约定
6. 掌握多态和鸭子类型

## C++ vs Python OOP对比

### 类定义
```cpp
// C++ class
class Person {
private:
    std::string name;
    int age;
public:
    Person(std::string name, int age) : name(name), age(age) {}
    void greet() {
        std::cout << "Hello, I'm " << name << std::endl;
    }
};
```

```python
# Python class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        print(f"Hello, I'm {self.name}")
```

### 继承
```cpp
// C++ inheritance
class Student : public Person {
private:
    int student_id;
public:
    Student(std::string name, int age, int id) 
        : Person(name, age), student_id(id) {}
    
    void study() {
        std::cout << "Studying..." << std::endl;
    }
};
```

```python
# Python inheritance
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
    
    def study(self):
        print("Studying...")
```

### 特殊方法 (Magic Methods)
Python的特殊方法让类能够与内置操作符和函数集成：

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"Vector({self.x}, {self.y})"
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __len__(self):
        return int((self.x**2 + self.y**2)**0.5)

v1 = Vector(3, 4)
v2 = Vector(1, 2)
print(v1)           # 调用 __str__
v3 = v1 + v2        # 调用 __add__
print(len(v3))      # 调用 __len__
```

### 属性和装饰器
```python
class Temperature:
    def __init__(self, celsius=0):
        self._celsius = celsius
    
    @property
    def fahrenheit(self):
        return self._celsius * 9/5 + 32
    
    @fahrenheit.setter
    def fahrenheit(self, value):
        self._celsius = (value - 32) * 5/9
    
temp = Temperature(25)
print(temp.fahrenheit)  # 77.0
temp.fahrenheit = 100
print(temp._celsius)    # 37.777...
```

### 私有成员约定
```python
class MyClass:
    def __init__(self):
        self.public_var = "public"
        self._protected_var = "protected"  # 单下划线：约定私有
        self.__private_var = "private"      # 双下划线：名称改写
```

### 鸭子类型
```python
# 不需要明确的接口定义，只要对象有所需方法即可
class Duck:
    def quack(self):
        print("Quack!")

class Person:
    def quack(self):
        print("I'm quacking like a duck!")

def make_sound(duck_like):
    duck_like.quack()

make_sound(Duck())
make_sound(Person())  # 只要对象有quack方法，就能工作
```

## Python OOP特有特性

1. **动态属性**: 运行时添加/删除属性
2. **多重继承**: 支持继承多个类
3. **方法重载**: 通过默认参数实现
4. **类方法和静态方法**: @classmethod 和 @staticmethod
5. **抽象基类**: abc模块

## 运行示例
```bash
python examples.py
```

## 完成练习
```bash
python exercises.py
```

## 预计学习时间
1周

## 下一步
完成本模块后，继续学习 `04_pythonic` 模块，体验Python的独特魅力。