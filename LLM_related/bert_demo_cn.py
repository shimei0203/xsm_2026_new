#未完成 中文数据集还有点问题

import os
os.environ["HF_ENDPOINT"] = "https://hf-mirror.com"
os.environ["TRANSFORMERS_VERBOSITY"] = "error"

import torch
import warnings
warnings.filterwarnings('ignore')
import numpy as np


# 设备检测
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"✅ 使用设备: {device}")
if torch.cuda.is_available():
    print(f"✅ CUDA 版本: {torch.version.cuda}")

# ===================== 超参数【中文 提速版 全参微调】=====================
# 换成中文BERT模型
MODEL_NAME = "bert-base-chinese"
NUM_EPOCHS = 1
MAX_SEQ_LEN = 128
OUTPUT_DIR = "./bert_chinese_full_speed"

# 模型加载 & 全参开放
from transformers import AutoModelForSequenceClassification, AutoTokenizer
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSequenceClassification.from_pretrained(
    MODEL_NAME, num_labels=2
).to(device)

# 全参数可训练
for param in model.parameters():
    param.requires_grad = True

total = sum(p.numel() for p in model.parameters())
trainable = sum(p.numel() for p in model.parameters() if p.requires_grad)
print(f"✅ 总参数: {total:,} | 全参可训练: {trainable:,}")

# ===================== 中文数据集：ChnSentiCorp 中文情感分析 =====================
from datasets import load_dataset
def tokenize_func(examples):
    return tokenizer(
        examples["text"],
        truncation=True,
        max_length=MAX_SEQ_LEN,
        padding="max_length"
    )

# 加载标准中文情感二分类数据集

# dataset = load_dataset("imdb")
dataset = load_dataset("seamew/ChnSentiCorp")
tokenized_data = dataset.map(tokenize_func, batched=True)

# 少量数据快速训练（保持速度快）
train_data = tokenized_data["train"].shuffle(seed=42).select(range(4000))
test_data = tokenized_data["test"].shuffle(seed=42).select(range(500))


# 评估指标
def compute_metrics(eval_pred):
    logits, labels = eval_pred
    predictions = np.argmax(logits, axis=-1)
    return {"accuracy": (predictions == labels).mean().item()}
 
# ===================== 训练参数【2060极致提速】=====================
from transformers import TrainingArguments, Trainer, DataCollatorWithPadding
training_args = TrainingArguments(
    output_dir=OUTPUT_DIR,
    per_device_train_batch_size=8,
    per_device_eval_batch_size=8,
    learning_rate=2e-5,
    num_train_epochs=NUM_EPOCHS,
    logging_steps=20,
    evaluation_strategy="epoch",
    save_strategy="no",
    weight_decay=0.01,
    warmup_ratio=0.05,
    fp16=True,                # 混合精度加速
    report_to="none",
    dataloader_num_workers=0,
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_data,
    eval_dataset=test_data,
    data_collator=DataCollatorWithPadding(tokenizer=tokenizer),
    compute_metrics=compute_metrics,
)

# 训练
print("\n🚀 中文BERT 快速全参微调开始...")
trainer.train()

# 测试集结果
print("\n========== 测试集最终结果 ==========")
eval_results = trainer.evaluate()
print(f"✅ 测试集准确率: {eval_results['eval_accuracy']:.4f}")
print(f"✅ 测试集损失: {eval_results['eval_loss']:.4f}")

# 中文推理测试
print("\n========== 中文文本情感测试 ==========")
test_texts = [
    "这部电影太好看了，演员演技在线，剧情精彩，强烈推荐！",
    "太难看了，浪费时间，剧情毫无逻辑，演技尴尬",
    "画面精美，故事感人，非常值得一看",
    "节奏太慢，情节枯燥，看得昏昏欲睡",
    "非常棒的作品，温暖治愈，看完心情很好",
    "全程无亮点，剧情老套，不推荐观看",
]

model.eval()
for text in test_texts:
    inputs = tokenizer(text, return_tensors="pt", truncation=True).to(device)
    with torch.no_grad():
        pred = torch.argmax(model(**inputs).logits, dim=1).item()
    print(f"文本: {text}")
    print(f"情感: {'✅ 正面' if pred==1 else '❌ 负面'}\n")









"""
========== 测试集最终结果 ==========
{'eval_loss': 0.5742729306221008, 'eval_accuracy': 0.706, 'eval_runtime': 1.727, 'eval_samples_per_second': 289.516, 'eval_steps_per_second': 36.479, 'epoch': 3.0}
✅ 测试集准确率: 0.7060
✅ 测试集损失: 0.5743
"""


"""
========== 测试集最终结果 ==========
{'eval_loss': 0.6252944469451904, 'eval_accuracy': 0.652, 'eval_runtime': 1.6905, 'eval_samples_per_second': 295.777, 'eval_steps_per_second': 37.268, 'epoch': 1.0}
✅ 测试集准确率: 0.6520
✅ 测试集损失: 0.6253
"""