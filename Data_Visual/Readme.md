# Python 数据可视化项目 (Data Visualization Project)

## 📝 项目简介

本项目是一个基于 Python 的数据处理与可视化实战练习。通过生成数据、下载公开数据集（CSV/JSON 格式）以及调用 Web API，使用多种图形库探索数据背后的规律。项目包含从简单的数学曲线到复杂的全球地震分布图及 GitHub 热门项目分析。

## 🛠 核心工具与库

- **Python 3.x**
- **Matplotlib**: 用于绘制折线图、散点图及定制图形样式 。
- **Plotly Express**: 用于创建交互式直方图、地理散点图及 Web 数据可视化 。
- **Requests**: 用于执行 API 调用，获取远程数据（如 GitHub 和 Hacker News）。
- **Pandas**: 作为 Plotly 的依赖，用于高效处理结构化数据 。
- **CSV & JSON 模块**: 处理本地存储的原始数据文件 。

## 📂 模块说明

### 基础数据生成与模拟

- **平方数绘图 (`mpl_squares.py`)**: 学习 Matplotlib 的基本操作，包括设置标签、线宽和内置样式 。
- **随机游走 (`random_walk.py`)**: 模拟晕头转向的蚂蚁移动路径，探索数据的随机性与艺术化呈现 。
- **掷骰子模拟 (`die_visual.py`)**: 使用 Plotly 模拟掷骰子结果并统计频率，生成交互式直方图 。

### CSV 数据处理（天气分析）

- **温度趋势图 (`sitka_highs.py`)**: 解析 CSV 文件，提取并绘制阿拉斯加锡特卡（Sitka）的最高与最低气温 。
- **错误检查机制 (`death_valley_highs_lows.py`)**: 学习使用 `try-except-else` 结构处理现实数据集中可能存在的缺失值 。

### JSON 数据处理（全球地震）

- **地震散点图 (`eq_world_map.py`)**: 处理 GeoJSON 格式的全球地震数据，根据震级设置标记的大小和颜色，直观展现地球板块边界 。

### API 自动采集与可视化

- **GitHub 热门项目 (`python_repos_visual.py`)**: 调用 GitHub API 获取星数最多的 Python 项目，并生成带超链接的交互式条形图 。
- **Hacker News 讨论分析 (`hn_submissions.py`)**: 采集 Hacker News 实时热门文章，并根据评论数进行排序分析 。

## 🚀 快速开始

### 环境准备

在终端中执行以下命令安装必要的依赖库：

```bash
python -m pip install --user matplotlib plotly pandas requests
```

### 数据准备

- 确保本地存在`data/` 文件夹。
- 将配套的 CSV 和 GeoJSON 原始文件放置在对应目录下 

### 运行程序

以查看 GitHub 热门项目为例：

Bash

```
python python_repos_visual.py
```

程序运行后，会自动在浏览器中打开一个交互式图表页面。