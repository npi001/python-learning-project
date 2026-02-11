#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
销售数据分析项目
使用pandas和matplotlib进行数据分析和可视化
演示Python在数据处理方面的强大能力
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import argparse
import json
from pathlib import Path
from datetime import datetime, timedelta
from typing import Dict, List, Tuple, Any
import warnings

# 设置中文显示
plt.rcParams['font.sans-serif'] = ['SimHei', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

# 忽略警告
warnings.filterwarnings('ignore')

# 设置样式
sns.set_style("whitegrid")
plt.style.use('seaborn-v0_8')


class SalesAnalyzer:
    """销售数据分析器"""
    
    def __init__(self):
        self.data = None
        self.report = {
            'generated_at': datetime.now().isoformat(),
            'summary': {},
            'analysis': {},
            'charts': []
        }
    
    def load_data(self, file_path: str) -> bool:
        """加载销售数据"""
        try:
            # 根据文件扩展名选择加载方式
            if file_path.endswith('.csv'):
                self.data = pd.read_csv(file_path, encoding='utf-8')
            elif file_path.endswith('.xlsx'):
                self.data = pd.read_excel(file_path)
            elif file_path.endswith('.json'):
                self.data = pd.read_json(file_path, encoding='utf-8')
            else:
                raise ValueError("不支持的文件格式，请使用CSV、Excel或JSON文件")
            
            # 数据预处理
            self._preprocess_data()
            print(f"成功加载数据：{len(self.data)} 条记录")
            return True
            
        except Exception as e:
            print(f"加载数据失败: {e}")
            return False
    
    def _preprocess_data(self):
        """数据预处理"""
        # 确保日期列存在并转换为datetime类型
        date_columns = ['date', 'order_date', 'created_at', '日期']
        for col in date_columns:
            if col in self.data.columns:
                self.data['date'] = pd.to_datetime(self.data[col])
                break
        
        # 如果没有日期列，创建一个模拟日期列
        if 'date' not in self.data.columns:
            self.data['date'] = pd.date_range(
                start='2023-01-01', 
                periods=len(self.data), 
                freq='D'
            )
        
        # 确保数值列存在
        numeric_columns = ['amount', 'price', 'total', '金额', '总价']
        for col in numeric_columns:
            if col in self.data.columns:
                self.data['amount'] = pd.to_numeric(self.data[col], errors='coerce')
                break
        
        if 'amount' not in self.data.columns:
            # 生成模拟金额数据
            self.data['amount'] = np.random.uniform(100, 10000, len(self.data))
        
        # 确保产品列存在
        product_columns = ['product', 'item', '商品', '产品']
        for col in product_columns:
            if col in self.data.columns:
                self.data['product'] = self.data[col]
                break
        
        if 'product' not in self.data.columns:
            # 生成模拟产品数据
            products = ['电子产品', '服装', '食品', '图书', '家居用品', '运动器材']
            self.data['product'] = np.random.choice(products, len(self.data))
        
        # 清理数据
        self.data = self.data.dropna(subset=['amount', 'date'])
        self.data['month'] = self.data['date'].dt.to_period('M')
        self.data['year'] = self.data['date'].dt.year
        self.data['quarter'] = self.data['date'].dt.quarter
    
    def generate_summary(self) -> Dict[str, Any]:
        """生成数据摘要"""
        summary = {
            'total_records': len(self.data),
            'date_range': {
                'start': self.data['date'].min().strftime('%Y-%m-%d'),
                'end': self.data['date'].max().strftime('%Y-%m-%d'),
                'days': (self.data['date'].max() - self.data['date'].min()).days
            },
            'total_sales': float(self.data['amount'].sum()),
            'average_sale': float(self.data['amount'].mean()),
            'median_sale': float(self.data['amount'].median()),
            'max_sale': float(self.data['amount'].max()),
            'min_sale': float(self.data['amount'].min()),
            'unique_products': self.data['product'].nunique(),
            'total_months': self.data['month'].nunique()
        }
        
        self.report['summary'] = summary
        return summary
    
    def analyze_sales_trend(self) -> Dict[str, Any]:
        """分析销售趋势"""
        # 按月份统计销售
        monthly_sales = self.data.groupby('month')['amount'].agg(['sum', 'count', 'mean']).reset_index()
        monthly_sales['month_str'] = monthly_sales['month'].dt.strftime('%Y-%m')
        
        # 计算增长率
        monthly_sales['growth_rate'] = monthly_sales['sum'].pct_change() * 100
        
        # 按季度统计
        quarterly_sales = self.data.groupby(['year', 'quarter'])['amount'].sum().reset_index()
        quarterly_sales['period'] = quarterly_sales['year'].astype(str) + 'Q' + quarterly_sales['quarter'].astype(str)
        
        analysis = {
            'monthly_trend': {
                'months': monthly_sales['month_str'].tolist(),
                'sales': monthly_sales['sum'].tolist(),
                'orders': monthly_sales['count'].tolist(),
                'growth_rates': monthly_sales['growth_rate'].fillna(0).tolist()
            },
            'quarterly_trend': {
                'periods': quarterly_sales['period'].tolist(),
                'sales': quarterly_sales['amount'].tolist()
            },
            'trend_insights': self._analyze_trend_insights(monthly_sales)
        }
        
        self.report['analysis']['sales_trend'] = analysis
        return analysis
    
    def _analyze_trend_insights(self, monthly_sales: pd.DataFrame) -> List[str]:
        """分析趋势洞察"""
        insights = []
        
        # 计算总体趋势
        if len(monthly_sales) >= 3:
            recent_growth = monthly_sales['sum'].iloc[-1] - monthly_sales['sum'].iloc[-3]
            if recent_growth > 0:
                insights.append(f"最近三个月销售额增长 {recent_growth:.2f}")
            else:
                insights.append(f"最近三个月销售额下降 {abs(recent_growth):.2f}")
        
        # 找出最佳和最差月份
        best_month = monthly_sales.loc[monthly_sales['sum'].idxmax()]
        worst_month = monthly_sales.loc[monthly_sales['sum'].idxmin()]
        
        insights.append(f"最佳销售月份: {best_month['month_str']} (销售额: {best_month['sum']:.2f})")
        insights.append(f"最差销售月份: {worst_month['month_str']} (销售额: {worst_month['sum']:.2f})")
        
        return insights
    
    def analyze_product_performance(self) -> Dict[str, Any]:
        """分析产品表现"""
        # 按产品统计
        product_stats = self.data.groupby('product').agg({
            'amount': ['sum', 'count', 'mean', 'std'],
            'date': ['min', 'max']
        }).round(2)
        
        product_stats.columns = ['总销售额', '订单数', '平均单价', '价格标准差', '首次销售', '最后销售']
        product_stats = product_stats.sort_values('总销售额', ascending=False)
        
        # 计算市场份额
        total_sales = product_stats['总销售额'].sum()
        product_stats['市场份额'] = (product_stats['总销售额'] / total_sales * 100).round(2)
        
        # ABC分析
        product_stats['累计份额'] = product_stats['市场份额'].cumsum()
        product_stats['ABC分类'] = product_stats['累计份额'].apply(
            lambda x: 'A' if x <= 70 else 'B' if x <= 90 else 'C'
        )
        
        analysis = {
            'product_ranking': product_stats.to_dict('index'),
            'top_products': product_stats.head(5).index.tolist(),
            'abc_analysis': {
                'A类产品': product_stats[product_stats['ABC分类'] == 'A'].index.tolist(),
                'B类产品': product_stats[product_stats['ABC分类'] == 'B'].index.tolist(),
                'C类产品': product_stats[product_stats['ABC分类'] == 'C'].index.tolist()
            },
            'market_concentration': product_stats['市场份额'].head(3).sum()
        }
        
        self.report['analysis']['product_performance'] = analysis
        return analysis
    
    def create_charts(self, output_dir: str) -> List[str]:
        """创建图表"""
        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)
        
        chart_files = []
        
        # 1. 销售趋势图
        chart_file = self._create_sales_trend_chart(output_path)
        if chart_file:
            chart_files.append(chart_file)
        
        # 2. 产品销售饼图
        chart_file = self._create_product_pie_chart(output_path)
        if chart_file:
            chart_files.append(chart_file)
        
        # 3. 产品表现条形图
        chart_file = self._create_product_bar_chart(output_path)
        if chart_file:
            chart_files.append(chart_file)
        
        # 4. 月度销售热力图
        chart_file = self._create_monthly_heatmap(output_path)
        if chart_file:
            chart_files.append(chart_file)
        
        self.report['charts'] = chart_files
        return chart_files
    
    def _create_sales_trend_chart(self, output_path: Path) -> str:
        """创建销售趋势图"""
        try:
            monthly_data = self.data.groupby('month')['amount'].sum().reset_index()
            monthly_data['month_str'] = monthly_data['month'].dt.strftime('%Y-%m')
            
            plt.figure(figsize=(12, 6))
            plt.plot(monthly_data['month_str'], monthly_data['amount'], 
                    marker='o', linewidth=2, markersize=6, color='#2E86AB')
            plt.title('月度销售趋势', fontsize=16, fontweight='bold')
            plt.xlabel('月份', fontsize=12)
            plt.ylabel('销售额', fontsize=12)
            plt.xticks(rotation=45)
            plt.grid(True, alpha=0.3)
            plt.tight_layout()
            
            chart_file = output_path / 'sales_trend.png'
            plt.savefig(chart_file, dpi=300, bbox_inches='tight')
            plt.close()
            
            return str(chart_file)
        except Exception as e:
            print(f"创建销售趋势图失败: {e}")
            return ""
    
    def _create_product_pie_chart(self, output_path: Path) -> str:
        """创建产品销售饼图"""
        try:
            product_sales = self.data.groupby('product')['amount'].sum().sort_values(ascending=False)
            
            plt.figure(figsize=(10, 8))
            colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEAA7', '#DDA0DD']
            wedges, texts, autotexts = plt.pie(product_sales.values, labels=product_sales.index, 
                                             autopct='%1.1f%%', colors=colors[:len(product_sales)],
                                             startangle=90, textprops={'fontsize': 10})
            
            plt.title('产品销售额分布', fontsize=16, fontweight='bold')
            plt.axis('equal')
            
            chart_file = output_path / 'product_distribution.png'
            plt.savefig(chart_file, dpi=300, bbox_inches='tight')
            plt.close()
            
            return str(chart_file)
        except Exception as e:
            print(f"创建产品饼图失败: {e}")
            return ""
    
    def _create_product_bar_chart(self, output_path: Path) -> str:
        """创建产品表现条形图"""
        try:
            product_stats = self.data.groupby('product')['amount'].agg(['sum', 'count']).reset_index()
            product_stats = product_stats.sort_values('sum', ascending=False)
            
            fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
            
            # 销售额条形图
            ax1.bar(product_stats['product'], product_stats['sum'], color='#2E86AB')
            ax1.set_title('产品销售额排名', fontweight='bold')
            ax1.set_xlabel('产品')
            ax1.set_ylabel('销售额')
            ax1.tick_params(axis='x', rotation=45)
            
            # 订单数条形图
            ax2.bar(product_stats['product'], product_stats['count'], color='#A23B72')
            ax2.set_title('产品订单数排名', fontweight='bold')
            ax2.set_xlabel('产品')
            ax2.set_ylabel('订单数')
            ax2.tick_params(axis='x', rotation=45)
            
            plt.tight_layout()
            
            chart_file = output_path / 'product_comparison.png'
            plt.savefig(chart_file, dpi=300, bbox_inches='tight')
            plt.close()
            
            return str(chart_file)
        except Exception as e:
            print(f"创建产品对比图失败: {e}")
            return ""
    
    def _create_monthly_heatmap(self, output_path: Path) -> str:
        """创建月度销售热力图"""
        try:
            # 创建年-月销售矩阵
            monthly_pivot = self.data.pivot_table(
                values='amount', 
                index=self.data['date'].dt.year, 
                columns=self.data['date'].dt.month, 
                aggfunc='sum', 
                fill_value=0
            )
            
            plt.figure(figsize=(12, 6))
            sns.heatmap(monthly_pivot, annot=True, fmt='.0f', cmap='YlOrRd', 
                       cbar_kws={'label': '销售额'})
            plt.title('年度月度销售热力图', fontsize=16, fontweight='bold')
            plt.xlabel('月份')
            plt.ylabel('年份')
            
            chart_file = output_path / 'monthly_heatmap.png'
            plt.savefig(chart_file, dpi=300, bbox_inches='tight')
            plt.close()
            
            return str(chart_file)
        except Exception as e:
            print(f"创建热力图失败: {e}")
            return ""
    
    def generate_sample_data(self, output_file: str) -> bool:
        """生成示例数据"""
        try:
            np.random.seed(42)
            
            # 生成基础数据
            n_records = 1000
            start_date = datetime(2023, 1, 1)
            end_date = datetime(2024, 12, 31)
            
            dates = [start_date + timedelta(days=np.random.randint(0, (end_date - start_date).days)) 
                    for _ in range(n_records)]
            
            products = ['电子产品', '服装', '食品', '图书', '家居用品', '运动器材']
            product_weights = [0.25, 0.20, 0.15, 0.15, 0.15, 0.10]
            
            selected_products = np.random.choice(products, n_records, p=product_weights)
            
            # 根据产品类别生成不同的价格范围
            price_ranges = {
                '电子产品': (500, 5000),
                '服装': (100, 1000),
                '食品': (20, 200),
                '图书': (30, 300),
                '家居用品': (150, 1500),
                '运动器材': (200, 2000)
            }
            
            amounts = []
            for product in selected_products:
                min_price, max_price = price_ranges[product]
                amounts.append(np.random.uniform(min_price, max_price))
            
            # 创建DataFrame
            data = pd.DataFrame({
                'date': dates,
                'product': selected_products,
                'amount': amounts,
                'quantity': np.random.randint(1, 5, n_records),
                'customer_id': [f'C{np.random.randint(1000, 9999)}' for _ in range(n_records)]
            })
            
            data = data.sort_values('date').reset_index(drop=True)
            
            # 保存数据
            if output_file.endswith('.csv'):
                data.to_csv(output_file, index=False, encoding='utf-8')
            elif output_file.endswith('.xlsx'):
                data.to_excel(output_file, index=False)
            elif output_file.endswith('.json'):
                data.to_json(output_file, orient='records', date_format='iso', force_ascii=False, indent=2)
            
            print(f"示例数据已生成: {output_file}")
            print(f"数据记录数: {len(data)}")
            return True
            
        except Exception as e:
            print(f"生成示例数据失败: {e}")
            return False
    
    def save_report(self, output_file: str) -> bool:
        """保存分析报告"""
        try:
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(self.report, f, ensure_ascii=False, indent=2)
            print(f"分析报告已保存: {output_file}")
            return True
        except Exception as e:
            print(f"保存报告失败: {e}")
            return False
    
    def run_full_analysis(self, data_file: str, output_dir: str) -> bool:
        """运行完整的分析流程"""
        print("开始销售数据分析...")
        print("=" * 50)
        
        # 加载数据
        if not self.load_data(data_file):
            return False
        
        # 生成摘要
        summary = self.generate_summary()
        print(f"\n数据摘要:")
        print(f"总记录数: {summary['total_records']}")
        print(f"时间范围: {summary['date_range']['start']} 至 {summary['date_range']['end']}")
        print(f"总销售额: {summary['total_sales']:.2f}")
        print(f"平均销售额: {summary['average_sale']:.2f}")
        print(f"产品种类: {summary['unique_products']}")
        
        # 趋势分析
        trend_analysis = self.analyze_sales_trend()
        print(f"\n趋势分析:")
        for insight in trend_analysis['trend_insights']:
            print(f"• {insight}")
        
        # 产品分析
        product_analysis = self.analyze_product_performance()
        print(f"\n产品分析:")
        print(f"TOP 5产品: {', '.join(product_analysis['top_products'])}")
        print(f"市场集中度(前三产品): {product_analysis['market_concentration']:.2f}%")
        
        # 创建图表
        charts = self.create_charts(output_dir)
        print(f"\n图表生成:")
        for chart in charts:
            print(f"• {chart}")
        
        # 保存报告
        report_file = Path(output_dir) / 'analysis_report.json'
        self.save_report(str(report_file))
        
        print(f"\n分析完成! 结果保存在: {output_dir}")
        return True


