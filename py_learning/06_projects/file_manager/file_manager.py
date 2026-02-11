#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件管理工具
一个功能完整的命令行文件管理工具，演示Python基础知识和文件操作
"""

import os
import sys
import shutil
import argparse
import json
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Any


class FileManager:
    """文件管理器类"""
    
    def __init__(self):
        self.stats = {
            'files_processed': 0,
            'directories_created': 0,
            'errors': 0
        }
    
    def list_directory(self, path: str, show_details: bool = False) -> None:
        """列出目录内容"""
        try:
            path_obj = Path(path)
            if not path_obj.exists():
                print(f"错误: 路径 '{path}' 不存在")
                return
            
            if not path_obj.is_dir():
                print(f"错误: '{path}' 不是一个目录")
                return
            
            print(f"\n目录内容: {path_obj.absolute()}")
            print("-" * 60)
            
            items = sorted(path_obj.iterdir(), key=lambda x: (x.is_file(), x.name.lower()))
            
            for item in items:
                if show_details:
                    self._show_detailed_info(item)
                else:
                    file_type = "目录" if item.is_dir() else "文件"
                    size = self._format_size(item.stat().st_size) if item.is_file() else ""
                    print(f"{file_type:4} {item.name:<30} {size:>10}")
            
            print(f"\n总计: {len(items)} 项")
            dirs = sum(1 for item in items if item.is_dir())
            files = len(items) - dirs
            print(f"目录: {dirs}, 文件: {files}")
            
        except Exception as e:
            print(f"错误: {e}")
            self.stats['errors'] += 1
    
    def _show_detailed_info(self, path: Path) -> None:
        """显示详细信息"""
        stat = path.stat()
        file_type = "目录" if path.is_dir() else "文件"
        size = self._format_size(stat.st_size) if path.is_file() else ""
        modified = datetime.fromtimestamp(stat.st_mtime).strftime("%Y-%m-%d %H:%M:%S")
        
        print(f"{file_type:4} {path.name:<30} {size:>10} {modified}")
    
    def copy_file(self, source: str, destination: str) -> bool:
        """复制文件或目录"""
        try:
            source_path = Path(source)
            dest_path = Path(destination)
            
            if not source_path.exists():
                print(f"错误: 源文件 '{source}' 不存在")
                return False
            
            # 如果目标是目录，则构建完整的目标路径
            if dest_path.is_dir():
                dest_path = dest_path / source_path.name
            
            print(f"复制: {source_path} -> {dest_path}")
            
            if source_path.is_file():
                shutil.copy2(source_path, dest_path)
            else:
                shutil.copytree(source_path, dest_path, dirs_exist_ok=True)
            
            print("复制成功!")
            self.stats['files_processed'] += 1
            return True
            
        except Exception as e:
            print(f"复制失败: {e}")
            self.stats['errors'] += 1
            return False
    
    def move_file(self, source: str, destination: str) -> bool:
        """移动文件或目录"""
        try:
            source_path = Path(source)
            dest_path = Path(destination)
            
            if not source_path.exists():
                print(f"错误: 源文件 '{source}' 不存在")
                return False
            
            if dest_path.is_dir():
                dest_path = dest_path / source_path.name
            
            print(f"移动: {source_path} -> {dest_path}")
            shutil.move(source_path, dest_path)
            print("移动成功!")
            self.stats['files_processed'] += 1
            return True
            
        except Exception as e:
            print(f"移动失败: {e}")
            self.stats['errors'] += 1
            return False
    
    def delete_file(self, path: str, force: bool = False) -> bool:
        """删除文件或目录"""
        try:
            path_obj = Path(path)
            
            if not path_obj.exists():
                print(f"错误: 路径 '{path}' 不存在")
                return False
            
            if not force:
                response = input(f"确定要删除 '{path}' 吗? (y/N): ")
                if response.lower() not in ['y', 'yes']:
                    print("取消删除")
                    return False
            
            if path_obj.is_file():
                path_obj.unlink()
                print(f"已删除文件: {path}")
            else:
                shutil.rmtree(path_obj)
                print(f"已删除目录: {path}")
            
            self.stats['files_processed'] += 1
            return True
            
        except Exception as e:
            print(f"删除失败: {e}")
            self.stats['errors'] += 1
            return False
    
    def create_directory(self, path: str) -> bool:
        """创建目录"""
        try:
            path_obj = Path(path)
            path_obj.mkdir(parents=True, exist_ok=True)
            print(f"已创建目录: {path_obj.absolute()}")
            self.stats['directories_created'] += 1
            return True
            
        except Exception as e:
            print(f"创建目录失败: {e}")
            self.stats['errors'] += 1
            return False
    
    def find_files(self, path: str, pattern: str = "*", recursive: bool = True) -> List[str]:
        """查找文件"""
        try:
            path_obj = Path(path)
            if not path_obj.exists():
                print(f"错误: 路径 '{path}' 不存在")
                return []
            
            print(f"\n在 '{path}' 中搜索: {pattern}")
            print("-" * 60)
            
            found_files = []
            
            if recursive:
                files = path_obj.rglob(pattern)
            else:
                files = path_obj.glob(pattern)
            
            for file_path in files:
                relative_path = file_path.relative_to(path_obj)
                file_type = "目录" if file_path.is_dir() else "文件"
                size = self._format_size(file_path.stat().st_size) if file_path.is_file() else ""
                print(f"{file_type:4} {relative_path:<40} {size:>10}")
                found_files.append(str(relative_path))
            
            print(f"\n找到 {len(found_files)} 个匹配项")
            return found_files
            
        except Exception as e:
            print(f"搜索失败: {e}")
            self.stats['errors'] += 1
            return []
    
    def get_directory_size(self, path: str) -> Dict[str, Any]:
        """获取目录大小信息"""
        try:
            path_obj = Path(path)
            if not path_obj.exists():
                print(f"错误: 路径 '{path}' 不存在")
                return {}
            
            total_size = 0
            file_count = 0
            dir_count = 0
            
            if path_obj.is_file():
                total_size = path_obj.stat().st_size
                file_count = 1
            else:
                for item in path_obj.rglob('*'):
                    if item.is_file():
                        total_size += item.stat().st_size
                        file_count += 1
                    else:
                        dir_count += 1
            
            size_info = {
                'path': str(path_obj.absolute()),
                'total_size': total_size,
                'formatted_size': self._format_size(total_size),
                'file_count': file_count,
                'dir_count': dir_count,
                'total_items': file_count + dir_count
            }
            
            print(f"\n目录大小信息: {path_obj.absolute()}")
            print("-" * 60)
            print(f"总大小: {size_info['formatted_size']}")
            print(f"文件数: {file_count}")
            print(f"目录数: {dir_count}")
            print(f"总项目数: {size_info['total_items']}")
            
            return size_info
            
        except Exception as e:
            print(f"获取大小信息失败: {e}")
            self.stats['errors'] += 1
            return {}
    
    def _format_size(self, size_bytes: int) -> str:
        """格式化文件大小"""
        if size_bytes == 0:
            return "0 B"
        
        size_names = ["B", "KB", "MB", "GB", "TB"]
        i = 0
        size = float(size_bytes)
        
        while size >= 1024.0 and i < len(size_names) - 1:
            size /= 1024.0
            i += 1
        
        return f"{size:.1f} {size_names[i]}"
    
    def show_stats(self) -> None:
        """显示统计信息"""
        print("\n操作统计:")
        print("-" * 30)
        print(f"处理文件数: {self.stats['files_processed']}")
        print(f"创建目录数: {self.stats['directories_created']}")
        print(f"错误次数: {self.stats['errors']}")
    
    def backup_directory(self, source: str, backup_dir: str | None = None) -> bool:
        """备份目录"""
        try:
            source_path = Path(source)
            if not source_path.exists():
                print(f"错误: 源路径 '{source}' 不存在")
                return False
            
            backup_path: Path
            if backup_dir is None:
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                backup_name = f"{source_path.name}_backup_{timestamp}"
                backup_path = source_path.parent / backup_name
            else:
                backup_path = Path(backup_dir)
            
            print(f"开始备份: {source_path} -> {backup_path}")
            
            if source_path.is_file():
                backup_path.mkdir(parents=True, exist_ok=True)
                shutil.copy2(source_path, backup_path / source_path.name)
            else:
                shutil.copytree(source_path, backup_path, dirs_exist_ok=True)
            
            print("备份完成!")
            self.stats['files_processed'] += 1
            return True
            
        except Exception as e:
            print(f"备份失败: {e}")
            self.stats['errors'] += 1
            return False


def main():
    """主函数"""
    parser = argparse.ArgumentParser(
        description="文件管理工具 - Python学习项目示例",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例用法:
  %(prog)s --list /path/to/directory
  %(prog)s --list /path/to/directory --details
  %(prog)s --copy source.txt backup/
  %(prog)s --move old.txt new.txt
  %(prog)s --delete tempfile.txt --force
  %(prog)s --mkdir new_project
  %(prog)s --find . --name "*.py"
  %(prog)s --size /path/to/directory
  %(prog)s --backup /path/to/important/data
        """
    )
    
    parser.add_argument('--list', metavar='PATH', help='列出目录内容')
    parser.add_argument('--details', action='store_true', help='显示详细信息')
    
    parser.add_argument('--copy', nargs=2, metavar=('SOURCE', 'DEST'), 
                       help='复制文件或目录')
    parser.add_argument('--move', nargs=2, metavar=('SOURCE', 'DEST'), 
                       help='移动文件或目录')
    parser.add_argument('--delete', metavar='PATH', help='删除文件或目录')
    parser.add_argument('--force', action='store_true', help='强制删除，不询问')
    
    parser.add_argument('--mkdir', metavar='PATH', help='创建目录')
    parser.add_argument('--find', metavar='PATH', help='查找文件')
    parser.add_argument('--name', metavar='PATTERN', default='*', 
                       help='搜索模式 (默认: *)')
    parser.add_argument('--size', metavar='PATH', help='显示目录大小')
    parser.add_argument('--backup', metavar='PATH', help='备份文件或目录')
    parser.add_argument('--no-recursive', action='store_true', 
                       help='不递归搜索')
    
    parser.add_argument('--stats', action='store_true', help='显示操作统计')
    
    args = parser.parse_args()
    
    if len(sys.argv) == 1:
        parser.print_help()
        return
    
    fm = FileManager()
    
    try:
        if args.list:
            fm.list_directory(args.list, args.details)
        
        elif args.copy:
            fm.copy_file(args.copy[0], args.copy[1])
        
        elif args.move:
            fm.move_file(args.move[0], args.move[1])
        
        elif args.delete:
            fm.delete_file(args.delete, args.force)
        
        elif args.mkdir:
            fm.create_directory(args.mkdir)
        
        elif args.find:
            recursive = not args.no_recursive
            fm.find_files(args.find, args.name, recursive)
        
        elif args.size:
            fm.get_directory_size(args.size)
        
        elif args.backup:
            fm.backup_directory(args.backup)
        
        if args.stats:
            fm.show_stats()
    
    except KeyboardInterrupt:
        print("\n\n操作被用户中断")
    except Exception as e:
        print(f"程序错误: {e}")


if __name__ == '__main__':
    main()