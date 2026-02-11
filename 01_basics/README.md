# 01_basics - Python基础语法

## 概述
这个模块涵盖Python的基础语法，专为有C++背景的程序员设计。

## 文件说明
- `examples.py` - 基础语法示例代码
- `exercises.py` - 练习题
- `README.md` - 本文件

## 学习目标
完成本模块后，你应该能够：
1. 理解Python的变量和数据类型系统
2. 掌握基本运算符和表达式
3. 使用条件语句和循环
4. 定义和调用函数
5. 熟练操作字符串
6. 理解Python的缩进规则

## C++ vs Python 对比

### 变量声明
```cpp
// C++
int age = 25;
string name = "Alice";
double salary = 50000.50;
```

```python
# Python
age = 25
name = "Alice"
salary = 50000.50
```

### 函数定义
```cpp
// C++
int add(int a, int b) {
    return a + b;
}
```

```python
# Python
def add(a, b):
    return a + b
```

### 条件语句
```cpp
// C++
if (x > 0) {
    cout << "Positive" << endl;
} else if (x < 0) {
    cout << "Negative" << endl;
} else {
    cout << "Zero" << endl;
}
```

```python
# Python
if x > 0:
    print("Positive")
elif x < 0:
    print("Negative")
else:
    print("Zero")
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
1-2周

## 下一步
完成本模块后，继续学习 `02_data_structures` 模块。