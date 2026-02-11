#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
02_data_structures/exercises.py
Python数据结构练习题

运行方式:
python exercises.py

完成后运行:
python check_exercises.py  # 检查答案
"""

def print_exercise_title(title):
    """打印练习题标题"""
    print(f"\n{'='*50}")
    print(f" 练习: {title}")
    print(f"{'='*50}")

def exercise_1_lists():
    """练习1: 列表操作"""
    print_exercise_title("列表操作")
    
    print("任务:")
    print("1. 创建包含1-20的列表")
    print("2. 筛选出所有偶数")
    print("3. 计算偶数的平方")
    print("4. 找出最大的三个数")
    
    # 在这里写你的代码:
    numbers = list(range(1, 21))
    even_numbers = [num for num in numbers if num % 2 == 0]
    even_squares = [num ** 2 for num in even_numbers]
    top_three = sorted(numbers, reverse=True)[:3]
    
    print(f"\n你的代码:")
    print(f"1-20: {numbers}")
    print(f"偶数: {even_numbers}")
    print(f"偶数平方: {even_squares}")
    print(f"最大的三个数: {top_three}")
    
    return numbers, even_numbers, even_squares, top_three

def exercise_2_tuples():
    """练习2: 元组操作"""
    print_exercise_title("元组操作")
    
    print("任务:")
    print("1. 创建包含学生信息的元组")
    print("2. 使用元组解包提取信息")
    print("3. 创建学生元组列表")
    print("4. 按年龄排序学生")
    
    # 在这里写你的代码:
    student = ("Alice", 20, "Computer Science")
    name, age, major = student
    
    students = [
        ("Bob", 19, "Mathematics"),
        ("Charlie", 21, "Physics"),
        ("David", 20, "Chemistry"),
        ("Eve", 22, "Biology")
    ]
    
    # 按年龄排序
    students_sorted = sorted(students, key=lambda x: x[1])
    
    print(f"\n你的代码:")
    print(f"单个学生: {student}")
    print(f"解包: name={name}, age={age}, major={major}")
    print(f"所有学生: {students}")
    print(f"按年龄排序: {students_sorted}")
    
    return student, students_sorted

def exercise_3_dictionaries():
    """练习3: 字典操作"""
    print_exercise_title("字典操作")
    
    print("任务:")
    print("1. 创建学生成绩字典")
    print("2. 计算每个学生的平均分")
    print("3. 找出最高分学生")
    print("4. 按平均分排序")
    
    # 在这里写你的代码:
    students = {
        "Alice": {"math": 95, "english": 88, "science": 92},
        "Bob": {"math": 87, "english": 92, "science": 85},
        "Charlie": {"math": 92, "english": 85, "science": 89},
        "David": {"math": 78, "english": 95, "science": 91}
    }
    
    # 计算平均分
    for name, scores in students.items():
        avg = sum(scores.values()) / len(scores)
        scores["average"] = avg
    
    # 找出最高分学生
    top_student = max(students.items(), key=lambda x: x[1]["average"])
    
    # 按平均分排序
    students_ranked = sorted(students.items(), key=lambda x: x[1]["average"], reverse=True)
    
    print(f"\n你的代码:")
    print(f"带平均分的学生成绩: {students}")
    print(f"最高分学生: {top_student[0]} (平均分: {top_student[1]['average']:.1f})")
    print(f"排名:")
    for i, (name, scores) in enumerate(students_ranked, 1):
        print(f"  {i}. {name}: {scores['average']:.1f}")
    
    return students, top_student, students_ranked

def exercise_4_sets():
    """练习4: 集合操作"""
    print_exercise_title("集合操作")
    
    print("任务:")
    print("1. 创建两个课程集合")
    print("2. 找出同时选两门课的学生")
    print("3. 找出只选一门课的学生")
    print("4. 统计所有选课学生")
    
    # 在这里写你的代码:
    math_students = {"Alice", "Bob", "Charlie", "David", "Eve"}
    physics_students = {"Charlie", "David", "Frank", "Grace", "Eve"}
    
    # 同时选两门课的学生（交集）
    both_courses = math_students & physics_students
    
    # 只选一门课的学生（对称差集）
    only_one_course = math_students ^ physics_students
    
    # 所有选课学生（并集）
    all_students = math_students | physics_students
    
    print(f"\n你的代码:")
    print(f"数学课学生: {math_students}")
    print(f"物理课学生: {physics_students}")
    print(f"同时选两门课: {both_courses}")
    print(f"只选一门课: {only_one_course}")
    print(f"所有选课学生: {all_students}")
    print(f"选课总人数: {len(all_students)}")
    
    return math_students, physics_students, both_courses, all_students

def exercise_5_comprehensions():
    """练习5: 推导式"""
    print_exercise_title("推导式练习")
    
    print("任务:")
    print("1. 使用列表推导式创建1-50的平方数列表")
    print("2. 使用字典推导式创建单词长度字典")
    print("3. 使用集合推导式创建字符串唯一字符集合")
    print("4. 使用嵌套推导式创建乘法表")
    
    # 在这里写你的代码:
    # 1-50的平方数
    squares = [x**2 for x in range(1, 51)]
    
    # 单词长度字典
    words = ["python", "programming", "data", "structures", "algorithm"]
    word_lengths = {word: len(word) for word in words}
    
    # 字符串唯一字符
    text = "hello world python programming"
    unique_chars = {char for char in text if char.isalpha()}
    
    # 乘法表 (嵌套列表推导式)
    multiplication_table = [[i*j for j in range(1, 11)] for i in range(1, 11)]
    
    print(f"\n你的代码:")
    print(f"1-50平方数前10个: {squares[:10]}...")
    print(f"单词长度: {word_lengths}")
    print(f"唯一字符: {sorted(unique_chars)}")
    print(f"乘法表前3行:")
    for row in multiplication_table[:3]:
        print(f"  {row}")
    
    return squares, word_lengths, unique_chars, multiplication_table

def exercise_6_data_analysis():
    """练习6: 数据分析"""
    print_exercise_title("数据分析")
    
    print("任务:")
    print("1. 分析销售数据")
    print("2. 计算各产品总销量")
    print("3. 找出最畅销产品")
    print("4. 生成销售报告")
    
    # 在这里写你的代码:
    sales_data = [
        {"date": "2023-01-01", "product": "laptop", "quantity": 5, "price": 999.99},
        {"date": "2023-01-01", "product": "mouse", "quantity": 10, "price": 29.99},
        {"date": "2023-01-02", "product": "laptop", "quantity": 3, "price": 999.99},
        {"date": "2023-01-02", "product": "keyboard", "quantity": 8, "price": 79.99},
        {"date": "2023-01-03", "product": "mouse", "quantity": 15, "price": 29.99},
        {"date": "2023-01-03", "product": "laptop", "quantity": 2, "price": 999.99},
        {"date": "2023-01-03", "product": "keyboard", "quantity": 6, "price": 79.99}
    ]
    
    # 计算各产品总销量和总收入
    product_stats = {}
    for sale in sales_data:
        product = sale["product"]
        if product not in product_stats:
            product_stats[product] = {
                "total_quantity": 0,
                "total_revenue": 0,
                "avg_price": 0
            }
        
        product_stats[product]["total_quantity"] += sale["quantity"]
        product_stats[product]["total_revenue"] += sale["quantity"] * sale["price"]
    
    # 计算平均价格
    for product, stats in product_stats.items():
        stats["avg_price"] = stats["total_revenue"] / stats["total_quantity"]
    
    # 找出最畅销产品（按销量）
    best_seller = max(product_stats.items(), key=lambda x: x[1]["total_quantity"])
    
    # 找出收入最高产品
    highest_revenue = max(product_stats.items(), key=lambda x: x[1]["total_revenue"])
    
    print(f"\n你的代码 - 销售分析报告:")
    print(f"{'产品':<10}{'总销量':<10}{'总收入':<15}{'平均价格':<10}")
    print("-" * 50)
    for product, stats in product_stats.items():
        print(f"{product:<10}{stats['total_quantity']:<10}"
              f"${stats['total_revenue']:<14.2f}${stats['avg_price']:<9.2f}")
    
    print(f"\n最畅销产品: {best_seller[0]} (销量: {best_seller[1]['total_quantity']})")
    print(f"收入最高产品: {highest_revenue[0]} (收入: ${highest_revenue[1]['total_revenue']:.2f})")
    
    return product_stats, best_seller, highest_revenue

def exercise_7_algorithm_implementation():
    """练习7: 算法实现"""
    print_exercise_title("算法实现")
    
    print("任务:")
    print("1. 实现二分查找")
    print("2. 实现冒泡排序")
    print("3. 实现栈数据结构")
    print("4. 实现队列数据结构")
    
    # 在这里写你的代码:
    def binary_search(arr, target):
        """二分查找"""
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
    
    def bubble_sort(arr):
        """冒泡排序"""
        n = len(arr)
        for i in range(n):
            for j in range(0, n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr
    
    # 栈实现
    class Stack:
        def __init__(self):
            self.items = []
        
        def push(self, item):
            self.items.append(item)
        
        def pop(self):
            if not self.is_empty():
                return self.items.pop()
            return None
        
        def is_empty(self):
            return len(self.items) == 0
        
        def size(self):
            return len(self.items)
    
    # 队列实现
    from collections import deque
    
    class Queue:
        def __init__(self):
            self.items = deque()
        
        def enqueue(self, item):
            self.items.append(item)
        
        def dequeue(self):
            if not self.is_empty():
                return self.items.popleft()
            return None
        
        def is_empty(self):
            return len(self.items) == 0
        
        def size(self):
            return len(self.items)
    
    # 测试
    test_array = [64, 34, 25, 12, 22, 11, 90]
    sorted_array = bubble_sort(test_array.copy())
    search_result = binary_search(sorted_array, 25)
    
    # 测试栈
    stack = Stack()
    for i in range(5):
        stack.push(i)
    
    popped_items = []
    while not stack.is_empty():
        popped_items.append(stack.pop())
    
    # 测试队列
    queue = Queue()
    for i in range(5):
        queue.enqueue(i)
    
    dequeued_items = []
    while not queue.is_empty():
        dequeued_items.append(queue.dequeue())
    
    print(f"\n你的代码 - 算法测试:")
    print(f"原数组: {test_array}")
    print(f"排序后: {sorted_array}")
    print(f"查找25的结果: 索引 {search_result}")
    print(f"栈操作 (LIFO): {popped_items}")
    print(f"队列操作 (FIFO): {dequeued_items}")
    
    return {
        "binary_search": binary_search,
        "bubble_sort": bubble_sort,
        "stack": stack,
        "queue": queue
    }

def check_answers():
    """检查练习答案"""
    print("\n" + "="*50)
    print(" 检查练习完成情况")
    print("="*50)
    
    try:
        # 执行所有练习
        results = []
        
        print("执行练习1...")
        result1 = exercise_1_lists()
        results.append(("练习1", len(result1[1]) == 10 and result1[1][0] == 2))
        
        print("执行练习2...")
        result2 = exercise_2_tuples()
        results.append(("练习2", len(result2[1]) == 4 and result2[1][0][0] == "Bob"))
        
        print("执行练习3...")
        result3 = exercise_3_dictionaries()
        results.append(("练习3", len(result3[0]) == 4 and result3[1][0] in result3[0]))
        
        print("执行练习4...")
        result4 = exercise_4_sets()
        results.append(("练习4", len(result4[3]) == 7))
        
        print("执行练习5...")
        result5 = exercise_5_comprehensions()
        results.append(("练习5", len(result5[0]) == 50 and len(result5[1]) == 5))
        
        print("执行练习6...")
        result6 = exercise_6_data_analysis()
        results.append(("练习6", len(result6[0]) == 3))
        
        print("执行练习7...")
        result7 = exercise_7_algorithm_implementation()
        results.append(("练习7", "bubble_sort" in result7 and "stack" in result7))
        
        # 显示结果
        print(f"\n{'练习':<10}{'状态':<10}")
        print("-" * 20)
        for exercise_name, passed in results:
            status = "✓ 完成" if passed else "✗ 未完成"
            print(f"{exercise_name:<10}{status:<10}")
        
        completed_count = sum(1 for _, passed in results if passed)
        print(f"\n总计: {completed_count}/{len(results)} 练习完成")
        
        if completed_count == len(results):
            print("🎉 恭喜！所有练习都完成了！")
        else:
            print("💪 继续努力！完成剩余的练习。")
            
    except Exception as e:
        print(f"❌ 检查过程中出现错误: {e}")
        print("请检查你的代码是否有语法错误。")

def main():
    """主函数"""
    print("Python数据结构练习题")
    print("=" * 50)
    
    while True:
        print("\n选择练习:")
        print("1. 列表操作")
        print("2. 元组操作")
        print("3. 字典操作")
        print("4. 集合操作")
        print("5. 推导式练习")
        print("6. 数据分析")
        print("7. 算法实现")
        print("8. 检查所有答案")
        print("0. 退出")
        
        choice = input("\n请选择 (0-8): ").strip()
        
        if choice == "0":
            print("学习愉快！再见！👋")
            break
        elif choice == "1":
            exercise_1_lists()
        elif choice == "2":
            exercise_2_tuples()
        elif choice == "3":
            exercise_3_dictionaries()
        elif choice == "4":
            exercise_4_sets()
        elif choice == "5":
            exercise_5_comprehensions()
        elif choice == "6":
            exercise_6_data_analysis()
        elif choice == "7":
            exercise_7_algorithm_implementation()
        elif choice == "8":
            check_answers()
        else:
            print("无效选择，请重试。")

if __name__ == "__main__":
    main()