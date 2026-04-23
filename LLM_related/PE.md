来源：https://www.promptingguide.ai/applications


Let's get started by going over a basic example of a simple prompt:
我们先来看一个简单的提示语示例作为开始：

Prompt  提示/提示词
The sky is
Output:  输出：
blue.


Let's try to improve it a bit:
让我们试着把它改进一点：

Prompt:  提示：
Complete the sentence: 
The sky is
Output:  输出：
blue during the day and dark at night.

### 增加了任务目标：补全句子

<Question>or<Instruction>

prompt:
Q: <Question>?
A: 

Q: What is prompt engineering?

What is prompt engineering?

Given the standard format above, one popular and effective technique to prompting is referred to as few-shot prompting where you provide exemplars (i.e., demonstrations). You can format few-shot prompts as follows:
按照上述标准格式，一种常用且有效的提示方法被称为“少样本提示法”，即通过提供示例来进行引导。少样本提示法的格式如下：

<Question>?
<Answer>
<Question>?
<Answer>
<Question>?
<Answer>
<Question>?

The QA format version would look like this:
QA 格式版本如下所示：

Q: <Question>?
A: <Answer>
Q: <Question>?
A: <Answer>
Q: <Question>?
A: <Answer>
Q: <Question>?
A:



rompt:  提示：
This is awesome! // Positive
This is bad! // Negative
Wow that movie was rad! // Positive
What a horrible show! //
Output:  输出：
Negative


### 训练得当的话应该是zero shot就可以很好的回答问题

A prompt contains any of the following elements:
提示语包含以下任意元素：
Instruction - a specific task or instruction you want the model to perform
指令——即你希望模型执行的具体任务或指示。
Context - external information or additional context that can steer the model to better responses
上下文——能够引导模型给出更好回应的外部信息或补充背景资料
Input Data - the input or question that we are interested to find a response for
输入数据——即我们希望找到答案的输入内容或问题
Output Indicator - the type or format of the output.
输出指标——输出的类型或格式。




Classify the text into neutral, negative, or positive
Text: I think the food was okay.
Sentiment:



Prompt:  提示：
### Instruction ###
Translate the text below to Spanish:
Text: "hello!"
Output:  输出：
¡Hola!





As an example, let's try a simple prompt to extract specific information from a piece of text.
例如，我们来试一个简单的提示语，从一段文本中提取特定信息。
Prompt:  提示：
Extract the name of places in the following text. 
Desired format:
Place: <comma_separated_list_of_places>
Input: "Although these developments are encouraging to researchers, much is still a mystery. “We often have a black box between the brain and the effect we see in the periphery,” says Henrique Veiga-Fernandes, a neuroimmunologist at the Champalimaud Centre for the Unknown in Lisbon. “If we want to use it in the therapeutic context, we actually need to understand the mechanism.“"
Output:  输出：
Place: Champalimaud Centre for the Unknown, Lisbon
Input text is obtained from this Nature article.
输入文本摘自这篇《自然》杂志的文章。



Explain the concept prompt engineering. Keep the explanation short, only a few sentences, and don't be too descriptive.
Use 2-3 sentences to explain the concept of prompt engineering to a high school student.




Here is an example of a movie recommendation chatbot failing at exactly what I don't want it to do because of how I wrote the instruction -- focusing on what not to do.
以下是一个电影推荐聊天机器人的例子：由于我的指令写法的问题——我明确指出了它不该做什么，结果它反而做错了我完全不想让它做的事。

Prompt:  提示：
The following is an agent that recommends movies to a customer. DO NOT ASK FOR INTERESTS. DO NOT ASK FOR PERSONAL INFORMATION.以下是向客户推荐电影的代理商。不要要求利益。不要索取个人信息。
Customer: Please recommend a movie based on my interests.
Agent: 
Output:  输出：
Sure, I can recommend a movie based on your interests. What kind of movie would you like to watch? Do you prefer action, comedy, romance, or something else?





Prompt:  提示：
The following is an agent that recommends movies to a customer. The agent is responsible to recommend a movie from the top global trending movies. It should refrain from asking users for their preferences and avoid asking for personal information. If the agent doesn't have a movie to recommend, it should respond "Sorry, couldn't find a movie to recommend today.".以下是向客户推荐电影的代理商。代理商负责推荐全球热门电影中的一部。它应该避免询问用户的偏好，避免询问个人信息。如果代理没有推荐的电影，它应该回复“抱歉，今天找不到推荐的电影。”。
Customer: Please recommend a movie based on my interests.
Agent:
Output:  输出：
Sorry, I don't have any information about your interests. However, here's a list of the top global trending movies right now: [list of movies]. I hope you find something you like!




### 类型
虽然之前的基本示例很有趣，但在本节中，我们将介绍更高级的提示工程技术。这些技术有助于我们完成更复杂的任务，同时提升大型语言模型的可靠性和性能。

Zero-shot Prompting
  零样本提示生成
Few-shot Prompting
  少样本提示生成
Chain-of-Thought Prompting
  思维链提示法
Meta Prompting
  元提示机制
Self-Consistency
  自我一致性
Generate Knowledge Prompting
  生成知识提示词
Prompt Chaining
  提示词链式处理
Tree of Thoughts
  思想之树
Retrieval Augmented Generation
  检索增强生成
Automatic Reasoning and Tool-use
  自动推理与工具使用
Automatic Prompt Engineer
  自动提示词工程师
Active-Prompt
Directional Stimulus Prompting
  定向刺激提示
Program-Aided Language Models
  程序辅助语言模型
ReAct
Reflexion
  反思
Multimodal CoT
  多模态协同训练
Graph Prompting
  图谱提示机制


Agents  代理商/代理人

Introduction to Agents
  智能体简介
Agent Components
  代理组件
AI Workflows vs AI Agents
  AI 工作流与 AI 智能体
Context Engineering for AI Agents
  AI 智能体的上下文工程
Context Engineering Deep Dive
  上下文工程深度解析
Function Calling
  函数调用
Deep Agents
  深度智能体





### https://github.com/dair-ai/Prompt-Engineering-Guide

1. 提示词数据集（可直接训练 / 测试）
fka/awesome-chatgpt-prompts
https://huggingface.co/datasets/fka/prompts.chat
(第二次碰到了)

2. 提示词工具与 Space（在线使用）
Prompt Engineering Playground
https://huggingface.co/learn/cookbook/zh-CN/prompt_tuning_peft


3. 提示微调与 PEFT 教程（技术落地）
Hugging Face 官方 PEFT 提示微调教程

