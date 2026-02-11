#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
待办事项API测试用例
演示如何测试FastAPI应用
"""

import pytest
from fastapi.testclient import TestClient
from datetime import datetime
import json
import os
import tempfile
from pathlib import Path

# 导入主应用
from main import app, TodoStorage, TodoCreate

# 创建测试客户端
client = TestClient(app)


class TestTodoAPI:
    """待办事项API测试类"""
    
    def setup_method(self):
        """每个测试方法前的设置"""
        # 使用临时文件进行测试
        self.temp_dir = tempfile.mkdtemp()
        self.test_data_file = Path(self.temp_dir) / "test_todos.json"
        
        # 临时替换存储
        global storage
        storage = TodoStorage(str(self.test_data_file))
    
    def teardown_method(self):
        """每个测试方法后的清理"""
        import shutil
        shutil.rmtree(self.temp_dir, ignore_errors=True)
    
    def test_root_endpoint(self):
        """测试根端点"""
        response = client.get("/")
        assert response.status_code == 200
        data = response.json()
        assert data["success"] is True
        assert "version" in data["data"]
    
    def test_create_todo(self):
        """测试创建待办事项"""
        todo_data = {
            "title": "测试待办事项",
            "description": "这是一个测试描述",
            "priority": "high"
        }
        
        response = client.post("/todos", json=todo_data)
        assert response.status_code == 201
        
        todo = response.json()
        assert todo["title"] == todo_data["title"]
        assert todo["description"] == todo_data["description"]
        assert todo["priority"] == todo_data["priority"]
        assert todo["completed"] is False
        assert "id" in todo
        assert "created_at" in todo
        assert "updated_at" in todo
    
    def test_create_todo_invalid_priority(self):
        """测试创建待办事项时使用无效优先级"""
        todo_data = {
            "title": "测试待办事项",
            "priority": "invalid"
        }
        
        response = client.post("/todos", json=todo_data)
        assert response.status_code == 422  # 验证错误
    
    def test_get_todos_empty(self):
        """测试获取空的待办事项列表"""
        response = client.get("/todos")
        assert response.status_code == 200
        assert response.json() == []
    
    def test_get_todos_with_data(self):
        """测试获取包含数据的待办事项列表"""
        # 先创建一个待办事项
        todo_data = {"title": "测试任务", "priority": "medium"}
        create_response = client.post("/todos", json=todo_data)
        created_todo = create_response.json()
        
        # 获取列表
        response = client.get("/todos")
        assert response.status_code == 200
        todos = response.json()
        assert len(todos) == 1
        assert todos[0]["id"] == created_todo["id"]
    
    def test_get_todo_by_id(self):
        """测试根据ID获取待办事项"""
        # 创建待办事项
        todo_data = {"title": "测试任务", "priority": "high"}
        create_response = client.post("/todos", json=todo_data)
        created_todo = create_response.json()
        
        # 根据ID获取
        response = client.get(f"/todos/{created_todo['id']}")
        assert response.status_code == 200
        todo = response.json()
        assert todo["id"] == created_todo["id"]
        assert todo["title"] == todo_data["title"]
    
    def test_get_todo_not_found(self):
        """测试获取不存在的待办事项"""
        fake_id = "non-existent-id"
        response = client.get(f"/todos/{fake_id}")
        assert response.status_code == 404
        assert "待办事项不存在" in response.json()["detail"]
    
    def test_update_todo(self):
        """测试更新待办事项"""
        # 创建待办事项
        todo_data = {"title": "原始标题", "priority": "medium"}
        create_response = client.post("/todos", json=todo_data)
        created_todo = create_response.json()
        
        # 更新
        update_data = {"title": "更新后的标题", "completed": True}
        response = client.put(f"/todos/{created_todo['id']}", json=update_data)
        assert response.status_code == 200
        
        updated_todo = response.json()
        assert updated_todo["title"] == "更新后的标题"
        assert updated_todo["completed"] is True
        assert updated_todo["priority"] == "medium"  # 未更新的字段保持原值
    
    def test_update_todo_not_found(self):
        """测试更新不存在的待办事项"""
        fake_id = "non-existent-id"
        update_data = {"title": "更新标题"}
        response = client.put(f"/todos/{fake_id}", json=update_data)
        assert response.status_code == 404
    
    def test_delete_todo(self):
        """测试删除待办事项"""
        # 创建待办事项
        todo_data = {"title": "待删除的任务", "priority": "low"}
        create_response = client.post("/todos", json=todo_data)
        created_todo = create_response.json()
        
        # 删除
        response = client.delete(f"/todos/{created_todo['id']}")
        assert response.status_code == 200
        
        data = response.json()
        assert data["success"] is True
        assert data["data"]["deleted_id"] == created_todo["id"]
        
        # 验证已删除
        get_response = client.get(f"/todos/{created_todo['id']}")
        assert get_response.status_code == 404
    
    def test_delete_todo_not_found(self):
        """测试删除不存在的待办事项"""
        fake_id = "non-existent-id"
        response = client.delete(f"/todos/{fake_id}")
        assert response.status_code == 404
    
    def test_toggle_todo(self):
        """测试切换待办事项状态"""
        # 创建待办事项
        todo_data = {"title": "待切换的任务", "priority": "medium"}
        create_response = client.post("/todos", json=todo_data)
        created_todo = create_response.json()
        
        # 切换状态
        response = client.get(f"/todos/{created_todo['id']}/toggle")
        assert response.status_code == 200
        
        toggled_todo = response.json()
        assert toggled_todo["completed"] is True  # 从False变为True
        
        # 再次切换
        response = client.get(f"/todos/{created_todo['id']}/toggle")
        toggled_todo = response.json()
        assert toggled_todo["completed"] is False  # 从True变回False
    
    def test_filter_todos_by_status(self):
        """测试按状态过滤待办事项"""
        # 创建多个待办事项
        client.post("/todos", json={"title": "已完成任务1", "completed": True})
        client.post("/todos", json={"title": "待完成任务1", "completed": False})
        client.post("/todos", json={"title": "已完成任务2", "completed": True})
        
        # 测试已完成过滤
        response = client.get("/todos?status=completed")
        completed_todos = response.json()
        assert len(completed_todos) == 2
        assert all(todo["completed"] for todo in completed_todos)
        
        # 测试待完成过滤
        response = client.get("/todos?status=pending")
        pending_todos = response.json()
        assert len(pending_todos) == 1
        assert all(not todo["completed"] for todo in pending_todos)
    
    def test_filter_todos_by_priority(self):
        """测试按优先级过滤待办事项"""
        # 创建不同优先级的任务
        client.post("/todos", json={"title": "高优先级", "priority": "high"})
        client.post("/todos", json={"title": "中优先级", "priority": "medium"})
        client.post("/todos", json={"title": "低优先级", "priority": "low"})
        
        # 测试高优先级过滤
        response = client.get("/todos?priority=high")
        high_priority_todos = response.json()
        assert len(high_priority_todos) == 1
        assert high_priority_todos[0]["priority"] == "high"
    
    def test_search_todos(self):
        """测试搜索待办事项"""
        # 创建测试数据
        client.post("/todos", json={"title": "学习Python编程", "description": "深入学习Python"})
        client.post("/todos", json={"title": "学习JavaScript", "description": "前端开发"})
        client.post("/todos", json={"title": "做运动", "description": "跑步锻炼"})
        
        # 搜索包含"Python"的任务
        response = client.get("/todos?search=Python")
        search_results = response.json()
        assert len(search_results) == 1
        assert "Python" in search_results[0]["title"]
    
    def test_get_stats(self):
        """测试获取统计信息"""
        # 创建测试数据
        client.post("/todos", json={"title": "已完成", "completed": True, "priority": "high"})
        client.post("/todos", json={"title": "待完成1", "completed": False, "priority": "medium"})
        client.post("/todos", json={"title": "待完成2", "completed": False, "priority": "low"})
        
        response = client.get("/stats")
        assert response.status_code == 200
        
        stats = response.json()
        assert stats["total"] == 3
        assert stats["completed"] == 1
        assert stats["pending"] == 2
        assert stats["completion_rate"] == 33.333333333333336
        assert stats["by_priority"]["high"] == 1
        assert stats["by_priority"]["medium"] == 1
        assert stats["by_priority"]["low"] == 1


class TestTodoStorage:
    """待办事项存储测试类"""
    
    def setup_method(self):
        """测试前准备"""
        self.temp_dir = tempfile.mkdtemp()
        self.data_file = Path(self.temp_dir) / "test_storage.json"
        self.storage = TodoStorage(str(self.data_file))
    
    def teardown_method(self):
        """测试后清理"""
        import shutil
        shutil.rmtree(self.temp_dir, ignore_errors=True)
    
    def test_create_and_retrieve_todo(self):
        """测试创建和检索待办事项"""
        todo_create = TodoCreate(
            title="测试任务",
            description="测试描述",
            priority="high"
        )
        
        # 创建
        todo = self.storage.create_todo(todo_create)
        assert todo.title == "测试任务"
        assert todo.priority == "high"
        assert todo.completed is False
        
        # 检索
        retrieved = self.storage.get_todo(todo.id)
        assert retrieved is not None
        assert retrieved.id == todo.id
        assert retrieved.title == todo.title
    
    def test_update_todo(self):
        """测试更新待办事项"""
        # 创建
        todo_create = TodoCreate(title="原始标题", priority="medium")
        todo = self.storage.create_todo(todo_create)
        
        # 更新
        from main import TodoUpdate
        update_data = TodoUpdate(title="更新标题", completed=True)
        updated = self.storage.update_todo(todo.id, update_data)
        
        assert updated is not None
        assert updated.title == "更新标题"
        assert updated.completed is True
        assert updated.priority == "medium"  # 未更新字段保持原值
    
    def test_delete_todo(self):
        """测试删除待办事项"""
        # 创建
        todo_create = TodoCreate(title="待删除", priority="low")
        todo = self.storage.create_todo(todo_create)
        
        # 删除
        success = self.storage.delete_todo(todo.id)
        assert success is True
        
        # 验证已删除
        retrieved = self.storage.get_todo(todo.id)
        assert retrieved is None


def run_tests():
    """运行所有测试"""
    print("运行待办事项API测试...")
    print("=" * 50)
    
    # 运行pytest
    exit_code = pytest.main([__file__, "-v"])
    
    return exit_code == 0


if __name__ == "__main__":
    success = run_tests()
    exit(0 if success else 1)