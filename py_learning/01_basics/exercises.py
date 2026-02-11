#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
01_basics/exercises.py
Python基础语法练习题

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

def exercise_1_variables():
    """练习1: 变量和数据类型"""
    print_exercise_title("变量和数据类型")
    
    print("任务:")
    print("1. 创建变量表示你的信息(姓名, 年龄, 身高, 是否为程序员)")
    print("2. 打印每个变量的值和类型")
    print("3. 将年龄转换为字符串并与姓名连接")
    
    # 在这里写你的代码:
    name = "张三"  # 替换为你的姓名
    age = 25       # 替换为你的年龄
    height = 1.75  # 替换为你的身高
    is_programmer = True
    
    print(f"\n你的代码:")
    print(f"name = '{name}', type: {type(name)}")
    print(f"age = {age}, type: {type(age)}")
    print(f"height = {height}, type: {type(height)}")
    print(f"is_programmer = {is_programmer}, type: {type(is_programmer)}")
    
    age_str = str(age)
    full_info = name + age_str
    print(f"姓名+年龄(字符串): {full_info}")
    
    return name, age, height, is_programmer

def exercise_2_operators():
    """练习2: 运算符"""
    print_exercise_title("运算符")
    
    print("任务:")
    print("1. 计算圆的面积(半径=5)")
    print("2. 判断一个数是否为偶数")
    print("3. 使用逻辑运算符组合多个条件")
    
    import math
    
    radius = 5
    area = math.pi * radius ** 2
    print(f"\n你的代码:")
    print(f"半径为{radius}的圆的面积: {area:.2f}")
    
    number = 8
    is_even = (number % 2 == 0)
    print(f"{number}是偶数吗? {is_even}")
    
    age = 25
    has_license = True
    can_drive = (age >= 18) and has_license
    print(f"年龄{age}岁，有驾照，可以开车吗? {can_drive}")
    
    return area, is_even, can_drive

def exercise_3_statements():
    """练习3: 条件语句和循环"""
    print_exercise_title("条件语句和循环")
    
    print("任务:")
    print("1. 根据分数给出等级(A-F)")
    print("2. 打印1-10之间的所有偶数")
    print("3. 计算列表中所有正数的和")
    
    score = 85
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"
    
    print(f"\n你的代码:")
    print(f"分数{score}对应等级: {grade}")
    
    print("1-10之间的偶数:")
    for i in range(1, 11):
        if i % 2 == 0:
            print(f"  {i}")
    
    numbers = [1, -2, 3, -4, 5, -6, 7]
    positive_sum = 0
    for num in numbers:
        if num > 0:
            positive_sum += num
    
    print(f"列表{numbers}中正数的和: {positive_sum}")
    
    return grade, positive_sum

def exercise_4_functions():
    """练习4: 函数"""
    print_exercise_title("函数")
    
    print("任务:")
    print("1. 创建一个计算圆面积的函数")
    print("2. 创建一个返回最大值的函数")
    print("3. 创建一个包含默认参数的函数")
    
    def circle_area(radius):
        import math
        return math.pi * radius ** 2
    
    def find_max(*args):
        if not args:
            return None
        max_val = args[0]
        for num in args[1:]:
            if num > max_val:
                max_val = num
        return max_val
    
    def greet(name, greeting="Hello"):
        return f"{greeting}, {name}!"
    
    print(f"\n你的代码:")
    print(f"半径3的圆面积: {circle_area(3):.2f}")
    print(f"最大值: {find_max(1, 5, 3, 9, 2)}")
    print(f"greet('Alice'): {greet('Alice')}")
    print(f"greet('Bob', 'Hi'): {greet('Bob', 'Hi')}")
    
    return circle_area, find_max, greet

def exercise_5_strings():
    """练习5: 字符串操作"""
    print_exercise_title("字符串操作")
    
    print("任务:")
    print("1. 格式化个人信息")
    print("2. 检查字符串包含关系")
    print("3. 使用切片操作字符串")
    
    name = "Alice Johnson"
    age = 25
    city = "Beijing"
    
    formatted_info = f"姓名: {name}, 年龄: {age}, 城市: {city}"
    print(f"\n你的代码:")
    print(formatted_info)
    
    text = "Python programming is fun and powerful"
    has_python = "Python" in text
    has_java = "Java" in text
    print(f"文本包含'Python': {has_python}")
    print(f"文本包含'Java': {has_java}")
    
    sentence = "Hello, World!"
    print(f"原句: '{sentence}'")
    print(f"前5个字符: '{sentence[:5]}'")
    print(f"后5个字符: '{sentence[-5:]}'")
    print(f"反转: '{sentence[::-1]}'")
    
    # 字符串处理
    email = "  alice@example.com  "
    processed_email = email.strip().lower()
    print(f"处理后的邮箱: '{processed_email}'")
    
    return formatted_info, has_python, processed_email

