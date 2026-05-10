# 🤖 AI Research Assistant

> 多智能体协同技术资料自动化分析平台  
> Multi-Agent Technical Document Analysis Platform

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.109+-green.svg)](https://fastapi.tiangolo.com/)
[![LangChain](https://img.shields.io/badge/LangChain-0.1+-orange.svg)](https://www.langchain.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## 📖 项目简介

基于 **LangChain + FastAPI** 构建的多智能体协同平台，通过 4 个专业 Agent 自动化分析技术文档、GitHub 仓库、学术论文等，大幅提升开发者资料消化效率（**10~20倍**）。

### 核心特性

- 🔗 **多智能体协同**：需求理解 → 信息检索 → 内容提取 → 智能总结
- ⚡ **异步任务队列**：基于 Redis 的高并发处理（峰值 50+ 并发任务）
- 🧠 **多模型支持**：DeepSeek-V3、Qwen-Max、MiMo-V2.5、GPT-4o
- 📊 **长上下文处理**：MapReduce 策略支持 100K+ tokens 输入
- 🔍 **工具集成**：Google Search API、GitHub API、ArXiv API

## 🏗️ 架构设计

## 📁 项目结构
ai-research-assistant/
├── main.py # FastAPI 入口
├── agents/
│ ├── requirement.py # 需求理解 Agent
│ ├── retrieval.py # 信息检索 Agent
│ ├── extraction.py # 内容提取 Agent
│ └── summary.py # 智能总结 Agent
├── workflows/
│ └── research_workflow.py # LangChain 工作流
├── utils/
│ ├── redis_queue.py # 异步任务队列
│ └── token_counter.py # Token 统计
├── config.py # 配置文件
└── requirements.txt



## 🚀 快速开始

```bash
# 1. 克隆仓库
git clone https://github.com/yourusername/ai-research-assistant.git
cd ai-research-assistant

# 2. 安装依赖
pip install -r requirements.txt

# 3. 配置环境变量
cp .env.example .env
# 编辑 .env 填入 API Keys

# 4. 启动 Redis
docker run -d -p 6379:6379 redis:alpine

# 5. 运行服务
uvicorn main:app --reload

📊 使用数据
✅ 已服务 12 位内测开发者
✅ 累计处理 300+ 次任务
✅ 近 14 天 Token 消耗：2.8M (日均 150K~280K)
✅ 平均响应时间：45 秒（长文档 60~90 秒）
📝 使用示例
Bash

curl -X POST http://localhost:8000/api/v1/research \
  -H "Content-Type: application/json" \
  -d '{
    "query": "分析 FastAPI 的异步架构设计",
    "sources": ["google", "github"],
    "depth": "detailed"
  }'
🛣️ Roadmap
 基础多智能体工作流
 GitHub 仓库分析
 学术论文摘要
 每日自动化扫描（GitHub Trending/ArXiv）
 方案设计与代码示例生成
 Web 界面
📄 License
MIT License - 详见 LICENSE

🙏 致谢
本项目使用以下开源技术/服务：

LangChain
FastAPI
DeepSeek
Qwen
