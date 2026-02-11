#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
05_advanced/examples.py
Python高级特性示例 - 专为C++程序员设计

运行方式:
python examples.py
"""

import os
import re
import threading
import time
import asyncio
import json
import sqlite3
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

def print_separator(title):
    """打印分隔符"""
    print(f"\n{'='*60}")
    print(f" {title}")
    print(f"{'='*60}")

def demo_threading():
    """演示多线程编程"""
    print_separator("1. 多线程编程")
    
    def worker(name, delay):
        """工作线程函数"""
        for i in range(3):
            print(f"{name}: 工作中... {i+1}")
            time.sleep(delay)
        print(f"{name}: 工作完成！")
    
    # 创建并启动多个线程
    print("启动多个线程:")
    threads = []
    
    thread1 = threading.Thread(target=worker, args=("线程1", 0.5))
    thread2 = threading.Thread(target=worker, args=("线程2", 0.3))
    thread3 = threading.Thread(target=worker, args=("线程3", 0.7))
    
    threads.extend([thread1, thread2, thread3])
    
    # 启动线程
    for thread in threads:
        thread.start()
    
    # 等待所有线程完成
    for thread in threads:
        thread.join()
    
    print("所有线程工作完成！")
    
    # 线程安全的计数器
    print("\n线程安全的计数器:")
    class SafeCounter:
        def __init__(self):
            self.count = 0
            self.lock = threading.Lock()
        
        def increment(self):
            with self.lock:
                old_count = self.count
                time.sleep(0.001)  # 模拟处理时间
                self.count = old_count + 1
                return self.count
    
    counter = SafeCounter()
    
    def increment_task():
        for _ in range(100):
            counter.increment()
    
    start_time = time.time()
    threads = []
    for _ in range(10):
        thread = threading.Thread(target=increment_task)
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()
    
    end_time = time.time()
    print(f"最终计数: {counter.count}")
    print(f"耗时: {end_time - start_time:.4f}秒")

def demo_asyncio():
    """演示异步编程"""
    print_separator("2. 异步编程")
    
    async def fetch_data(name, delay):
        """异步获取数据"""
        print(f"开始获取 {name} 的数据...")
        await asyncio.sleep(delay)  # 模拟异步操作
        print(f"{name} 数据获取完成")
        return f"{name}的数据"
    
    async def process_data(data):
        """异步处理数据"""
        print(f"开始处理: {data}")
        await asyncio.sleep(0.5)
        print(f"处理完成: {data}")
        return f"已处理{data}"
    
    async def main():
        """主协程"""
        print("启动多个异步任务:")
        
        # 并发执行多个任务
        tasks = [
            fetch_data("用户信息", 1),
            fetch_data("订单信息", 1.5),
            fetch_data("商品信息", 0.8)
        ]
        
        results = await asyncio.gather(*tasks)
        print(f"所有数据获取完成: {results}")
        
        # 链式异步操作
        print("\n链式异步操作:")
        user_data = await fetch_data("用户", 0.5)
        processed_data = await process_data(user_data)
        print(f"最终结果: {processed_data}")
    
    # 运行异步主函数
    asyncio.run(main())

def demo_file_operations():
    """演示文件操作"""
    print_separator("3. 文件操作")
    
    # 创建测试数据
    test_data = [
        "张三,25,北京,工程师",
        "李四,30,上海,产品经理",
        "王五,28,广州,设计师",
        "赵六,32,深圳,销售"
    ]
    
    # 写入文件
    filename = "test_data.csv"
    print(f"写入文件: {filename}")
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write("姓名,年龄,城市,职业\n")  # CSV头部
        for line in test_data:
            f.write(line + '\n')
    
    print("文件写入完成")
    
    # 读取文件
    print(f"\n读取文件: {filename}")
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
        print("文件内容:")
        print(content)
    
    # 逐行读取并处理
    print("\n逐行处理数据:")
    with open(filename, 'r', encoding='utf-8') as f:
        header = f.readline().strip()  # 读取头部
        print(f"头部: {header}")
        
        people = []
        for line in f:
            if line.strip():  # 跳过空行
                data = line.strip().split(',')
                person = {
                    'name': data[0],
                    'age': int(data[1]),
                    'city': data[2],
                    'job': data[3]
                }
                people.append(person)
                print(f"读取: {person}")
    
    # 使用pathlib进行文件操作
    print("\n使用pathlib:")
    file_path = Path(filename)
    print(f"文件存在: {file_path.exists()}")
    print(f"文件大小: {file_path.stat().st_size} 字节")
    print(f"文件名: {file_path.name}")
    print(f"文件扩展名: {file_path.suffix}")
    
    # 复制文件
    backup_path = Path("backup_" + filename)
    import shutil
    shutil.copy2(file_path, backup_path)
    print(f"文件已复制到: {backup_path}")
    
    # 清理测试文件
    file_path.unlink()
    backup_path.unlink()
    print("测试文件已清理")

def demo_json_operations():
    """演示JSON操作"""
    print_separator("4. JSON操作")
    
    # 创建复杂数据结构
    data = {
        "company": "Python科技",
        "employees": [
            {
                "id": 1,
                "name": "张三",
                "department": "开发部",
                "skills": ["Python", "JavaScript", "SQL"],
                "salary": 15000
            },
            {
                "id": 2,
                "name": "李四",
                "department": "产品部",
                "skills": ["产品设计", "用户研究", "数据分析"],
                "salary": 12000
            }
        ],
        "projects": [
            {
                "name": "网站重构",
                "status": "进行中",
                "team": ["张三"]
            },
            {
                "name": "移动应用",
                "status": "计划中",
                "team": ["李四", "张三"]
            }
        ]
    }
    
    # 写入JSON文件
    filename = "company_data.json"
    print(f"写入JSON文件: {filename}")
    
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print("JSON文件写入完成")
    
    # 读取JSON文件
    print(f"\n读取JSON文件: {filename}")
    with open(filename, 'r', encoding='utf-8') as f:
        loaded_data = json.load(f)
    
    print("公司信息:")
    print(f"公司名称: {loaded_data['company']}")
    print(f"员工数量: {len(loaded_data['employees'])}")
    print(f"项目数量: {len(loaded_data['projects'])}")
    
    # 处理嵌套数据
    print("\n员工详情:")
    for emp in loaded_data['employees']:
        print(f"- {emp['name']} ({emp['department']}): "
              f"{emp['skills'][0] if emp['skills'] else '无技能'}, "
              f"薪资: ¥{emp['salary']}")
    
    # JSON字符串操作
    print("\nJSON字符串操作:")
    json_str = json.dumps(data, ensure_ascii=False, indent=2)
    print("JSON字符串长度:", len(json_str))
    
    # 从字符串解析
    parsed_data = json.loads(json_str)
    print("从字符串解析的公司名称:", parsed_data['company'])
    
    # 清理测试文件
    Path(filename).unlink()
    print("\n测试文件已清理")

def demo_regex():
    """演示正则表达式"""
    print_separator("5. 正则表达式")
    
    # 基本匹配
    text = """
    联系人信息：
    张三 - 电话：138-1234-5678，邮箱：zhangsan@example.com
    李四 - 电话：159-9876-5432，邮箱：lisi@company.org
    王五 - 电话：186-5555-6666，邮箱：wang.wang@test.net
    """
    
    print("原始文本:")
    print(text)
    
    # 匹配电话号码
    phone_pattern = r'(\d{3})-(\d{4})-(\d{4})'
    phones = re.findall(phone_pattern, text)
    print(f"\n找到的电话号码: {phones}")
    
    # 匹配邮箱
    email_pattern = r'[\w\.-]+@[\w\.-]+\.\w+'
    emails = re.findall(email_pattern, text)
    print(f"找到的邮箱: {emails}")
    
    # 提取姓名
    name_pattern = r'([^\s-]+)\s*-\s*电话'
    names = re.findall(name_pattern, text)
    print(f"找到的姓名: {names}")
    
    # 使用编译的正则表达式
    print("\n使用编译的正则表达式:")
    phone_regex = re.compile(phone_pattern)
    email_regex = re.compile(email_pattern)
    
    for match in phone_regex.finditer(text):
        print(f"电话: {match.group()} (区号: {match.group(1)})")
    
    # 替换操作
    print("\n文本替换:")
    # 隐藏电话号码中间4位
    hidden_phone_text = re.sub(phone_pattern, r'\1-****-\3', text)
    print("隐藏手机号后的文本:")
    print(hidden_phone_text)
    
    # 复杂匹配案例
    print("\n复杂匹配案例:")
    code_snippet = '''
    def calculate_tax(price, tax_rate=0.1):
        """
        计算税后价格
        """
        return price * (1 + tax_rate)
    
    class Product:
        def __init__(self, name, price):
            self.name = name
            self.price = price
        
        def get_final_price(self):
            return calculate_tax(self.price)
    '''
    
    # 匹配函数定义
    func_pattern = r'def\s+(\w+)\s*\([^)]*\):'
    functions = re.findall(func_pattern, code_snippet)
    print(f"找到的函数: {functions}")
    
    # 匹配类定义
    class_pattern = r'class\s+(\w+).*?:'
    classes = re.findall(class_pattern, code_snippet)
    print(f"找到的类: {classes}")
    
    # 提取文档字符串
    docstring_pattern = r'"""([^"]+)"""'
    docstrings = re.findall(docstring_pattern, code_snippet)
    print(f"找到的文档字符串: {docstrings}")

def demo_sqlite():
    """演示SQLite数据库操作"""
    print_separator("6. SQLite数据库操作")
    
    # 创建测试数据库
    db_file = "test_database.db"
    print(f"创建数据库: {db_file}")
    
    # 连接数据库
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    
    # 创建表
    print("\n创建员工表:")
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS employees (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER,
            department TEXT,
            salary REAL,
            hire_date TEXT
        )
    ''')
    
    # 插入数据
    employees_data = [
        ('张三', 28, '开发部', 15000.0, '2022-01-15'),
        ('李四', 32, '产品部', 12000.0, '2021-06-20'),
        ('王五', 26, '设计部', 10000.0, '2023-03-10'),
        ('赵六', 35, '市场部', 13000.0, '2020-11-05')
    ]
    
    cursor.executemany(
        'INSERT INTO employees (name, age, department, salary, hire_date) VALUES (?, ?, ?, ?, ?)',
        employees_data
    )
    conn.commit()
    print(f"插入了 {len(employees_data)} 条记录")
    
    # 查询数据
    print("\n查询所有员工:")
    cursor.execute('SELECT * FROM employees')
    all_employees = cursor.fetchall()
    
    for emp in all_employees:
        print(f"ID: {emp[0]}, 姓名: {emp[1]}, 年龄: {emp[2]}, "
              f"部门: {emp[3]}, 薪资: {emp[4]}, 入职: {emp[5]}")
    
    # 条件查询
    print("\n薪资大于12000的员工:")
    cursor.execute('SELECT name, salary FROM employees WHERE salary > 12000')
    high_salary_employees = cursor.fetchall()
    
    for name, salary in high_salary_employees:
        print(f"{name}: ¥{salary}")
    
    # 聚合查询
    cursor.execute('SELECT department, COUNT(*), AVG(salary) FROM employees GROUP BY department')
    dept_stats = cursor.fetchall()
    
    print("\n部门统计:")
    for dept, count, avg_salary in dept_stats:
        print(f"{dept}: {count}人, 平均薪资: ¥{avg_salary:.2f}")
    
    # 更新数据
    print("\n更新数据:")
    cursor.execute('UPDATE employees SET salary = salary * 1.1 WHERE department = "开发部"')
    conn.commit()
    
    cursor.execute('SELECT name, salary FROM employees WHERE department = "开发部"')
    dev_employees = cursor.fetchall()
    
    for name, salary in dev_employees:
        print(f"{name} (开发部): ¥{salary:.2f} (已涨薪10%)")
    
    # 删除数据
    print("\n删除年龄大于33岁的员工:")
    cursor.execute('DELETE FROM employees WHERE age > 33')
    deleted_count = cursor.rowcount
    conn.commit()
    print(f"删除了 {deleted_count} 条记录")
    
    # 关闭连接
    conn.close()
    
    # 清理测试文件
    Path(db_file).unlink()
    print("测试数据库已清理")

def demo_concurrent_futures():
    """演示并发执行"""
    print_separator("7. 并发执行 (ThreadPoolExecutor & ProcessPoolExecutor)")
    
    def cpu_bound_task(n):
        """CPU密集型任务"""
        result = 0
        for i in range(n):
            result += i * i
        return result
    
    def io_bound_task(name, delay):
        """I/O密集型任务"""
        import time
        time.sleep(delay)
        return f"{name} 完成"
    
    # 线程池 (适合I/O密集型任务)
    print("使用ThreadPoolExecutor处理I/O密集型任务:")
    
    io_tasks = [
        ("文件读取", 0.5),
        ("网络请求", 0.8),
        ("数据库查询", 0.3)
    ]
    
    start_time = time.time()
    
    with ThreadPoolExecutor(max_workers=3) as executor:
        futures = [
            executor.submit(io_bound_task, name, delay)
            for name, delay in io_tasks
        ]
        
        for future in futures:
            result = future.result()
            print(f"  {result}")
    
    end_time = time.time()
    print(f"ThreadPoolExecutor耗时: {end_time - start_time:.4f}秒")
    
    # 进程池 (适合CPU密集型任务)
    print("\n使用ProcessPoolExecutor处理CPU密集型任务:")
    
    numbers = [10000, 20000, 15000, 25000]
    
    start_time = time.time()
    
    with ProcessPoolExecutor(max_workers=4) as executor:
        futures = [
            executor.submit(cpu_bound_task, n)
            for n in numbers
        ]
        
        results = [future.result() for future in futures]
    
    end_time = time.time()
    
    for n, result in zip(numbers, results):
        print(f"  计算1到{n}的平方和: {result}")
    
    print(f"ProcessPoolExecutor耗时: {end_time - start_time:.4f}秒")

def demo_performance_testing():
    """演示性能测试"""
    print_separator("8. 性能测试")
    
    import time
    import functools
    
    def timing_decorator(func):
        """计时装饰器"""
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            print(f"{func.__name__} 耗时: {end - start:.6f}秒")
            return result
        return wrapper
    
    # 测试列表生成方式
    @timing_decorator
    def list_comprehension():
        """列表推导式"""
        return [i * i for i in range(100000)]
    
    @timing_decorator
    def for_loop():
        """for循环"""
        result = []
        for i in range(100000):
            result.append(i * i)
        return result
    
    @timing_decorator
    def map_function():
        """map函数"""
        return list(map(lambda x: x * x, range(100000)))
    
    print("比较列表生成方式的性能:")
    
    result1 = list_comprehension()
    result2 = for_loop()
    result3 = map_function()
    
    print(f"结果长度相同: {len(result1) == len(result2) == len(result3) == 100000}")
    
    # 内存使用测试
    print("\n内存使用测试:")
    import sys
    
    small_list = list(range(100))
    large_list = list(range(1000000))
    
    print(f"小列表(100个元素): {sys.getsizeof(small_list)} 字节")
    print(f"大列表(100万个元素): {sys.getsizeof(large_list)} 字节")
    
    # 字符串连接性能
    print("\n字符串连接性能测试:")
    
    @timing_decorator
    def string_concat_plus():
        """使用+连接字符串"""
        result = ""
        for i in range(1000):
            result += str(i)
        return result
    
    @timing_decorator
    def string_concat_join():
        """使用join连接字符串"""
        return "".join(str(i) for i in range(1000))
    
    @timing_decorator
    def string_concat_list():
        """使用列表后join"""
        parts = []
        for i in range(1000):
            parts.append(str(i))
        return "".join(parts)
    
    result1 = string_concat_plus()
    result2 = string_concat_join()
    result3 = string_concat_list()
    
    print(f"结果长度相同: {len(result1) == len(result2) == len(result3)}")

def main():
    """主函数 - 运行所有高级特性示例"""
    print("Python高级特性示例 - 专为C++程序员设计")
    print("=" * 60)
    
    demo_threading()
    demo_asyncio()
    demo_file_operations()
    demo_json_operations()
    demo_regex()
    demo_sqlite()
    demo_concurrent_futures()
    demo_performance_testing()
    
    print_separator("总结")
    print("Python高级特性 vs C++ 主要差异:")
    print("✓ 简化的并发编程 - 无需复杂的线程管理")
    print("✓ 异步编程支持 - asyncio提供强大的异步I/O")
    print("✓ 丰富的文件操作 - pathlib提供现代文件系统接口")
    print("✓ 内置JSON支持 - 轻松处理结构化数据")
    print("✓ 强大的正则表达式 - 内置re模块")
    print("✓ 轻量级数据库 - SQLite集成")
    print("✓ 简化的并发执行 - concurrent.futures")
    print("✓ 内置性能测试工具 - timeit和装饰器")
    
    print("\n学习建议:")
    print("• 理解GIL的影响 - CPU密集型任务用多进程")
    print("• 掌握异步编程 - 适合I/O密集型应用")
    print("• 使用pathlib - 现代化的文件操作方式")
    print("• 学习JSON处理 - Web开发必备技能")
    print("• 练习正则表达式 - 文本处理的利器")
    print("• 了解数据库基础 - 数据驱动应用")

if __name__ == "__main__":
    main()