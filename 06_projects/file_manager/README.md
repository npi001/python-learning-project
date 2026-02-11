# 文件管理工具项目

## 项目概述
这是一个功能完整的命令行文件管理工具，演示了Python在文件操作、命令行参数处理、错误管理等方面的应用。

## 功能特性
- 列出目录内容（简单/详细视图）
- 复制、移动、删除文件和目录
- 创建目录
- 文件搜索（支持通配符）
- 目录大小统计
- 目录备份功能
- 操作统计和错误处理

## 技术要点
- `pathlib` - 现代路径操作
- `argparse` - 命令行参数解析
- `shutil` - 高级文件操作
- 异常处理和用户交互
- 类型注解（Type Hints）

## 使用示例

### 基本操作
```bash
# 列出当前目录
python file_manager.py --list .

# 显示详细信息
python file_manager.py --list . --details

# 复制文件
python file_manager.py --copy source.txt backup/

# 移动文件
python file_manager.py --move old.txt new.txt

# 创建目录
python file_manager.py --mkdir my_project
```

### 高级操作
```bash
# 搜索Python文件
python file_manager.py --find . --name "*.py"

# 获取目录大小
python file_manager.py --size /path/to/directory

# 备份目录
python file_manager.py --backup /path/to/important/data

# 强制删除（不询问）
python file_manager.py --delete tempfile.txt --force
```

## 学习目标
通过这个项目，你将学会：
1. 如何使用Python进行文件系统操作
2. 命令行工具的设计和实现
3. 错误处理和用户体验设计
4. 代码组织和模块化
5. Python标准库的强大功能

## 扩展练习
1. 添加文件内容搜索功能
2. 实现文件压缩和解压
3. 添加配置文件支持
4. 实现批量重命名功能
5. 添加进度条显示