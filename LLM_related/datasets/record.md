我需要一些文本数据集
种类多样

## 1	
Salesforce/wikitext

## 2
openai/gsm8k

```plaintext
Natalia sold clips to 48 of her friends in April, and then she sold half as many clips in May. How many clips did Natalia sell altogether in April and May?
 sold half as many clips in May. How many clips did Natalia sell altogether in April and May?
Natalia sold 48/2 = <<48/2=24>>24 clips in May.
Natalia sold 48+24 = <<48+24=72>>72 clips altogether in April and May.
#### 72
```

```
娜塔莉亚在四月份向她的48位朋友卖出了视频片段，然后在五月份卖出的数量是四月份的一半。
娜塔莉亚在四月和五月一共卖出了多少个视频片段？

娜塔莉亚在五月份卖出了 \(48 \div 2 = 24\) 个视频片段。
娜塔莉亚在四月和五月一共卖出了 \(48 + 24 = 72\) 个视频片段。

#### 72
```

## 3
mrmrx/CADS-dataset
CADS-dataset:   CADS 数据集：
22,022 CT volumes with complete annotations for 167 anatomical structures.
包含 167 种解剖结构的 22,022 个 CT 数据集，均附有完整标注。
Most extensive whole-body CT dataset, exceeding current collections in both scale (18x more CT scans) and anatomical coverage (60% more distinct targets).
规模最大的全身 CT 数据集：无论是在数据量上（CT 扫描数量多 18 倍），还是在解剖结构覆盖范围上（涵盖的独立目标多 60%），均优于现有的所有数据集。
Data collected from publicly available datasets and private hospital data, spanning 100+ imaging centers across 16 countries.
数据来源于公开数据集和私立医院的数据，涵盖了 16 个国家的 100 多家影像中心。



## 4
yahma/alpaca-cleaned
规模：约 5.2 万条指令
特点：斯坦福 Alpaca 的高质量清理版，覆盖写作、问答、翻译、摘要、代码、常识、推理等几十类任务
提示词多样性：高，句式、长度、任务类型都很均衡
output:
The passage discusses a study that highlights the significance of global climate change as a challenge. It goes on to mention the consequences such as rising sea levels and loss of biodiversity. Climate change is caused by human activities with potential for long-term devastating impacts if not addressed.
该文章介绍了一项研究，强调了全球气候变化作为一项挑战的重要性。文章还提到了由此带来的后果，如海平面上升和生物多样性丧失。气候变化是人类活动造成的，如果不加以应对，可能会带来长期的破坏性影响。
input:
A recent study showed that global climate change is one of the most important challenges facing the world today. The consequences of global warming include rising sea levels, extreme weather events and biodiversity loss. Climate change is caused by human activities such as burning fossil fuels, and if unchecked will have long-term and devastating impacts on the planet.
一项最新研究表明，全球气候变化是当今世界面临的最重要挑战之一。全球变暖的后果包括海平面上升、极端天气事件以及生物多样性的丧失。气候变化是由人类活动引起的，比如燃烧化石燃料。如果不加以控制，气候变化将对地球造成长期且毁灭性的影响。
instruction：
Summarize the given passage.
总结给定的段落。




## 5
Open-Orca/OpenOrca
规模：约 100 万条高质量指令 - 响应对
特点：基于 GPT-4 生成，复杂推理、多步逻辑、数学、长文本指令极多
提示词多样性：极高，覆盖大量复杂、少样本、思维链类 Prompt

system_prompt:
You are a helpful assistant, who always provide explanation. Think like you are answering to a five year old.
你是个乐于助人的助手，总是会给出解释。想象自己正在回答一个五岁小孩的问题。

question:
What happens next in this paragraph?

She then rubs a needle on a cotton ball then pushing it onto a pencil and wrapping thread around it. She then holds up a box of a product and then pouring several liquids into a bowl. she
Choose your answer from: A. adds saucepan and shakes up the product in a grinder. B. pinches the thread to style a cigarette, and then walks away. C. then dips the needle in ink and using the pencil to draw a design on her leg, rubbing it off with a rag in the end. D. begins to style her hair and cuts it several times before parting the ends of it to show the hairstyle she has created.
这段文字接下来会讲什么？

她先将针在棉球上摩擦，然后把棉球按在铅笔上，再用线将其缠紧。接着，她拿起一盒产品，将几种液体倒入碗中。她
请从以下选项中选择答案：A. 在研磨器中加入炖锅并搅拌产品。B. 捏弄香烟的烟丝来整理形状，然后离开。C. 将针浸入墨水中，用铅笔在腿上画出图案，最后用布擦掉。D. 开始整理头发，多次修剪后再分开发梢，展示自己设计的发型。

