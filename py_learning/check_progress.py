#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
check_progress.py
检查学习进度的工具

运行方式:
python check_progress.py

功能:
- 检查各模块完成情况
- 验证代码正确性
- 生成详细进度报告
"""

import os
import sys
from pathlib import Path
import importlib.util
import ast

def print_header(title):
    """打印标题"""
    print(f"\n{'='*60}")
    print(f" {title}")
    print(f"{'='*60}")

def check_module_completion():
    """检查各模块完成情况"""
    print_header("模块完成情况检查")
    
    modules = [
        ("01_basics", "基础语法", [
            "变量和数据类型", "运算符和表达式", "条件语句和循环", 
            "函数定义和调用", "字符串操作", "列表基础操作"
        ]),
        ("02_data_structures", "数据结构", [
            "列表高级操作", "元组使用", "字典操作", "集合操作", 
            "推导式语法", "数据结构选择"
        ]),
        ("03_oop", "面向对象编程", [
            "类和对象", "继承机制", "特殊方法", "属性装饰器", 
            "私有成员", "多态和鸭子类型"
        ]),
        ("04_pythonic", "Python特色功能", [
            "列表推导式", "字典推导式", "生成器", "装饰器", 
            "上下文管理器", "异常处理"
        ]),
        ("05_advanced", "高级特性", [
            "并发编程", "文件操作", "正则表达式", "包管理", 
            "调试和测试", "标准库使用"
        ])
    ]
    
    total_score = 0
    max_score = len(modules) * 100
    
    print(f"{'模块':<20} {'完成度':<10} {'示例':<8} {'练习':<8} {'说明':<8} {'状态':<10}")
    print("-" * 80)
    
    for module_dir, module_name, topics in modules:
        # 检查文件存在性
        examples_file = Path(module_dir) / "examples.py"
        exercises_file = Path(module_dir) / "exercises.py"
        readme_file = Path(module_dir) / "README.md"
        
        file_scores = {
            "examples": 40 if examples_file.exists() else 0,
            "exercises": 40 if exercises_file.exists() else 0,
            "readme": 20 if readme_file.exists() else 0
        }
        
        completion_score = sum(file_scores.values())
        total_score += completion_score
        
        # 检查代码质量
        code_quality = check_code_quality(examples_file) if examples_file.exists() else 0
        completion_score = min(completion_score + code_quality, 100)
        
        # 显示状态
        status = "完成" if completion_score >= 90 else "进行中" if completion_score >= 50 else "未开始"
        
        print(f"{module_name:<20} {completion_score:<10} {'OK' if file_scores['examples'] else 'NO':<8} "
              f"{'OK' if file_scores['exercises'] else 'NO':<8} {'OK' if file_scores['readme'] else 'NO':<8} {status:<10}")
        
        # 显示主题覆盖
        if completion_score >= 50:
            covered_topics = check_topics_covered(examples_file, topics) if examples_file.exists() else []
            if covered_topics:
                print(f"   已覆盖主题: {', '.join(covered_topics[:3])}{'...' if len(covered_topics) > 3 else ''}")
    
    print(f"\n总体完成度: {total_score}/{max_score} ({total_score/max_score*100:.1f}%)")
    return total_score / max_score

def check_code_quality(file_path):
    """检查代码质量"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 解析AST
        tree = ast.parse(content)
        
        quality_score = 0
        max_score = 20
        
        # 检查函数数量
        functions = [node for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)]
        if len(functions) >= 5:
            quality_score += 5
        
        # 检查类的数量（如果是OOP模块）
        classes = [node for node in ast.walk(tree) if isinstance(node, ast.ClassDef)]
        if len(classes) >= 2:
            quality_score += 5
        
        # 检查注释
        lines = content.split('\n')
        comment_lines = [line for line in lines if line.strip().startswith('#')]
        if len(comment_lines) >= 10:
            quality_score += 5
        
        # 检查文档字符串（简化版本）
        docstrings = [node for node in ast.walk(tree) 
                     if isinstance(node, (ast.FunctionDef, ast.ClassDef))]
        # 假设有文档字符串的函数/类
        if len(docstrings) >= 3:
            quality_score += 5
        
        return min(quality_score, max_score)
        
    except:
        return 0

