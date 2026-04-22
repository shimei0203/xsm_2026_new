
# langchain_demo.py  100% 支持 Python3.8
from langchain_openai import ChatOpenAI
from langchain_community.tools import DuckDuckGoSearchRun

# ===================== 模型配置（国内可用） =====================
llm = ChatOpenAI(
    model="qwen-turbo",
    api_key="sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)

# 联网搜索工具
search = DuckDuckGoSearchRun()

# ===================== 执行智能体任务 =====================
question = "2026年AI智能体发展趋势"

print("正在联网搜索...")
search_result = search.run(question)

print("AI 正在总结...")
response = llm.invoke(f"""
请根据资料，简洁、清晰地回答问题：

资料：{search_result}
问题：{question}
""")

# 输出结果
print("\n===== AI 智能体回答 =====")
print(response.content)




# # 不使用智能体。
# question = "2026年AI智能体发展趋势"

# print("AI 直接回答（无联网搜索）...")
# response = llm.invoke(f"""
# 请简洁、清晰地回答问题：

# 问题：{question}
# """)

# print("\n===== 无搜索·AI 直接回答 =====")
# print(response.content)





""" 联网搜索工具
# python langchain_demo.py 
正在联网搜索...
AI 正在总结...

===== AI 智能体回答 =====
2026年，AI智能体呈现出以下发展趋势：  
1. **开源 AI 智能体受欢迎**：如 OpenClaw（小龙虾）等开源项目在 GitHub 上获得大量关注，因其本地运行、低门槛操作和自动执行任务等特点而备受欢迎。  
2. **AI 工具普及化**：AI 技术逐渐下沉到更多应用场景，如编程领域出现如 GLM Coding Plan 这样的订阅制 AI 编程工具，深度集成主流开发环境。  
3. **AI 平台多样化**：如 Kimi 平台等 AI 服务不断涌现，提供多样化的功能支持。  
4. **人才与技术积累**：中国在人工智能领域持续积累人才和技术，工程师群体庞大且勤奋，为 AI 发展提供了坚实基础。
"""





""" 不使用智能体
# python langchain_demo.py 
AI 直接回答（无联网搜索）...

===== 无搜索·AI 直接回答 =====
2026年AI智能体的发展趋势主要包括：

1. **更强的自主决策能力**：AI智能体在复杂环境中的自主学习和决策能力显著提升。  
2. **多模态融合**：结合视觉、语音、文本等多模态信息，提升理解和交互能力。  
3. **行业深度应用**：在医疗、金融、制造、交通等领域实现更广泛和深入的应用。  
4. **人机协作增强**：与人类协同工作更加自然、高效，成为生产力的重要组成部分。  
5. **伦理与安全强化**：AI治理和安全性得到更多关注，确保技术可控、可信。
"""



# # ====================== 换模型只改这里 ======================
#  1. 使用 DeepSeek
# llm = ChatOpenAI(
#     model="deepseek-chat",
#     api_key="你的KEY",
#     base_url="https://api.deepseek.com/v1"
# )

# # Create LLM
# llm = ChatOpenAI(
#     model="gpt-4o-mini",   # fast + cheap
#     # model="gpt-3.5-turbo",
#     temperature=0.7
# )


""" 不是很确定，没有一一试过。但是应该大差不差。꒰⸝⸝⸝•ᴗ•⸝⸝⸝꒱ 𓄼𓆩🌷𓆪
Not entirely sure, haven't tried each one. But it should be pretty close.
如果你想看“还有哪些 tools”，常见的一批包括这些：

搜索类：BingSearchRun、GoogleSearchRun、GoogleSerperRun、SearxSearchRun、BraveSearch、WikipediaQueryRun、ArxivQueryRun。

邮件类：GmailSearch、GmailSendMessage、O365SearchEmails、O365SendMessage。

文件与系统类：ReadFileTool、WriteFileTool、ListDirectoryTool、CopyFileTool、MoveFileTool、DeleteFileTool。

数据库类：QuerySQLDataBaseTool、ListSQLDatabaseTool、InfoSQLDatabaseTool、QuerySparkSQLTool。

网页与浏览类：NavigateTool、NavigateBackTool、ExtractTextTool、ExtractHyperlinksTool、GetElementsTool。

其他实用类：PythonREPLTool、PythonAstREPLTool、ShellTool、HumanInputRun、YouTubeSearchTool、WolframAlphaQueryRun。

"""