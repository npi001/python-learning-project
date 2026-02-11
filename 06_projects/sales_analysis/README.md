# 销售数据分析项目

## 项目概述
一个完整的销售数据分析工具，使用pandas进行数据处理，matplotlib和seaborn进行数据可视化，演示Python在数据科学领域的强大能力。

## 功能特性
- 支持多种数据格式（CSV、Excel、JSON）
- 自动数据清洗和预处理
- 销售趋势分析
- 产品表现分析
- ABC分析（产品分类）
- 多种图表可视化
- 示例数据生成
- 完整分析报告

## 技术要点
- pandas - 数据处理和分析
- matplotlib & seaborn - 数据可视化
- numpy - 数值计算
- 数据预处理和清洗
- 统计分析方法
- 图表设计和美化

## 运行方式

### 安装依赖
```bash
pip install pandas matplotlib seaborn numpy
```

### 生成示例数据
```bash
python analyze.py --generate-sample sales_data.csv
```

### 运行分析
```bash
python analyze.py --data sales_data.csv --output analysis_report/
```

### 支持的数据格式
- CSV文件 (.csv)
- Excel文件 (.xlsx)
- JSON文件 (.json)

## 分析报告内容

### 1. 数据摘要
- 总记录数和时间范围
- 总销售额、平均销售额
- 产品种类统计

### 2. 趋势分析
- 月度销售趋势
- 季度销售对比
- 增长率分析
- 趋势洞察

### 3. 产品分析
- 产品销售排名
- 市场份额分析
- ABC分类（重要产品识别）
- 订单统计

### 4. 可视化图表
- 月度销售趋势线图
- 产品销售额饼图
- 产品表现对比条形图
- 年度月度销售热力图

## 示例用法

### 基本分析
```bash
# 使用默认输出目录
python analyze.py --data sales.csv

# 指定输出目录
python analyze.py --data sales.xlsx --output my_report/
```

### 数据预处理
程序会自动：
- 识别日期列并转换为datetime格式
- 识别金额列并转换为数值类型
- 识别产品列用于分类分析
- 清理无效数据

### 生成示例数据
```bash
# 生成CSV格式的示例数据
python analyze.py --generate-sample sample_sales.csv

# 生成Excel格式的示例数据
python analyze.py --generate-sample sample_sales.xlsx
```

## 输出文件

分析完成后会在输出目录生成：

1. **analysis_report.json** - 完整的分析数据
2. **sales_trend.png** - 销售趋势图
3. **product_distribution.png** - 产品分布饼图
4. **product_comparison.png** - 产品对比图
5. **monthly_heatmap.png** - 月度销售热力图

## 学习目标
通过这个项目，你将学会：
1. 使用pandas进行数据加载和清洗
2. 数据分组、聚合和分析
3. 时间序列数据处理
4. 统计分析方法应用
5. 数据可视化和图表设计
6. 完整的数据分析工作流

## 扩展练习
1. 添加更多数据源支持（数据库、API等）
2. 实现交互式仪表板
3. 添加预测功能（时间序列预测）
4. 实现数据质量检查
5. 添加更多可视化类型
6. 支持实时数据处理
7. 添加Web界面展示

## 数据要求

### 推荐的数据列
- `date`, `order_date`, `created_at` - 订单日期
- `amount`, `price`, `total`, `金额` - 销售金额
- `product`, `item`, `商品` - 产品名称
- `quantity` - 数量（可选）
- `customer_id` - 客户ID（可选）

### 自动适配
程序会自动识别常见的列名，即使你的数据使用不同的列名也能正常工作。

## 性能优化
- 使用向量化操作提高处理速度
- 内存优化的大数据集处理
- 可配置的采样频率