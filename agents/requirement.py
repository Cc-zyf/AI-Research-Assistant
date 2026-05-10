"""需求理解 Agent - 基于 DeepSeek-V3"""
from langchain.prompts import PromptTemplate

class RequirementAgent:
    def __init__(self, model="deepseek-chat"):
        self.model = model
        self.prompt = PromptTemplate(
            input_variables=["query"],
            template="分析用户需求并拆解为子任务: {query}"
        )
    
    def analyze(self, query: str):
        # TODO: 调用 DeepSeek API
        return {"sub_tasks": [], "keywords": []}