def check_topics_covered(file_path, topics):
    """检查主题覆盖情况"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        covered = []
        for topic in topics:
            # 简单的关键词匹配
            keywords = {
                "变量": ["variable", "var", "变量"],
                "数据类型": ["int", "str", "float", "bool", "type"],
                "运算符": ["operator", "+", "-", "*", "/", "==", "运算"],
                "条件": ["if", "else", "elif", "condition", "条件"],
                "循环": ["for", "while", "loop", "循环"],
                "函数": ["def", "function", "函数"],
                "字符串": ["str", "string", "字符串"],
                "列表": ["list", "列表"],
                "字典": ["dict", "dictionary", "字典"],
                "集合": ["set", "集合"],
                "元组": ["tuple", "元组"],
                "类": ["class", "类"],
                "对象": ["object", "对象"],
                "继承": ["inherit", "继承"],
                "多态": ["polymorph", "多态"],
                "推导式": ["comprehension", "推导"],
                "生成器": ["generator", "yield", "生成器"],
                "装饰器": ["decorator", "装饰器"],
                "上下文": ["context", "with", "上下文"],
                "异常": ["exception", "try", "except", "异常"],
                "并发": ["thread", "async", "concurrent", "并发"],
                "文件": ["file", "open", "文件"],
                "正则": ["regex", "re", "正则"]
            }
            
            # 检查主题相关的关键词
            topic_keywords = keywords.get(topic, [])
            for keyword in topic_keywords:
                if keyword.lower() in content.lower():
                    covered.append(topic)
                    break
        
        return covered
        
    except:
        return []

def check_exercises_completion():
    """检查练习完成情况"""
    print_header("练习完成情况检查")
    
    exercise_modules = ["01_basics", "02_data_structures", "03_oop", "04_pythonic", "05_advanced"]
    
    total_exercises = 0
    completed_exercises = 0
    
    for module in exercise_modules:
        exercises_file = Path(module) / "exercises.py"
        
        if exercises_file.exists():
            try:
                with open(exercises_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # 计算练习数量（以exercise_开头的函数）
                tree = ast.parse(content)
                functions = [node for node in ast.walk(tree) 
                           if isinstance(node, ast.FunctionDef) and node.name.startswith('exercise_')]
                
                module_exercises = len(functions)
                module_completed = 0
                
                # 简单检查是否有实现（函数体不为空）
                for func in functions:
                    if func.body and len(func.body) > 1:  # 超过只有文档字符串
                        module_completed += 1
                
                total_exercises += module_exercises
                completed_exercises += module_completed
                
                completion_rate = (module_completed / module_exercises * 100) if module_exercises > 0 else 0
                status = "完成" if completion_rate >= 80 else "进行中" if completion_rate >= 50 else "未开始"
                
                print(f"{module:<20} {module_completed}/{module_exercises:<10} ({completion_rate:.0f}%) {status}")
                
            except Exception as e:
                print(f"{module:<20} 解析失败: {e}")
        else:
            print(f"{module:<20} 练习文件不存在")
    
    overall_rate = (completed_exercises / total_exercises * 100) if total_exercises > 0 else 0
    print(f"\n练习总完成率: {completed_exercises}/{total_exercises} ({overall_rate:.0f}%)")
    
    return overall_rate

def generate_learning_recommendations(overall_progress):
    """生成学习建议"""
    print_header("学习建议")
    
    if overall_progress >= 0.9:
        print("恭喜你！你已经完成了大部分Python学习内容！")
        print("建议:")
        print("   • 开始实践项目，应用到实际场景")
        print("   • 学习更高级的主题（如机器学习、Web开发）")
        print("   • 参与开源项目，提升实战经验")
        
    elif overall_progress >= 0.7:
        print("太棒了！你已经掌握了Python的核心知识！")
        print("建议:")
        print("   - 完成剩余的高级特性学习")
        print("   - 重点练习Pythonic编程风格")
        print("   - 尝试构建小型项目")
        
    elif overall_progress >= 0.5:
        print("不错！你已经掌握了Python的基础知识！")
        print("建议:")
        print("   - 继续学习高级特性")
        print("   - 多做编程练习")
        print("   - 重点关注面向对象编程")
        
    elif overall_progress >= 0.3:
        print("继续努力！你正在稳步前进！")
        print("建议:")
        print("   - 重点完成基础语法和数据结构")
        print("   - 每天坚持编写Python代码")
        print("   - 多做练习题巩固知识")
        
    else:
        print("刚开始，加油！Python是一门很棒的语言！")
        print("建议:")
        print("   - 从基础语法模块开始")
        print("   - 仔细阅读示例代码")
        print("   - 每天学习1-2小时")
    
    print("\n通用学习技巧:")
    print("   - 理论结合实践，多写代码")
    print("   - 不要害怕犯错，错误是最好的老师")
    print("   - 加入Python社区，与其他学习者交流")
    print("   - 定期复习，巩固已学知识")
    print("   - 尝试解决实际问题")

def main():
    """主函数"""
    print("Python学习进度检查工具")
    print("=" * 60)
    
    # 检查各模块完成情况
    module_progress = check_module_completion()
    
    # 检查练习完成情况
    exercise_progress = check_exercises_completion() / 100
    
    # 计算总体进度
    overall_progress = (module_progress + exercise_progress) / 2
    
    print(f"\n总体学习进度: {overall_progress*100:.1f}%")
    
    # 生成学习建议
    generate_learning_recommendations(overall_progress)
    
    # 生成下一步计划
    print_header("下一步学习计划")
    
    if overall_progress < 0.3:
        print("1. 完成基础语法模块 (01_basics)")
        print("2. 练习所有基础语法练习题")
        print("3. 开始学习数据结构 (02_data_structures)")
        
    elif overall_progress < 0.5:
        print("1. 完成数据结构模块 (02_data_structures)")
        print("2. 开始学习面向对象编程 (03_oop)")
        print("3. 多做数据结构相关的练习")
        
    elif overall_progress < 0.7:
        print("1. 完成面向对象编程模块 (03_oop)")
        print("2. 学习Python特色功能 (04_pythonic)")
        print("3. 尝试编写小型程序")
        
    elif overall_progress < 0.9:
        print("1. 完成Python特色功能模块 (04_pythonic)")
        print("2. 学习高级特性 (05_advanced)")
        print("3. 开始实践项目 (06_projects)")
        
    else:
        print("1. 完成所有理论学习")
        print("2. 深入实践项目 (06_projects)")
        print("3. 探索专业领域（Web开发、数据科学等）")
    
    print(f"\n检查完成时间: {__import__('datetime').datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("继续加油，你一定可以掌握Python的！")

if __name__ == "__main__":
    main()