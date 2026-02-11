#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
待办事项Web API
基于FastAPI的RESTful API示例，演示现代Python Web开发
"""

from fastapi import FastAPI, HTTPException, Query, Path
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from datetime import datetime
import json
import uuid
import os
from pathlib import Path


# 数据模型定义
class TodoBase(BaseModel):
    """待办事项基础模型"""
    title: str = Field(..., min_length=1, max_length=200, description="待办事项标题")
    description: Optional[str] = Field(None, max_length=1000, description="详细描述")
    priority: str = Field("medium", regex="^(low|medium|high)$", description="优先级")
    completed: bool = Field(False, description="是否完成")


class TodoCreate(TodoBase):
    """创建待办事项模型"""
    pass


class TodoUpdate(BaseModel):
    """更新待办事项模型"""
    title: Optional[str] = Field(None, min_length=1, max_length=200)
    description: Optional[str] = Field(None, max_length=1000)
    priority: Optional[str] = Field(None, regex="^(low|medium|high)$")
    completed: Optional[bool] = None


class Todo(TodoBase):
    """完整的待办事项模型"""
    id: str = Field(..., description="唯一标识符")
    created_at: datetime = Field(..., description="创建时间")
    updated_at: datetime = Field(..., description="更新时间")
    
    class Config:
        json_encoders = {
            datetime: lambda v: v.isoformat()
        }


class TodoResponse(BaseModel):
    """API响应模型"""
    success: bool
    message: str
    data: Optional[Any] = None


# 数据存储管理
class TodoStorage:
    """待办事项数据存储管理器"""
    
    def __init__(self, data_file: str = "todos.json"):
        self.data_file = Path(data_file)
        self.todos: Dict[str, Todo] = {}
        self.load_todos()
    
    def load_todos(self):
        """从文件加载待办事项"""
        if self.data_file.exists():
            try:
                with open(self.data_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    for todo_data in data:
                        todo = Todo(**todo_data)
                        self.todos[todo.id] = todo
            except Exception as e:
                print(f"加载数据失败: {e}")
                self.todos = {}
    
    def save_todos(self):
        """保存待办事项到文件"""
        try:
            data = []
            for todo in self.todos.values():
                todo_dict = todo.dict()
                # 确保日期时间正确序列化
                todo_dict['created_at'] = todo.created_at.isoformat()
                todo_dict['updated_at'] = todo.updated_at.isoformat()
                data.append(todo_dict)
            
            with open(self.data_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"保存数据失败: {e}")
    
    def create_todo(self, todo_create: TodoCreate) -> Todo:
        """创建新待办事项"""
        todo_id = str(uuid.uuid4())
        now = datetime.now()
        
        todo = Todo(
            id=todo_id,
            title=todo_create.title,
            description=todo_create.description,
            priority=todo_create.priority,
            completed=todo_create.completed,
            created_at=now,
            updated_at=now
        )
        
        self.todos[todo_id] = todo
        self.save_todos()
        return todo
    
    def get_todo(self, todo_id: str) -> Optional[Todo]:
        """获取特定待办事项"""
        return self.todos.get(todo_id)
    
    def get_all_todos(self) -> List[Todo]:
        """获取所有待办事项"""
        return list(self.todos.values())
    
    def update_todo(self, todo_id: str, todo_update: TodoUpdate) -> Optional[Todo]:
        """更新待办事项"""
        if todo_id not in self.todos:
            return None
        
        todo = self.todos[todo_id]
        update_data = todo_update.dict(exclude_unset=True)
        
        for field, value in update_data.items():
            setattr(todo, field, value)
        
        todo.updated_at = datetime.now()
        self.save_todos()
        return todo
    
    def delete_todo(self, todo_id: str) -> bool:
        """删除待办事项"""
        if todo_id not in self.todos:
            return False
        
        del self.todos[todo_id]
        self.save_todos()
        return True
    
    def filter_todos(self, status: Optional[str] = None, 
                    priority: Optional[str] = None,
                    search: Optional[str] = None) -> List[Todo]:
        """过滤待办事项"""
        todos = self.get_all_todos()
        
        if status == "completed":
            todos = [todo for todo in todos if todo.completed]
        elif status == "pending":
            todos = [todo for todo in todos if not todo.completed]
        
        if priority:
            todos = [todo for todo in todos if todo.priority == priority]
        
        if search:
            search_lower = search.lower()
            todos = [
                todo for todo in todos 
                if search_lower in todo.title.lower() or 
                (todo.description and search_lower in todo.description.lower())
            ]
        
        return todos


# 创建FastAPI应用实例
app = FastAPI(
    title="待办事项API",
    description="一个简单的待办事项管理RESTful API",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# 添加CORS中间件
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 初始化数据存储
storage = TodoStorage()


# API端点定义
@app.get("/", response_model=TodoResponse)
async def root():
    """根端点，返回API信息"""
    return TodoResponse(
        success=True,
        message="待办事项API服务运行中",
        data={
            "version": "1.0.0",
            "endpoints": {
                "todos": "/todos",
                "docs": "/docs"
            }
        }
    )


@app.get("/todos", response_model=List[Todo])
async def get_todos(
    status: Optional[str] = Query(None, regex="^(completed|pending)$", description="按状态过滤"),
    priority: Optional[str] = Query(None, regex="^(low|medium|high)$", description="按优先级过滤"),
    search: Optional[str] = Query(None, min_length=1, description="搜索关键词")
):
    """获取待办事项列表"""
    todos = storage.filter_todos(status=status, priority=priority, search=search)
    return todos


@app.post("/todos", response_model=Todo, status_code=201)
async def create_todo(todo: TodoCreate):
    """创建新的待办事项"""
    return storage.create_todo(todo)


@app.get("/todos/{todo_id}", response_model=Todo)
async def get_todo(todo_id: str = Path(..., description="待办事项ID")):
    """获取特定待办事项"""
    todo = storage.get_todo(todo_id)
    if todo is None:
        raise HTTPException(status_code=404, detail="待办事项不存在")
    return todo


@app.put("/todos/{todo_id}", response_model=Todo)
async def update_todo(
    todo_id: str = Path(..., description="待办事项ID"),
    todo_update: TodoUpdate = None
):
    """更新待办事项"""
    todo = storage.update_todo(todo_id, todo_update)
    if todo is None:
        raise HTTPException(status_code=404, detail="待办事项不存在")
    return todo


@app.delete("/todos/{todo_id}", response_model=TodoResponse)
async def delete_todo(todo_id: str = Path(..., description="待办事项ID")):
    """删除待办事项"""
    success = storage.delete_todo(todo_id)
    if not success:
        raise HTTPException(status_code=404, detail="待办事项不存在")
    
    return TodoResponse(
        success=True,
        message="待办事项删除成功",
        data={"deleted_id": todo_id}
    )


@app.get("/todos/{todo_id}/toggle", response_model=Todo)
async def toggle_todo(todo_id: str = Path(..., description="待办事项ID")):
    """切换待办事项完成状态"""
    todo = storage.get_todo(todo_id)
    if todo is None:
        raise HTTPException(status_code=404, detail="待办事项不存在")
    
    update_data = TodoUpdate(completed=not todo.completed)
    updated_todo = storage.update_todo(todo_id, update_data)
    return updated_todo


@app.get("/stats", response_model=Dict[str, Any])
async def get_stats():
    """获取统计信息"""
    todos = storage.get_all_todos()
    total = len(todos)
    completed = sum(1 for todo in todos if todo.completed)
    pending = total - completed
    
    priority_stats = {
        "high": sum(1 for todo in todos if todo.priority == "high"),
        "medium": sum(1 for todo in todos if todo.priority == "medium"),
        "low": sum(1 for todo in todos if todo.priority == "low")
    }
    
    return {
        "total": total,
        "completed": completed,
        "pending": pending,
        "completion_rate": (completed / total * 100) if total > 0 else 0,
        "by_priority": priority_stats
    }


# 启动函数
def main():
    """启动API服务器"""
    import uvicorn
    
    print("启动待办事项API服务器...")
    print("API文档: http://localhost:8000/docs")
    print("API服务: http://localhost:8000")
    
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )


if __name__ == "__main__":
    main()