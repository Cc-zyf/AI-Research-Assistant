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
