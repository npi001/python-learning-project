# 待办事项Web API项目

## 项目概述
基于FastAPI框架的RESTful API，演示Python在Web开发、数据验证、异步编程等方面的应用。

## 功能特性
- 创建、读取、更新、删除待办事项（CRUD）
- 数据验证和错误处理
- 自动生成API文档
- 数据持久化（JSON文件存储）
- 查询过滤功能
- 状态管理

## 技术要点
- FastAPI - 现代、快速的Web框架
- Pydantic - 数据验证和设置管理
- 异步编程支持
- RESTful API设计
- 自动API文档生成
- 数据模型设计

## 运行方式

### 安装依赖
```bash
pip install fastapi uvicorn pydantic
```

### 启动服务器
```bash
python main.py
```

或使用uvicorn:
```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### 访问API
- API服务: http://localhost:8000
- 交互式文档: http://localhost:8000/docs
- OpenAPI规范: http://localhost:8000/openapi.json

## API端点

### 待办事项管理
- `GET /todos` - 获取所有待办事项
- `POST /todos` - 创建新待办事项
- `GET /todos/{id}` - 获取特定待办事项
- `PUT /todos/{id}` - 更新待办事项
- `DELETE /todos/{id}` - 删除待办事项

### 查询过滤
- `GET /todos?status=pending` - 按状态过滤
- `GET /todos?priority=high` - 按优先级过滤
- `GET /todos?search=关键词` - 搜索待办事项

## 示例请求

### 创建待办事项
```bash
curl -X POST "http://localhost:8000/todos" \
     -H "Content-Type: application/json" \
     -d '{"title": "学习Python", "description": "完成Python基础教程", "priority": "high"}'
```

### 获取所有待办事项
```bash
curl "http://localhost:8000/todos"
```

### 更新待办事项
```bash
curl -X PUT "http://localhost:8000/todos/1" \
     -H "Content-Type: application/json" \
     -d '{"title": "学习Python（更新）", "completed": true}'
```

## 学习目标
通过这个项目，你将学会：
1. RESTful API设计和实现
2. 数据验证和模型定义
3. 异步编程概念
4. Web框架的使用
5. API文档自动生成
6. 错误处理最佳实践

## 扩展练习
1. 添加用户认证和授权
2. 集成数据库（SQLite/PostgreSQL）
3. 实现分页功能
4. 添加任务分类和标签
5. 实现任务依赖关系
6. 添加通知功能
7. 创建前端界面