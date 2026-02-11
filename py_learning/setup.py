#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Python学习项目设置脚本
帮助快速配置开发环境和依赖
"""

import os
import sys
import subprocess
import platform
from pathlib import Path
from typing import List, Tuple


def check_python_version() -> Tuple[bool, str]:
    """检查Python版本"""
    version = sys.version_info
    if version.major == 3 and version.minor >= 7:
        return True, f"Python {version.major}.{version.minor}.{version.micro} ✓"
    else:
        return False, f"Python {version.major}.{version.minor}.{version.micro} (需要3.7+)"


def check_command(command: str) -> bool:
    """检查命令是否存在"""
    try:
        subprocess.run([command, '--version'], 
                      capture_output=True, check=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False


def create_virtual_environment() -> bool:
    """创建虚拟环境"""
    venv_path = Path('venv')
    if venv_path.exists():
        print("虚拟环境已存在")
        return True
    
    print("创建虚拟环境...")
    try:
        subprocess.run([sys.executable, '-m', 'venv', 'venv'], 
                      check=True)
        print("虚拟环境创建成功")
        return True
    except subprocess.CalledProcessError as e:
        print(f"创建虚拟环境失败: {e}")
        return False


def get_activate_command() -> str:
    """获取激活虚拟环境的命令"""
    system = platform.system().lower()
    if system == 'windows':
        return 'venv\\Scripts\\activate'
    else:
        return 'source venv/bin/activate'


def install_dependencies() -> bool:
    """安装依赖"""
    requirements_file = Path('requirements.txt')
    if not requirements_file.exists():
        print("requirements.txt 不存在，跳过依赖安装")
        return True
    
    print("安装项目依赖...")
    try:
        # 升级pip
        subprocess.run(['python', '-m', 'pip', 'install', '--upgrade', 'pip'], 
                      check=True)
        
        # 安装依赖
        subprocess.run(['python', '-m', 'pip', 'install', '-r', 'requirements.txt'], 
                      check=True)
        print("依赖安装成功")
        return True
    except subprocess.CalledProcessError as e:
        print(f"依赖安装失败: {e}")
        return False


def run_code_quality_tools() -> bool:
    """运行代码质量检查工具"""
    print("运行代码质量检查...")
    
    tools = [
        ('flake8', 'flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics'),
        ('black', 'black --check .'),
        ('mypy', 'mypy . --ignore-missing-imports')
    ]
    
    all_passed = True
    for tool_name, command in tools:
        try:
            result = subprocess.run(command, shell=True, capture_output=True, text=True)
            if result.returncode == 0:
                print(f"{tool_name} 检查通过")
            else:
                print(f"{tool_name} 检查发现问题:")
                print(result.stdout)
                all_passed = False
        except subprocess.CalledProcessError:
            print(f"{tool_name} 检查失败")
            all_passed = False
    
    return all_passed


def run_tests() -> bool:
    """运行测试"""
    print("运行测试...")
    
    # 查找测试文件
    test_files = list(Path('.').rglob('test_*.py')) + list(Path('.').rglob('*_test.py'))
    
    if not test_files:
        print("未找到测试文件")
        return True
    
    try:
        result = subprocess.run(['python', '-m', 'pytest', '-v'], capture_output=True, text=True)
        if result.returncode == 0:
            print("所有测试通过")
            return True
        else:
            print("测试失败:")
            print(result.stdout)
            return False
    except subprocess.CalledProcessError:
        print("运行测试失败")
        return False


def print_system_info():
    """打印系统信息"""
    print("系统信息:")
    print(f"  操作系统: {platform.system()} {platform.release()}")
    print(f"  Python版本: {sys.version}")
    print(f"  工作目录: {os.getcwd()}")
    print()


def print_project_summary():
    """打印项目摘要"""
    print("项目摘要:")
    print("  这是一个完整的Python学习项目，包含以下模块:")
    print("    - 01_basics - Python基础语法")
    print("    - 02_data_structures - 数据结构")
    print("    - 03_oop - 面向对象编程")
    print("    - 04_pythonic - Python特色功能")
    print("    - 05_advanced - 高级特性")
    print("    - 06_projects - 实践项目")
    print()
    print("  实践项目包括:")
    print("    - file_manager - 文件管理工具")
    print("    - todo_api - 待办事项Web API")
    print("    - sales_analysis - 销售数据分析")
    print()


def print_next_steps():
    """打印下一步操作"""
    print("下一步操作:")
    print("1. 激活虚拟环境:")
    print(f"   {get_activate_command()}")
    print()
    print("2. 运行学习进度检查:")
    print("   python check_progress.py")
    print()
    print("3. 运行所有示例:")
    print("   python run_tests.py")
    print()
    print("4. 开始第一个模块:")
    print("   python 01_basics/examples.py")
    print()
    print("5. 尝试练习题:")
    print("   python 01_basics/exercises.py")
    print()


def main():
    """主函数"""
    print("=" * 60)
    print("Python学习项目环境设置")
    print("=" * 60)
    print()
    
    print_system_info()
    print_project_summary()
    
    # 检查Python版本
    version_ok, version_info = check_python_version()
    print(f"Python版本检查: {version_info}")
    if not version_ok:
        print("请升级Python到3.7或更高版本")
        return
    
    # 检查必要工具
    tools = ['git', 'pip']
    print("\n工具检查:")
    for tool in tools:
        status = "✓" if check_command(tool) else "✗"
        print(f"  {tool}: {status}")
    
    # 询问是否创建虚拟环境
    create_venv = input("\n是否创建虚拟环境? (y/N): ").lower().strip() in ['y', 'yes']
    if create_venv:
        if create_virtual_environment():
            print(f"\n请运行以下命令激活虚拟环境:")
            print(f"  {get_activate_command()}")
            print("\n然后重新运行此脚本")
            return
    
    # 询问是否安装依赖
    install_deps = input("\n是否安装项目依赖? (y/N): ").lower().strip() in ['y', 'yes']
    if install_deps:
        if not install_dependencies():
            print("依赖安装失败，请手动安装")
            return
    
    # 询问是否运行代码质量检查
    run_quality = input("\n是否运行代码质量检查? (y/N): ").lower().strip() in ['y', 'yes']
    if run_quality:
        run_code_quality_tools()
    
    # 询问是否运行测试
    run_test = input("\n是否运行测试? (y/N): ").lower().strip() in ['y', 'yes']
    if run_test:
        run_tests()
    
    print("\n" + "=" * 60)
    print("环境设置完成!")
    print("=" * 60)
    print()
    print_next_steps()


if __name__ == '__main__':
    main()