response:
C. She then dips the needle in ink and using the pencil to draw a design on her leg, rubbing it off with a rag in the end. In this option, she is continuing the process of using the needle, pencil, and thread, which is most related to what she was doing in the previous sentence.
C. 接着她把针浸入墨水中，用铅笔在腿上画出图案，最后用布把墨迹擦掉。在这个步骤中，她继续使用针、铅笔和线，这与前一句中所描述的动作十分相似。


## 6
BAAI/Infinity-Instruct
（智源）
规模：744 万条基础指令 + 149 万对话指令
特点：覆盖数学、代码、常识、百科、写作、翻译、逻辑等全领域
提示词多样性：极高，覆盖简单到复杂、短到超长指令

## 7
pacozaa/mistral-sharegpt90k

## 8
timdettmers/openassistant-guanaco


```
### Human: Can you write a short introduction about the relevance of the term "monopsony" in economics? Please use examples related to potential monopsonies in the labour market and cite relevant research.### Assistant: "Monopsony" refers to a market structure where there is only one buyer for a particular good or service. In economics, this term is particularly relevant in the labor market, where a monopsony employer has significant power over the wages and working conditions of their employees. The presence of a monopsony can result in lower wages and reduced employment opportunities for workers, as the employer has little incentive to increase wages or provide better working conditions.

Recent research has identified potential monopsonies in industries such as retail and fast food, where a few large companies control a significant portion of the market (Bivens & Mishel, 2013). In these industries, workers often face low wages, limited benefits, and reduced bargaining power, leading to a situation where they are dependent on the employer for their livelihood. This dependence can result in further suppression of wages and a decline in working conditions.

Overall, the concept of monopsony is essential to understanding the dynamics of labor markets and the impact of market power on workers. Further research is needed to understand the extent and impact of monopsonies on the economy and to develop policies to address this issue.

References:
Bivens, J., & Mishel, L. (2013). The Pay of Corporate Executives and Financial Professionals as Evidence of Rents in Top 1 Percent Incomes. Journal of Economic Perspectives, 27(3), 57-78.### Human: Now explain it to a dog

### 人类用户：能否简要介绍一下“买方垄断”这一经济学概念的关联性？请举例说明劳动力市场中的买方垄断现象，并引用相关研究。### 智能助手：“买方垄断”是指某种商品或服务只有一个买方的市场结构。在经济学中，这一概念在劳动力市场尤为重要。在买方垄断的情况下，雇主对员工的工资和工作条件拥有极大影响力。由于雇主没有动力提高工资或改善工作条件，因此可能导致工资水平下降和就业机会减少。

最新研究指出，在零售和快餐等行业中存在潜在的买方垄断现象，少数大型企业掌控了市场的大部分份额（Bivens & Mishel, 2013）。在这些行业中，工人往往面临低工资、有限的福利以及较弱的议价能力，不得不依赖雇主来维持生计。这种依赖关系会进一步压低工资水平，恶化工作条件。

总体而言，买方垄断这一概念对于理解劳动力市场的运行机制以及市场力量对工人的影响至关重要。需要进一步的研究来弄清买方垄断对经济的程度和影响，并制定相应的政策来应对这一问题。

参考文献：
Bivens, J., & Mishel, L. (2013). 高管与金融从业人员的薪酬：来自收入最高 1%人群的租金证据。《经济展望杂志》，27(3)，57-78。### 人类：现在试着给狗解释一下吧。
```

## 9
llamafactory/alpaca_gpt4_zh
 llamafactory/alpaca_gpt4_zh
规模：约 5 万条
特点：中文 Alpaca，GPT-4 生成，质量高

保持健康的三个提示。
以下是保持健康的三个提示：

1. 保持身体活动。每天做适当的身体运动，如散步、跑步或游泳，能促进心血管健康，增强肌肉力量，并有助于减少体重。

2. 均衡饮食。每天食用新鲜的蔬菜、水果、全谷物和脂肪含量低的蛋白质食物，避免高糖、高脂肪和加工食品，以保持健康的饮食习惯。

3. 睡眠充足。睡眠对人体健康至关重要，成年人每天应保证 7-8 小时的睡眠。良好的睡眠有助于减轻压力，促进身体恢复，并提高注意力和记忆力。




## 10

A:

fka/prompts.chat
Ethereum Developer  以太坊开发者
Imagine you are an experienced Ethereum developer tasked with creating a smart contract for a blockchain messenger. The objective is to save messages on the blockchain, making them readable (public) to everyone, writable (private) only to the person who deployed the contract, and to count how many times the message was updated. Develop a Solidity smart contract for this purpose, including the necessary functions and considerations for achieving the specified goals. Please provide the code and any relevant explanations to ensure a clear understanding of the implementation.
假设你是一名经验丰富的以太坊开发者，负责为一家区块链消息应用开发智能合约。该应用的目标是将消息存储在区块链上：让所有人都能读取这些消息，只有部署了该合约的人才能修改消息，并能统计消息被更新的次数。请为此目的编写一个 Solidity 智能合约，包括实现上述目标所需的所有函数和注意事项。请提供代码及相关说明，以便清晰理解该实现方式。

B:
Linux Terminal  Linux 终端
I want you to act as a linux terminal. I will type commands and you will reply with what the terminal should show. I want you to only reply with the terminal output inside one unique code block, and nothing else. do not write explanations. do not type commands unless I instruct you to do so. when i need to tell you something in english, i will do so by putting text inside curly brackets {like this}. my first command is pwd
我希望你充当一个 Linux 终端。我会输入命令，你则输出终端应该显示的内容。请只将终端的输出内容放在一个代码块中显示，不要添加其他任何内容。不要写解释性文字。除非我指示你，否则不要自行输入命令。当需要用英语与你交流时，我会把文字放在大括号{中，就像这样}。我的第一个命令是 pwd。





## 11
Provide step-by-step instructions on how to make a safe and effective homemade all-purpose cleaner from common household ingredients. The guide should include measurements, tips for storing the cleaner, and additional variations or scents that can be added. Additionally, the guide should be written in clear and concise...
提供如何利用常见家庭用品制作安全有效的自制多功能清洁剂的详细步骤。该指南应包括用量说明、清洁剂的储存方法，以及可添加的各种变种或香味。此外，指南的表述应清晰简洁……

省略

## 12


BAAI/COIG
[
{
"question": "玉露香梨和库尔勒香梨是同一种梨吗？",
"answer": "不是同一种梨，玉露香梨是以库尔勒香梨为母本、雪花梨为父本杂交育成的新品种。"
},
{
"question": "玉露香梨难道不是口感多汁、味道甜美吗？",
"answer": "确实，玉露香梨以汁多、酥脆、含糖高等品质而著名，但这些品质特点并不表明它与库尔勒香梨为同一种梨。"
},
{
"question": "玉露香梨难道不是在库尔勒市种植最多吗？",
"answer": "不是完全正确，虽然隰县是玉露香梨的主要产地，但它在其他地区，如山西、吉林、辽宁等也有种植。"
},
{
"question": "难道玉露香梨的地域范围不仅限于中国吗？",
"answer": "不仅限于中国，玉露香梨还流行于东南亚和俄罗斯等地。"
},
{
"question": "请重新介绍一下玉露香梨。",
"answer": "玉露香梨是由山西省农科院果树研究所杂交选育出的新品种，其品质与库尔勒香梨相似，但它们并不是同一种梨。玉露香梨以汁多、酥脆、含糖高、无公害等特点而广受欢迎，主产于隰县等地，远销东南亚和俄罗斯等地。需要注意的是，库尔勒香梨是一种古老而优秀的本地梨品种，其品质与玉露香梨有一些相似之处，但它们并不是同一种梨。"
}
]

YeungNLP/firefly-train-1.1M
NLI
自然语言推理：
前提：家里人心甘情愿地养他,还有几家想让他做女婿的
假设：他是被家里人收养的孤儿
中立

Summary
在上海的苹果代工厂，较低的基本工资让工人们形成了“软强制”的加班默契。加班能多拿两三千，“自愿”加班成为常态。律师提示，加班后虽能获得一时不错的报酬，但过重的工作负荷会透支身体，可能对今后劳动权利造成不利影响。
输出摘要：
苹果代工厂员工调查：为何争着“自愿”加班










参考：
Plaintext = 纯文本 / 明文，plaintext
数字、符号，没有任何格式：没有字体、颜色、加粗、图片、表格、排版，最干净、最简单的文本格式
 <<...>>、#### 72 就是 plaintext 里用来表示计算过程和答案的固定符号格式。

# Heading level 1	
## Heading level 2	
### Heading level 3	
#### Heading level 4	
##### Heading level 5


I just love **bold text**.
I just love __bold text__.


多个段落的块引用
> Dorothy followed her through many of the beautiful rooms in her castle.
>
> The Witch bade her clean the pots and kettles and sweep the floor and keep the fire fed with wo

.gguf 是 GGUF (GPT-Generated Unified Format) 格式的文件后缀，专门用于存储量化后的大型语言模型 (LLM)，是目前在个人电脑（CPU）上本地运行 AI 大模型的主流文件格式。