def exercise_6_lists():
    """练习6: 列表操作"""
    print_exercise_title("列表操作")
    
    print("任务:")
    print("1. 创建数字列表并计算统计信息")
    print("2. 列表元素的增删改查")
    print("3. 列表推导式练习")
    
    # 创建1-10的平方数列表
    squares = [i ** 2 for i in range(1, 11)]
    print(f"\n你的代码:")
    print(f"1-10的平方数: {squares}")
    
    # 统计信息
    total = sum(squares)
    average = total / len(squares)
    maximum = max(squares)
    minimum = min(squares)
    
    print(f"和: {total}, 平均值: {average:.2f}")
    print(f"最大值: {maximum}, 最小值: {minimum}")
    
    # 列表操作
    fruits = ["apple", "banana", "orange"]
    fruits.append("grape")
    fruits.insert(1, "kiwi")
    fruits.remove("banana")
    last_fruit = fruits.pop()
    
    print(f"水果列表操作后: {fruits}")
    print(f"删除的最后一个水果: {last_fruit}")
    
    # 筛选偶数
    numbers = list(range(1, 21))
    even_numbers = [num for num in numbers if num % 2 == 0]
    print(f"1-20中的偶数: {even_numbers}")
    
    return squares, fruits, even_numbers

def exercise_7_comprehensive():
    """练习7: 综合练习"""
    print_exercise_title("综合练习")
    
    print("任务:")
    print("1. 创建学生信息管理系统")
    print("2. 实现成绩统计和排名")
    print("3. 输出格式化报告")
    
    # 学生数据
    students = [
        {"name": "张三", "chinese": 85, "math": 92, "english": 78},
        {"name": "李四", "chinese": 76, "math": 88, "english": 92},
        {"name": "王五", "chinese": 92, "math": 85, "english": 88},
        {"name": "赵六", "chinese": 68, "math": 72, "english": 76}
    ]
    
    def calculate_total(student):
        return student["chinese"] + student["math"] + student["english"]
    
    def calculate_average(student):
        total = calculate_total(student)
        return total / 3
    
    def get_grade(score):
        if score >= 90:
            return "A"
        elif score >= 80:
            return "B"
        elif score >= 70:
            return "C"
        elif score >= 60:
            return "D"
        else:
            return "F"
    
    # 计算总分和平均分
    for student in students:
        student["total"] = calculate_total(student)
        student["average"] = calculate_average(student)
        student["grade"] = get_grade(student["average"])
    
    # 按总分排序
    students_sorted = sorted(students, key=lambda x: x["total"], reverse=True)
    
    print(f"\n你的代码 - 学生成绩报告:")
    print(f"{'排名':<4}{'姓名':<8}{'语文':<6}{'数学':<6}{'英语':<6}{'总分':<6}{'平均分':<8}{'等级':<4}")
    print("-" * 50)
    
    for rank, student in enumerate(students_sorted, 1):
        print(f"{rank:<4}{student['name']:<8}{student['chinese']:<6}{student['math']:<6}"
              f"{student['english']:<6}{student['total']:<6}{student['average']:<8.1f}{student['grade']:<4}")
    
    # 计算班级统计
    class_total = sum(student["total"] for student in students)
    class_avg = class_total / len(students)
    highest_total = max(student["total"] for student in students)
    lowest_total = min(student["total"] for student in students)
    
    print(f"\n班级统计:")
    print(f"班级总分: {class_total}")
    print(f"班级平均分: {class_avg:.2f}")
    print(f"最高分: {highest_total}")
    print(f"最低分: {lowest_total}")
    
    return students_sorted, class_avg

def check_answers():
    """检查练习答案"""
    print("\n" + "="*50)
    print(" 检查练习完成情况")
    print("="*50)
    
    try:
        # 执行所有练习
        results = []
        
        print("执行练习1...")
        result1 = exercise_1_variables()
        results.append(("练习1", result1[0] is not None))
        
        print("执行练习2...")
        result2 = exercise_2_operators()
        results.append(("练习2", result2[0] > 0))
        
        print("执行练习3...")
        result3 = exercise_3_statements()
        results.append(("练习3", result3[0] in "ABCDEF"))
        
        print("执行练习4...")
        result4 = exercise_4_functions()
        results.append(("练习4", callable(result4[0])))
        
        print("执行练习5...")
        result5 = exercise_5_strings()
        results.append(("练习5", "Alice" in result5[0]))
        
        print("执行练习6...")
        result6 = exercise_6_lists()
        results.append(("练习6", len(result6[0]) > 0))
        
        print("执行练习7...")
        result7 = exercise_7_comprehensive()
        results.append(("练习7", len(result7[0]) > 0))
        
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
    print("Python基础语法练习题")
    print("=" * 50)
    
    while True:
        print("\n选择练习:")
        print("1. 变量和数据类型")
        print("2. 运算符")
        print("3. 条件语句和循环")
        print("4. 函数")
        print("5. 字符串操作")
        print("6. 列表操作")
        print("7. 综合练习")
        print("8. 检查所有答案")
        print("0. 退出")
        
        choice = input("\n请选择 (0-8): ").strip()
        
        if choice == "0":
            print("学习愉快！再见！👋")
            break
        elif choice == "1":
            exercise_1_variables()
        elif choice == "2":
            exercise_2_operators()
        elif choice == "3":
            exercise_3_statements()
        elif choice == "4":
            exercise_4_functions()
        elif choice == "5":
            exercise_5_strings()
        elif choice == "6":
            exercise_6_lists()
        elif choice == "7":
            exercise_7_comprehensive()
        elif choice == "8":
            check_answers()
        else:
            print("无效选择，请重试。")

if __name__ == "__main__":
    main()