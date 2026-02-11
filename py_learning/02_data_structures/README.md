# 02_data_structures - Python数据结构

## 概述
这个模块介绍Python的内置数据结构，与C++ STL容器进行对比。

## 文件说明
- `examples.py` - 数据结构示例代码
- `exercises.py` - 练习题
- `README.md` - 本文件

## 学习目标
完成本模块后，你应该能够：
1. 熟练使用列表 (List)
2. 理解元组 (Tuple) 的不可变性
3. 掌握字典 (Dict) 的使用
4. 使用集合 (Set) 进行去重
5. 运用推导式简化代码
6. 理解各数据结构的适用场景

## C++ vs Python 数据结构对比

### 列表 vs Vector
```cpp
// C++ vector
#include <vector>
std::vector<int> numbers = {1, 2, 3, 4, 5};
numbers.push_back(6);
numbers.pop_back();
for (int num : numbers) {
    std::cout << num << " ";
}
```

```python
# Python List
numbers = [1, 2, 3, 4, 5]
numbers.append(6)
numbers.pop()
for num in numbers:
    print(num, end=" ")
```

### 字典 vs Map
```cpp
// C++ map
#include <map>
std::map<std::string, int> scores;
scores["Alice"] = 95;
scores["Bob"] = 87;
```

```python
# Python Dict
scores = {}
scores["Alice"] = 95
scores["Bob"] = 87
# 或者直接创建
scores = {"Alice": 95, "Bob": 87}
```

### Python特有：推导式
```python
# 列表推导式
squares = [x**2 for x in range(1, 11)]

# 字典推导式
word_lengths = {word: len(word) for word in ["hello", "world", "python"]}

# 集合推导式
unique_chars = {char for char in "abracadabra"}
```

## 数据结构选择指南

| 场景 | 推荐结构 | C++对应 |
|------|----------|---------|
| 有序序列，需要频繁修改 | List | vector |
| 固定不变的序列 | Tuple | const array |
| 键值对映射 | Dict | map/unordered_map |
| 去重，集合运算 | Set | set/unordered_set |
| 频繁的队首/队尾操作 | collections.deque | deque |

## 性能特点
- **List**: O(1) 访问，O(n) 插入/删除
- **Dict**: 平均 O(1) 查找、插入、删除
- **Set**: 平均 O(1) 查找、插入、删除
- **Tuple**: 不可变，适合作为字典的键

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
完成本模块后，继续学习 `03_oop` 模块。