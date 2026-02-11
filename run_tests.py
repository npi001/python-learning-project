#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
run_tests.py
运行所有测试和示例的主脚本

运行方式:
python run_tests.py

功能:
- 运行所有模块的示例代码
- 检查代码语法和导入
- 生成学习进度报告
"""

import os
import sys
import subprocess
import importlib.util
from pathlib import Path

def print_header(title):
    """打印标题"""
    print(f"\n{'='*70}")
    print(f" {title}")
    print(f"{'='*70}")

def run_examples():
    """运行所有示例代码"""
    print_header("运行示例代码")
    
    examples = [
        ("01_basics", "基础语法"),
        ("02_data_structures", "数据结构"),
        ("03_oop", "面向对象编程"),
        ("04_pythonic", "Python特色功能"),
        ("05_advanced", "高级特性")
    ]
    
    for module, name in examples:
        example_file = Path(f"{module}/examples.py")
        if example_file.exists():
            print(f"\n运行 {name} 示例...")
            try:
                result = subprocess.run([sys.executable, str(example_file)], 
                                     capture_output=True, text=True, timeout=30)
                if result.returncode == 0:
                    print(f"{name} 示例运行成功")
                    # 显示输出的前几行
                    output_lines = result.stdout.split('\n')[:10]
                    for line in output_lines:
                        if line.strip():
                            print(f"   {line}")
                else:
                    print(f"{name} 示例运行失败")
                    print(f"   错误: {result.stderr}")
            except subprocess.TimeoutExpired:
                print(f"{name} 示例运行超时")
            except Exception as e:
                print(f"{name} 示例运行出错: {e}")
        else:
            print(f"{name} 示例文件不存在: {example_file}")

def check_syntax():
    """检查所有Python文件的语法"""
    print_header("检查语法")
    
    python_files = []
    for root, dirs, files in os.walk('.'):
        # 跳过__pycache__目录
        dirs[:] = [d for d in dirs if not d.startswith('__')]
        for file in files:
            if file.endswith('.py') and not file.startswith('run_'):
                python_files.append(Path(root) / file)
    
    syntax_errors = []
    syntax_warnings = []
    
    for py_file in python_files:
        try:
            # 编译检查语法
            with open(py_file, 'r', encoding='utf-8') as f:
                compile(f.read(), str(py_file), 'exec')
            
            # 检查一些常见的Python代码风格问题
            with open(py_file, 'r', encoding='utf-8') as f:
                content = f.read()
                
                # 检查行长度
                lines = content.split('\n')
                long_lines = [i+1 for i, line in enumerate(lines) 
                             if len(line) > 100 and not line.strip().startswith('#')]
                
                if long_lines:
                    syntax_warnings.append(f"{py_file}: 行过长 {long_lines}")
                
                # 检查常见问题
                if 'import *' in content:
                    syntax_warnings.append(f"{py_file}: 使用了 import *")
                
                if 'eval(' in content and 'security' not in py_file.name.lower():
                    syntax_warnings.append(f"{py_file}: 使用了 eval() 函数")
                
        except SyntaxError as e:
            syntax_errors.append(f"{py_file}: {e}")
        except Exception as e:
            syntax_errors.append(f"{py_file}: 读取错误 - {e}")
    
    # 显示结果
    if syntax_errors:
        print("语法错误:")
        for error in syntax_errors:
            print(f"   {error}")
    else:
        print("所有文件语法正确")
    
    if syntax_warnings:
        print("\n代码风格警告:")
        for warning in syntax_warnings:
            print(f"   {warning}")
    else:
        print("代码风格检查通过")
    
    return len(syntax_errors) == 0

def check_imports():
    """检查模块导入"""
    print_header("检查模块导入")
    
    modules_to_check = [
        ("01_basics.examples", "基础语法示例"),
        ("02_data_structures.examples", "数据结构示例"),
        ("03_oop.examples", "面向对象示例"),
        ("04_pythonic.examples", "Python特色功能示例"),
        ("05_advanced.examples", "高级特性示例")
    ]
    
    import_errors = []
    
    for module_name, description in modules_to_check:
        try:
            # 尝试导入模块
            spec = importlib.util.spec_from_file_location(
                module_name, 
                f"{module_name.replace('.', '/')}.py"
            )
            if spec and spec.loader:
                module = importlib.util.module_from_spec(spec)
                # 只导入，不执行
                print(f"✅ {description}: 导入成功")
            else:
                import_errors.append(f"{description}: 无法创建模块规格")
        except Exception as e:
            import_errors.append(f"{description}: {e}")
    
    if import_errors:
        print("\n导入错误:")
        for error in import_errors:
            print(f"   {error}")
    else:
        print("所有模块导入成功")
    
    return len(import_errors) == 0

def generate_progress_report():
    """生成学习进度报告"""
    print_header("学习进度报告")
    
    # 检查各模块完成情况
    modules = [
        ("01_basics", "基础语法", "variables, operators, statements, functions, strings"),
        ("02_data_structures", "数据结构", "list, tuple, dict, set, comprehension"),
        ("03_oop", "面向对象编程", "class, inheritance, polymorphism, encapsulation"),
        ("04_pythonic", "Python特色功能", "comprehensions, generators, decorators, context managers"),
        ("05_advanced", "高级特性", "concurrency, file operations, regex, packaging")
    ]
    
    total_modules = len(modules)
    completed_modules = 0
    
    print(f"模块完成情况:")
    print("-" * 70)
    
    for module_dir, module_name, topics in modules:
        examples_file = Path(module_dir) / "examples.py"
        exercises_file = Path(module_dir) / "exercises.py"
        readme_file = Path(module_dir) / "README.md"
        
        files_exist = sum([
            examples_file.exists(),
            exercises_file.exists(),
            readme_file.exists()
        ])
        
        completion = files_exist / 3 * 100
        if completion == 100:
            completed_modules += 1
            status = "完成"
        elif completion >= 66:
            status = "进行中"
        else:
            status = "未开始"
        
        print(f"   {module_name:<20} {completion:>6.0f}% {status}")
        print(f"      主题: {topics}")
    
    # 统计代码文件
    print(f"\n项目统计:")
    python_files = list(Path('.').rglob('*.py'))
    markdown_files = list(Path('.').rglob('*.md'))
    
    print(f"   Python文件: {len(python_files)} 个")
    print(f"   Markdown文件: {len(markdown_files)} 个")
    print(f"   代码总行数: {count_lines(python_files)} 行")
    
    # 学习建议
    print(f"\n学习建议:")
    progress_percentage = completed_modules / total_modules * 100
    
    if progress_percentage == 100:
        print("   恭喜！你已经完成了所有模块的学习！")
        print("   现在可以开始实践项目了！")
    elif progress_percentage >= 80:
        print("   太棒了！你已经掌握了大部分Python知识！")
        print("   建议完成剩余模块的学习")
    elif progress_percentage >= 60:
        print("   不错！你已经掌握了Python的基础知识！")
        print("   继续努力，完成更多模块")
    elif progress_percentage >= 40:
        print("   继续学习，你正在稳步前进！")
        print("   建议每天学习1-2小时")
    else:
        print("   刚刚开始，加油！")
        print("   建议从基础语法模块开始")
    
    return completed_modules / total_modules

def count_lines(files):
    """统计代码行数"""
    total_lines = 0
    for file in files:
        try:
            with open(file, 'r', encoding='utf-8') as f:
                total_lines += len(f.readlines())
        except:
            pass
    return total_lines

def generate_learning_plan():
    """生成个性化学习计划"""
    print_header("个性化学习计划")
    
    current_time = __import__('datetime').datetime.now()
    
    print(f"学习计划生成时间: {current_time.strftime('%Y-%m-%d %H:%M:%S')}")
    print("\n推荐学习路径:")
    
    learning_plan = [
        {
            "week": 1,
            "topic": "基础语法强化",
            "tasks": [
                "完成01_basics/examples.py中的所有示例",
                "解决01_basics/exercises.py中的练习题",
                "重点练习变量、函数、条件语句",
                "编写简单的Python脚本"
            ]
        },
        {
            "week": 2,
            "topic": "数据结构掌握",
            "tasks": [
                "学习列表、字典、集合的高级用法",
                "掌握推导式语法",
                "练习数据结构操作",
                "完成相关练习题"
            ]
        },
        {
            "week": 3,
            "topic": "面向对象编程",
            "tasks": [
                "理解类和对象的概念",
                "学习继承和多态",
                "练习特殊方法的使用",
                "编写面向对象的程序"
            ]
        },
        {
            "week": 4,
            "topic": "Python特色功能",
            "tasks": [
                "掌握列表/字典推导式",
                "学习生成器和装饰器",
                "理解上下文管理器",
                "写出更Pythonic的代码"
            ]
        },
        {
            "week": 5-6,
            "topic": "高级特性和实践",
            "tasks": [
                "学习文件操作和异常处理",
                "了解并发编程",
                "掌握模块和包管理",
                "开始小项目实践"
            ]
        }
    ]
    
    for week_plan in learning_plan:
        week_range = week_plan["week"]
        topic = week_plan["topic"]
        tasks = week_plan["tasks"]
        
        print(f"\n   第{week_range}周: {topic}")
        for task in tasks:
            print(f"     - {task}")
    
    print("\n学习技巧:")
    print("   - 每天保持练习，即使只有30分钟")
    print("   - 多写代码，少看教程")
    print("   - 遇到问题时先尝试自己解决")
    print("   - 加入Python学习社区，与他人交流")
    print("   - 定期复习之前学过的内容")

def main():
    """主函数"""
    print("Python学习测试工具")
    print("=" * 70)
    
    # 检查Python版本
    version = sys.version_info
    print(f"Python版本: {version.major}.{version.minor}.{version.micro}")
    
    if version.major < 3 or version.minor < 7:
        print("⚠️  建议使用Python 3.7或更高版本")
    
    # 运行检查
    syntax_ok = check_syntax()
    imports_ok = check_imports()
    
    if syntax_ok and imports_ok:
        print("\n代码检查通过，可以运行示例...")
        run_examples()
    else:
        print("\n代码检查失败，请先修复错误")
    
    # 生成报告
    progress = generate_progress_report()
    generate_learning_plan()
    
    # 总结
    print_header("总结")
    if syntax_ok and imports_ok:
        print("所有检查都通过了！")
        print("你已经准备好开始Python学习之旅了！")
        print("建议按照学习计划逐步进行")
    else:
        print("请先修复代码问题")
        print("然后重新运行此脚本进行检查")
    
    print("\n如需帮助，请查看:")
    print("   - README.md - 项目说明")
    print("   - 各模块目录下的README.md - 详细说明")
    print("   - examples.py - 示例代码")
    print("   - exercises.py - 练习题")
    
    print(f"\n运行完成于: {__import__('datetime').datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

if __name__ == "__main__":
    main()