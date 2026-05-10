# 🤖 AI Research Assistant
**多智能体协同技术资料分析平台** | Powered by LangChain + FastAPI

## 🔧 技术栈
- **底层模型**: DeepSeek-V3 (主力) | Qwen-Max (复杂推理) | MiMo-V2.5 (长链路)
- **后端**: FastAPI + Redis (异步任务队列)
- **工作流**: LangChain + Dify (4-Agent协同)
- **日均处理**: 20+ GitHub仓库分析 | 15+ 技术文章总结

## 📊 核心指标
| 指标          | 数值                     |
|---------------|--------------------------|
| 日均Token消耗 | 150K ~ 280K              |
| 高峰Token消耗 | 420K/日                  |
| 单任务平均    | 25K ~ 80K tokens         |
| 效率提升      | 资料消化时间压缩90%+     |

## 🚀 快速开始
```bash
git clone https://github.com/yourusername/ai-research-assistant.git
cd ai-research-assistant
pip install -r requirements.txt
uvicorn main:app --reload
