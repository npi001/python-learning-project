#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件管理工具测试用例
演示如何为Python项目编写测试
"""

import os
import sys
import unittest
import tempfile
import shutil
from pathlib import Path
from unittest.mock import patch, StringIO

# 添加项目根目录到Python路径
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from file_manager.file_manager import FileManager


class TestFileManager(unittest.TestCase):
    """文件管理器测试类"""
    
    def setUp(self):
        """测试前准备"""
        self.fm = FileManager()
        self.test_dir = tempfile.mkdtemp()
        self.test_file = Path(self.test_dir) / "test.txt"
        self.test_file.write_text("测试内容", encoding='utf-8')
    
    def tearDown(self):
        """测试后清理"""
        shutil.rmtree(self.test_dir, ignore_errors=True)
    
    def test_list_directory_exists(self):
        """测试列出存在的目录"""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.fm.list_directory(self.test_dir)
            output = mock_stdout.getvalue()
            self.assertIn("目录内容", output)
            self.assertIn("test.txt", output)
    
    def test_list_directory_not_exists(self):
        """测试列出不存在的目录"""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.fm.list_directory("/nonexistent/path")
            output = mock_stdout.getvalue()
            self.assertIn("错误", output)
            self.assertIn("不存在", output)
    
    def test_copy_file_success(self):
        """测试成功复制文件"""
        dest_dir = Path(self.test_dir) / "backup"
        dest_dir.mkdir()
        result = self.fm.copy_file(str(self.test_file), str(dest_dir))
        
        self.assertTrue(result)
        self.assertTrue((dest_dir / "test.txt").exists())
        self.assertEqual(self.fm.stats['files_processed'], 1)
    
    def test_copy_file_not_exists(self):
        """测试复制不存在的文件"""
        result = self.fm.copy_file("/nonexistent/file.txt", self.test_dir)
        self.assertFalse(result)
        self.assertEqual(self.fm.stats['errors'], 1)
    
    def test_create_directory_success(self):
        """测试成功创建目录"""
        new_dir = Path(self.test_dir) / "new_directory"
        result = self.fm.create_directory(str(new_dir))
        
        self.assertTrue(result)
        self.assertTrue(new_dir.exists())
        self.assertEqual(self.fm.stats['directories_created'], 1)
    
    def test_delete_file_with_force(self):
        """测试强制删除文件"""
        result = self.fm.delete_file(str(self.test_file), force=True)
        
        self.assertTrue(result)
        self.assertFalse(self.test_file.exists())
        self.assertEqual(self.fm.stats['files_processed'], 1)
    
    def test_find_files(self):
        """测试查找文件"""
        # 创建更多测试文件
        (Path(self.test_dir) / "test.py").write_text("# Python file")
        (Path(self.test_dir) / "data.json").write_text('{"key": "value"}')
        
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            found = self.fm.find_files(self.test_dir, "*.py")
            output = mock_stdout.getvalue()
            
            self.assertEqual(len(found), 1)
            self.assertIn("test.py", output)
    
    def test_get_directory_size(self):
        """测试获取目录大小"""
        size_info = self.fm.get_directory_size(self.test_dir)
        
        self.assertIn('total_size', size_info)
        self.assertIn('file_count', size_info)
        self.assertIn('formatted_size', size_info)
        self.assertEqual(size_info['file_count'], 1)
    
    def test_format_size(self):
        """测试文件大小格式化"""
        # 测试不同大小的格式化
        self.assertEqual(self.fm._format_size(0), "0 B")
        self.assertEqual(self.fm._format_size(1024), "1.0 KB")
        self.assertEqual(self.fm._format_size(1024*1024), "1.0 MB")
    
    def test_backup_directory(self):
        """测试目录备份"""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            result = self.fm.backup_directory(self.test_dir)
            
            self.assertTrue(result)
            output = mock_stdout.getvalue()
            self.assertIn("备份完成", output)
            self.assertEqual(self.fm.stats['files_processed'], 1)
    
    def test_show_stats(self):
        """测试显示统计信息"""
        self.fm.stats['files_processed'] = 5
        self.fm.stats['directories_created'] = 2
        self.fm.stats['errors'] = 1
        
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.fm.show_stats()
            output = mock_stdout.getvalue()
            
            self.assertIn("处理文件数: 5", output)
            self.assertIn("创建目录数: 2", output)
            self.assertIn("错误次数: 1", output)


def run_tests():
    """运行所有测试"""
    print("运行文件管理工具测试...")
    print("=" * 50)
    
    # 创建测试套件
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFileManager)
    
    # 运行测试
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # 输出结果
    print("\n测试结果:")
    print(f"运行测试: {result.testsRun}")
    print(f"失败: {len(result.failures)}")
    print(f"错误: {len(result.errors)}")
    print(f"成功率: {((result.testsRun - len(result.failures) - len(result.errors)) / result.testsRun * 100):.1f}%")
    
    return result.wasSuccessful()


if __name__ == '__main__':
    success = run_tests()
    sys.exit(0 if success else 1)