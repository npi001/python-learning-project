# tests - 测试文件

## 概述
这个目录包含所有学习模块的测试文件，帮助你验证代码正确性和巩固所学知识。

## 目录结构
```
tests/
├── __init__.py              # 测试包初始化
├── conftest.py              # pytest配置文件
├── test_01_basics.py        # 基础语法测试
├── test_02_data_structures.py  # 数据结构测试
├── test_03_oop.py           # 面向对象编程测试
├── test_04_pythonic.py      # Python特色功能测试
├── test_05_advanced.py      # 高级特性测试
├── integration_tests.py      # 集成测试
├── performance_tests.py     # 性能测试
└── utils/                   # 测试工具
    ├── __init__.py
    ├── test_helpers.py      # 测试辅助函数
    └── fixtures.py          # 测试数据
```

## 运行测试

### 运行所有测试
```bash
# 使用pytest
pytest tests/ -v

# 使用unittest
python -m unittest discover tests -v
```

### 运行特定测试
```bash
# 运行单个测试文件
pytest tests/test_01_basics.py -v

# 运行特定测试函数
pytest tests/test_01_basics.py::test_variable_declaration -v

# 运行特定模块的所有测试
pytest tests/ -k "basics" -v
```

### 测试覆盖率
```bash
# 安装coverage
pip install coverage

# 运行覆盖率测试
coverage run -m pytest tests/
coverage report
coverage html  # 生成HTML报告
```

## 测试文件说明

### test_01_basics.py
测试基础语法概念：
- 变量和数据类型
- 运算符和表达式
- 条件语句和循环
- 函数定义和调用
- 字符串操作

### test_02_data_structures.py
测试数据结构操作：
- 列表操作和方法
- 元组创建和使用
- 字典键值对操作
- 集合运算和方法
- 推导式语法

### test_03_oop.py
测试面向对象编程：
- 类和对象创建
- 继承和多态
- 特殊方法使用
- 属性和装饰器
- 私有成员约定

### test_04_pythonic.py
测试Python特色功能：
- 各种推导式
- 生成器和迭代器
- 装饰器应用
- 上下文管理器
- 异常处理

### test_05_advanced.py
测试高级特性：
- 并发编程
- 文件操作
- 正则表达式
- 虚拟环境相关
- 调试和性能

### integration_tests.py
集成测试：
- 跨模块功能测试
- 端到端测试
- 实际场景模拟

### performance_tests.py
性能测试：
- 算法效率比较
- 内存使用测试
- 并发性能测试

## 编写测试的原则

### 1. 测试命名规范
```python
def test_function_name_should_return_expected_result():
    # 测试函数应该做什么
    pass

def test_class_method_should_handle_edge_cases():
    # 测试边界情况
    pass

def test_should_raise_error_for_invalid_input():
    # 测试异常情况
    pass
```

### 2. 测试结构 (AAA模式)
```python
def test_user_creation():
    # Arrange (准备)
    user_data = {"name": "Alice", "age": 25}
    
    # Act (执行)
    user = User(**user_data)
    
    # Assert (断言)
    assert user.name == "Alice"
    assert user.age == 25
```

### 3. 测试数据管理
```python
# 使用pytest fixture
@pytest.fixture
def sample_user():
    return User(name="Bob", age=30)

def test_user_age(sample_user):
    assert sample_user.age == 30
```

## 常用断言

### 基本断言
```python
assert x == y          # 相等
assert x != y          # 不相等
assert x < y           # 小于
assert x in y          # 包含
assert x not in y      # 不包含
assert isinstance(x, type)  # 类型检查
assert callable(x)      # 可调用对象
```

### 异常断言
```python
import pytest

def test_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        result = 10 / 0

def test_value_error():
    with pytest.raises(ValueError, match="Invalid input"):
        process_data("invalid")
```

### 警告断言
```python
import warnings

def test_deprecation_warning():
    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter("always")
        deprecated_function()
        assert len(w) == 1
        assert issubclass(w[0].category, DeprecationWarning)
```

## 测试数据管理

### 使用fixtures
```python
# conftest.py
@pytest.fixture
def sample_data():
    return {
        "users": [
            {"name": "Alice", "age": 25},
            {"name": "Bob", "age": 30}
        ],
        "products": [
            {"id": 1, "name": "Laptop", "price": 999.99},
            {"id": 2, "name": "Phone", "price": 699.99}
        ]
    }

@pytest.fixture
def temp_file(tmp_path):
    """创建临时文件"""
    file_path = tmp_path / "test.txt"
    file_path.write_text("test content")
    return file_path
```

### 参数化测试
```python
@pytest.mark.parametrize("input,expected", [
    (2, 4),
    (3, 9),
    (4, 16),
    (5, 25)
])
def test_square(input, expected):
    assert square(input) == expected

@pytest.mark.parametrize("name,age", [
    ("Alice", 25),
    ("Bob", 30),
    ("Charlie", 35)
])
def test_user_creation(name, age):
    user = User(name, age)
    assert user.name == name
    assert user.age == age
```

## 模拟和打桩

### 使用unittest.mock
```python
from unittest.mock import Mock, patch

def test_external_api_call():
    # 模拟外部API调用
    mock_api = Mock()
    mock_api.get.return_value = {"status": "success", "data": [1, 2, 3]}
    
    result = process_api_data(mock_api)
    assert result == [1, 2, 3]
    mock_api.get.assert_called_once()

def test_file_operations():
    with patch("builtins.open", mock_open(read_data="test content")):
        result = read_file("test.txt")
        assert result == "test content"
```

## 性能测试

### 基准测试
```python
import time

def test_performance():
    start_time = time.time()
    result = expensive_operation()
    end_time = time.time()
    
    assert result is not None
    assert end_time - start_time < 1.0  # 应该在1秒内完成

# 使用pytest-benchmark
def test_list_comprehension_vs_loop(benchmark):
    data = list(range(10000))
    
    def comprehension():
        return [x * 2 for x in data]
    
    def loop():
        result = []
        for x in data:
            result.append(x * 2)
        return result
    
    comp_time = benchmark(comprehension)
    loop_time = benchmark(loop)
    
    assert comp_time < loop_time  # 推导式应该更快
```

## 持续集成

### GitHub Actions配置
```yaml
# .github/workflows/tests.yml
name: Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: [3.8, 3.9, "3.10", "3.11"]

    steps:
    - uses: actions/checkout@v2
    - name: Set up Python ${{ matrix.python-version }}
      uses: actions/setup-python@v2
      with:
        python-version: ${{ matrix.python-version }}
    
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install pytest pytest-cov
    
    - name: Run tests
      run: |
        pytest tests/ --cov=. --cov-report=xml
    
    - name: Upload coverage
      uses: codecov/codecov-action@v1
```

## 最佳实践

1. **保持测试简单**: 每个测试只验证一个功能点
2. **使用描述性名称**: 测试名称应该清楚说明测试内容
3. **测试边界条件**: 不仅测试正常情况，还要测试边界和异常
4. **保持测试独立**: 测试之间不应该相互依赖
5. **定期运行测试**: 建立CI/CD流水线自动运行测试
6. **维护测试代码**: 测试代码也需要重构和优化

## 运行建议

1. **学习阶段**: 运行对应模块的测试来验证理解
2. **练习阶段**: 先写代码，再运行测试检查
3. **项目阶段**: 使用TDD方式，先写测试再写实现
4. **复习阶段**: 运行所有测试巩固知识

测试不仅是验证工具，也是学习的重要组成部分！