#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
02_data_structures/examples.py
Python数据结构示例 - 与C++STL对比

运行方式:
python examples.py
"""

def print_separator(title):
    """打印分隔符"""
    print(f"\n{'='*60}")
    print(f" {title}")
    print(f"{'='*60}")

def demo_lists():
    """演示列表操作"""
    print_separator("1. 列表 (List) - 类似C++ vector")
    
    # 创建列表 - 对比C++ vector<int> numbers = {1, 2, 3};
    numbers = [1, 2, 3, 4, 5]
    mixed = [1, "hello", 3.14, True]  # Python可以混合类型
    
    print(f"Numbers: {numbers}")
    print(f"Mixed: {mixed}")
    
    # 基本操作
    print(f"Length: {len(numbers)}")
    print(f"First element: {numbers[0]}")
    print(f"Last element: {numbers[-1]}")
    print(f"Slice [1:3]: {numbers[1:3]}")
    print(f"Slice [::-1]: {numbers[::-1]}")  # 反转
    
    # 添加元素
    numbers.append(6)      # 尾部添加
    numbers.insert(0, 0)    # 指定位置插入
    print(f"After append and insert: {numbers}")
    
    # 删除元素
    removed = numbers.pop()        # 删除尾部
    numbers.remove(3)               # 删除指定值
    print(f"After pop and remove: {numbers}, removed: {removed}")
    
    # 查找和计数
    print(f"Count of 2: {numbers.count(2)}")
    print(f"Index of 4: {numbers.index(4)}")
    
    # 排序和反转
    numbers.sort()
    print(f"After sort: {numbers}")
    numbers.reverse()
    print(f"After reverse: {numbers}")
    
    # 列表推导式 - Python特色
    squares = [x**2 for x in range(1, 11)]
    even_squares = [x**2 for x in range(1, 11) if x % 2 == 0]
    print(f"Squares: {squares}")
    print(f"Even squares: {even_squares}")

def demo_tuples():
    """演示元组操作"""
    print_separator("2. 元组 (Tuple) - 不可变序列")
    
    # 创建元组
    point = (3, 4)
    single_element = (42,)  # 注意逗号
    empty_tuple = ()
    
    print(f"Point: {point}")
    print(f"Single element: {single_element}")
    print(f"Empty: {empty_tuple}")
    
    # 元组解包 - Python特色功能
    x, y = point
    print(f"Unpacked: x={x}, y={y}")
    
    # 函数返回多值
    def get_position():
        return 10, 20, 30
    
    x, y, z = get_position()
    print(f"Function return: x={x}, y={y}, z={z}")
    
    # 元组作为字典键（因为不可变）
    locations = {
        (0, 0): "Origin",
        (1, 2): "Point A",
        (3, 4): "Point B"
    }
    print(f"Location dict: {locations}")
    
    # 命名元组 - 更清晰
    from collections import namedtuple
    Point = namedtuple('Point', ['x', 'y', 'z'])
    p = Point(1, 2, 3)
    print(f"Named tuple: {p}")
    print(f"Access by name: p.x = {p.x}, p.y = {p.y}")
    
    # 元组不可变性演示
    try:
        point[0] = 5  # 这会报错
    except TypeError as e:
        print(f"Tuple is immutable: {e}")

def demo_dictionaries():
    """演示字典操作"""
    print_separator("3. 字典 (Dict) - 类似C++ map")
    
    # 创建字典 - 对比C++ map<string, int>
    scores = {"Alice": 95, "Bob": 87, "Charlie": 92}
    empty_dict = {}
    
    print(f"Scores: {scores}")
    
    # 基本操作
    print(f"Alice's score: {scores['Alice']}")
    print(f"Keys: {list(scores.keys())}")
    print(f"Values: {list(scores.values())}")
    print(f"Items: {list(scores.items())}")
    
    # 安全访问
    print(f"David's score (default 0): {scores.get('David', 0)}")
    
    # 添加和修改
    scores["David"] = 88  # 添加
    scores["Alice"] = 98  # 修改
    print(f"After updates: {scores}")
    
    # 删除
    removed_score = scores.pop("Bob")
    print(f"Removed Bob's score: {removed_score}")
    print(f"After pop: {scores}")
    
    # 字典推导式 - Python特色
    word_lengths = {word: len(word) for word in ["hello", "world", "python"]}
    print(f"Word lengths: {word_lengths}")
    
    # 嵌套字典
    students = {
        "Alice": {"age": 20, "grade": "A"},
        "Bob": {"age": 19, "grade": "B"}
    }
    print(f"Nested dict: {students}")
    print(f"Alice's age: {students['Alice']['age']}")
    
    # 遍历字典
    print("Iterating over dictionary:")
    for name, score in scores.items():
        print(f"  {name}: {score}")

def demo_sets():
    """演示集合操作"""
    print_separator("4. 集合 (Set) - 去重和集合运算")
    
    # 创建集合
    numbers = {1, 2, 3, 4, 5}
    duplicate_list = [1, 2, 2, 3, 3, 4]
    unique_numbers = set(duplicate_list)
    
    print(f"Set: {numbers}")
    print(f"From list with duplicates: {unique_numbers}")
    
    # 基本操作
    numbers.add(6)
    numbers.discard(1)  # 安全删除，不存在也不报错
    print(f"After add and discard: {numbers}")
    
    # 集合运算 - Python强大功能
    set_a = {1, 2, 3, 4, 5}
    set_b = {4, 5, 6, 7, 8}
    
    print(f"Set A: {set_a}")
    print(f"Set B: {set_b}")
    print(f"Union (A | B): {set_a | set_b}")
    print(f"Intersection (A & B): {set_a & set_b}")
    print(f"Difference (A - B): {set_a - set_b}")
    print(f"Symmetric Difference (A ^ B): {set_a ^ set_b}")
    
    # 成员测试 - 集合的高效操作
    print(f"3 in set_a: {3 in set_a}")
    print(f"10 in set_a: {10 in set_a}")
    
    # 集合推导式
    squares_set = {x**2 for x in range(1, 11)}
    print(f"Squares set: {squares_set}")
    
    # 不可变集合
    frozen = frozenset([1, 2, 3])
    print(f"Frozen set: {frozen}")
    try:
        frozen.add(4)  # 会报错
    except AttributeError as e:
        print(f"Frozen set is immutable: {e}")

def demo_advanced_structures():
    """演示高级数据结构"""
    print_separator("5. 高级数据结构")
    
    # collections.deque - 双端队列
    from collections import deque, defaultdict, Counter
    
    # Deque - 高效的队首队尾操作
    dq = deque([1, 2, 3])
    dq.append(4)      # 右端添加
    dq.appendleft(0) # 左端添加
    dq.pop()          # 右端弹出
    dq.popleft()      # 左端弹出
    
    print(f"Deque operations: {dq}")
    
    # Defaultdict - 带默认值的字典
    d = defaultdict(int)  # 默认值为0
    d['a'] += 1
    d['b'] += 2
    d['c'] += 3
    print(f"Defaultdict: {dict(d)}")
    
    # Counter - 计数器
    words = ["apple", "banana", "apple", "orange", "banana", "apple"]
    word_count = Counter(words)
    print(f"Word count: {word_count}")
    print(f"Most common: {word_count.most_common(2)}")
    
    # 链表实现
    class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next
        
        def __repr__(self):
            return f"ListNode({self.val})"
    
    # 创建链表 1->2->3
    node3 = ListNode(3)
    node2 = ListNode(2, node3)
    node1 = ListNode(1, node2)
    
    print("Linked list:")
    current = node1
    while current:
        print(f"  {current.val}", end=" -> " if current.next else "\n")
        current = current.next

def demo_performance_comparison():
    """演示性能对比"""
    print_separator("6. 性能对比")
    
    import time
    
    # 测试列表 vs 集合的成员查找
    large_list = list(range(100000))
    large_set = set(range(100000))
    target = 99999
    
    # 列表查找 - O(n)
    start = time.time()
    result_list = target in large_list
    list_time = time.time() - start
    
    # 集合查找 - O(1)
    start = time.time()
    result_set = target in large_set
    set_time = time.time() - start
    
    print(f"List search time: {list_time:.6f}s")
    print(f"Set search time: {set_time:.6f}s")
    print(f"Set is {list_time/set_time:.1f}x faster")
    
    # 字典 vs 列表的键值查找
    dict_data = {f"key_{i}": i for i in range(10000)}
    list_data = [(f"key_{i}", i) for i in range(10000)]
    target_key = "key_9999"
    
    # 字典查找
    start = time.time()
    dict_result = dict_data.get(target_key)
    dict_time = time.time() - start
    
    # 列表查找
    start = time.time()
    list_result = None
    for key, value in list_data:
        if key == target_key:
            list_result = value
            break
    list_time = time.time() - start
    
    print(f"Dictionary lookup time: {dict_time:.6f}s")
    print(f"List search time: {list_time:.6f}s")
    print(f"Dictionary is {list_time/dict_time:.1f}x faster")

def demo_real_world_examples():
    """演示实际应用场景"""
    print_separator("7. 实际应用场景")
    
    # 学生成绩管理系统
    students = [
        {"name": "Alice", "scores": {"math": 95, "english": 88, "science": 92}},
        {"name": "Bob", "scores": {"math": 87, "english": 92, "science": 85}},
        {"name": "Charlie", "scores": {"math": 92, "english": 85, "science": 89}}
    ]
    
    # 计算每个学生的平均分
    for student in students:
        scores = student["scores"].values()
        avg = sum(scores) / len(scores)
        student["average"] = avg
    
    # 按平均分排序
    students_sorted = sorted(students, key=lambda x: x["average"], reverse=True)
    
    print("Student rankings:")
    for i, student in enumerate(students_sorted, 1):
        print(f"  {i}. {student['name']}: {student['average']:.1f}")
    
    # 库存管理示例
    inventory = {
        "laptop": {"quantity": 10, "price": 999.99},
        "mouse": {"quantity": 50, "price": 29.99},
        "keyboard": {"quantity": 25, "price": 79.99}
    }
    
    # 计算总价值
    total_value = sum(item["quantity"] * item["price"] for item in inventory.values())
    print(f"\nTotal inventory value: ${total_value:.2f}")
    
    # 找出低库存商品
    low_stock = [product for product, info in inventory.items() if info["quantity"] < 30]
    print(f"Low stock items: {low_stock}")

def main():
    """主函数"""
    print("Python数据结构示例 - 与C++STL对比")
    print("=" * 60)
    
    demo_lists()
    demo_tuples()
    demo_dictionaries()
    demo_sets()
    demo_advanced_structures()
    demo_performance_comparison()
    demo_real_world_examples()
    
    print_separator("总结")
    print("C++ vs Python 数据结构对比:")
    print("✓ List <-> vector: 动态数组，Python更灵活")
    print("✓ Tuple <-> const array: 不可变，Python支持解包")
    print("✓ Dict <-> map/unordered_map: 键值对，Python语法更简洁")
    print("✓ Set <-> set/unordered_set: 去重和集合运算，Python更强大")
    print("✓ Deque <-> deque: 双端队列，性能相似")
    print("✓ Python特色: 推导式、解包、动态类型、丰富内置方法")
    
    print("\n数据结构选择建议:")
    print("• 频繁索引访问: 用列表 (List)")
    print("• 固定数据、作为键: 用元组 (Tuple)")
    print("• 键值映射: 用字典 (Dict)")
    print("• 去重、集合运算: 用集合 (Set)")
    print("• 队首队尾操作: 用deque")
    
    print("\n性能提示:")
    print("• 成员查找: set/dict >> list")
    print("• 插入删除: deque两端 > list头部")
    print("• 内存占用: tuple < list")
    print("• Python数据结构通常比C++STL更易用，但性能略低")

if __name__ == "__main__":
    main()