# 05_advanced - Python高级特性

## 概述
这个模块介绍Python的高级特性，包括并发编程、文件操作、正则表达式、包管理等。

## 文件说明
- `examples.py` - 高级特性示例
- `exercises.py` - 练习题
- `README.md` - 本文件

## 学习目标
完成本模块后，你应该能够：
1. 理解Python的并发编程模型
2. 掌握文件和目录操作
3. 使用正则表达式处理文本
4. 管理虚拟环境和包依赖
5. 进行调试和性能分析
6. 编写和运行测试

## 1. 并发编程

### 多线程 (Threading)
```python
import threading
import time

def worker(name):
    for i in range(5):
        print(f"{name}: {i}")
        time.sleep(0.1)

threads = []
for i in range(3):
    t = threading.Thread(target=worker, args=(f"Thread-{i}",))
    threads.append(t)
    t.start()

for t in threads:
    t.join()
```

### 异步编程 (asyncio)
```python
import asyncio
import time

async def fetch_data(name, delay):
    print(f"{name}: 开始获取数据")
    await asyncio.sleep(delay)
    print(f"{name}: 数据获取完成")
    return f"{name}的数据"

async def main():
    tasks = [
        fetch_data("API-1", 1),
        fetch_data("API-2", 2),
        fetch_data("API-3", 1.5),
    ]
    results = await asyncio.gather(*tasks)
    for result in results:
        print(result)

asyncio.run(main())
```

### GIL (全局解释器锁)
Python的GIL限制同一时间只有一个线程执行Python字节码：
- **CPU密集型任务**: 用多进程 (multiprocessing)
- **I/O密集型任务**: 用多线程或异步编程

## 2. 文件操作

### 基本文件操作
```python
# 读取文件
with open("data.txt", "r", encoding="utf-8") as f:
    content = f.read()        # 全部内容
    lines = f.readlines()     # 所有行
    f.seek(0)                # 重置指针
    line = f.readline()       # 读取一行

# 写入文件
with open("output.txt", "w", encoding="utf-8") as f:
    f.write("Hello, World!\n")
    f.writelines(["Line 1\n", "Line 2\n"])

# 追加模式
with open("log.txt", "a", encoding="utf-8") as f:
    f.write(f"Log entry: {time.ctime()}\n")
```

### 目录操作
```python
import os
import shutil
from pathlib import Path

# pathlib推荐方式
path = Path("/home/user/documents")
print(path.exists())        # 目录是否存在
print(path.is_dir())        # 是否为目录
print(path.name)           # 目录名

# 创建目录
path.mkdir(parents=True, exist_ok=True)

# 遍历目录
for item in path.rglob("*"):  # 递归遍历
    if item.is_file():
        print(f"File: {item}")
    elif item.is_dir():
        print(f"Dir:  {item}")

# 复制/移动/删除
shutil.copy("source.txt", "backup.txt")
shutil.move("old.txt", "new.txt")
os.remove("temp.txt")
```

## 3. 正则表达式

### 基础匹配
```python
import re

text = "联系方式：电话 138-1234-5678，邮箱 example@email.com"

# 查找所有匹配
phone_pattern = r'\d{3}-\d{4}-\d{4}'
phones = re.findall(phone_pattern, text)
print(phones)  # ['138-1234-5678']

# 编译正则表达式（性能更好）
email_pattern = re.compile(r'\w+@\w+\.\w+')
emails = email_pattern.findall(text)
print(emails)  # ['example@email.com']
```

### 高级匹配
```python
import re

# 分组捕获
pattern = r'(\d{4})-(\d{2})-(\d{2})'
date = "2023-12-25"
match = re.match(pattern, date)
if match:
    year, month, day = match.groups()
    print(f"Year: {year}, Month: {month}, Day: {day}")

# 替换
text = "价格：$100，折扣：$20"
new_text = re.sub(r'\$(\d+)', r'¥\1', text)
print(new_text)  # 价格：¥100，折扣：¥20

# 分割
data = "name,age,city;name2,age2,city2"
records = re.split(r'[;,]', data)
print(records)  # ['name', 'age', 'city', 'name2', 'age2', 'city2']
```

## 4. 虚拟环境和包管理

### 虚拟环境
```bash
# 创建虚拟环境
python -m venv myenv

# 激活虚拟环境
# Windows
myenv\Scripts\activate
# Linux/Mac
source myenv/bin/activate

# 安装包
pip install numpy pandas requests

# 导出依赖
pip freeze > requirements.txt

# 安装依赖
pip install -r requirements.txt

# 退出虚拟环境
deactivate
```

### requirements.txt
```txt
numpy>=1.21.0
pandas==1.3.0
requests>=2.25.0,<3.0.0
matplotlib>=3.3.0
```

## 5. 调试和测试

### 调试技巧
```python
import pdb

def complex_function(data):
    processed = []
    for item in data:
        # 设置断点
        pdb.set_trace()
        result = item * 2
        processed.append(result)
    return processed

# 更现代的方式：使用breakpoint()
def debug_function(x, y):
    breakpoint()  # Python 3.7+
    result = x + y
    return result
```

### 单元测试
```python
import unittest

class Calculator:
    def add(self, a, b):
        return a + b
    
    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()
    
    def test_add(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
    
    def test_divide(self):
        self.assertEqual(self.calc.divide(6, 2), 3)
        self.assertRaises(ValueError, self.calc.divide, 5, 0)

if __name__ == "__main__":
    unittest.main()
```

### 性能分析
```python
import time
import cProfile

def slow_function():
    total = 0
    for i in range(1000000):
        total += i * i
    return total

# 简单计时
start = time.time()
result = slow_function()
end = time.time()
print(f"Time: {end - start:.4f}s")

# 详细性能分析
cProfile.run('slow_function()', 'profile_output')
```

## 6. 常用标准库

### collections模块
```python
from collections import Counter, defaultdict, deque

# Counter - 计数
words = ["apple", "banana", "apple", "orange", "banana", "apple"]
word_count = Counter(words)
print(word_count)  # Counter({'apple': 3, 'banana': 2, 'orange': 1})

# defaultdict - 默认值字典
d = defaultdict(int)
d['missing_key'] += 1  # 不会报错

# deque - 双端队列
dq = deque([1, 2, 3])
dq.append(4)      # 右端添加
dq.appendleft(0)  # 左端添加
dq.pop()          # 右端弹出
dq.popleft()      # 左端弹出
```

### itertools模块
```python
import itertools

# 无限迭代器
counter = itertools.count(1, 2)  # 1, 3, 5, 7, ...

# 组合
items = ['a', 'b', 'c']
combinations = itertools.combinations(items, 2)  # ab, ac, bc
permutations = itertools.permutations(items, 2)   # ab, ba, ac, ca, bc, cb

# 分组
data = [('a', 1), ('b', 2), ('a', 3), ('b', 4)]
for key, group in itertools.groupby(data, lambda x: x[0]):
    print(f"{key}: {list(group)}")
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
完成本模块后，进入 `06_projects` 实践项目，将所学知识应用到实际开发中。