def main():
    """主函数"""
    parser = argparse.ArgumentParser(
        description="销售数据分析工具",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例用法:
  %(prog)s --data sales.csv --output report/
  %(prog)s --generate-sample sample_data.csv
  %(prog)s --data sales.xlsx --output analysis/ --create-charts
        """
    )
    
    parser.add_argument('--data', metavar='FILE', help='销售数据文件(CSV/Excel/JSON)')
    parser.add_argument('--output', metavar='DIR', default='analysis_report', 
                       help='输出目录 (默认: analysis_report)')
    parser.add_argument('--generate-sample', metavar='FILE', 
                       help='生成示例数据文件')
    parser.add_argument('--create-charts', action='store_true', 
                       help='创建图表 (默认已启用)')
    
    args = parser.parse_args()
    
    analyzer = SalesAnalyzer()
    
    try:
        if args.generate_sample:
            success = analyzer.generate_sample_data(args.generate_sample)
        elif args.data:
            success = analyzer.run_full_analysis(args.data, args.output)
        else:
            parser.print_help()
            return
        
        if success:
            print("\n✓ 分析完成!")
        else:
            print("\n✗ 分析失败!")
            
    except KeyboardInterrupt:
        print("\n\n分析被用户中断")
    except Exception as e:
        print(f"\n程序错误: {e}")


if __name__ == '__main__':
    main()