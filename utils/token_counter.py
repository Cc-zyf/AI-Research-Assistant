"""Token 消耗统计工具"""
import tiktoken

class TokenCounter:
    def __init__(self, model="gpt-4"):
        self.encoding = tiktoken.encoding_for_model(model)
    
    def count(self, text: str) -> int:
        return len(self.encoding.encode(text))