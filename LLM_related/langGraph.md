LangGraph
https://www.langchain.com/langgraph

具有代理性的平衡代理人控制
设计能够可靠处理复杂任务的代理，LangGraph 是一个代理运行时和低级编排框架。

LangGraph是开源的吗？它是免费的吗？
是的。LangGraph 是一个获得麻省理工学院许可的开源库，免费使用。



``` python
from langchain.agents import create_agent

def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"

agent = create_agent(
    model="claude-sonnet-4-6",
    tools=[get_weather],
    system_prompt="You are a helpful assistant",
)

# Run the agent
agent.invoke(
    {"messages": [{"role": "user", "content": "what is the weather in sf"}]}
)
```






参考列表：
TypeScript 是带有类型语法的 JavaScript。
Markdown 指南是一本免费且开源的参考指南，解释如何使用 Markdown，这是一种简单易用的标记语言，几乎可以用来格式化任何文档。

``` cpp
bool getBit(int num, int i) {
    return ((num & (1<<i)) != 0);
}
```

# mv deepseek.md DeepSeek.md
mv: 'deepseek.md' and 'DeepSeek.md' are the same file
