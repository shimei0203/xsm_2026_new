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

# ===================== 超参数【提速版 全参微调】=====================
MODEL_NAME = "bert-base-uncased"
NUM_EPOCHS = 1
MAX_SEQ_LEN = 128
OUTPUT_DIR = "./bert_full_speed"

# 模型加载 & 全参开放
from transformers import AutoModelForSequenceClassification, AutoTokenizer
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSequenceClassification.from_pretrained(
    MODEL_NAME, num_labels=2
).to(device)

# 全参数可训练（你要的全参）
for param in model.parameters():
    param.requires_grad = True

total = sum(p.numel() for p in model.parameters())
trainable = sum(p.numel() for p in model.parameters() if p.requires_grad)
print(f"✅ 总参数: {total:,} | 全参可训练: {trainable:,}")

# 数据处理
from datasets import load_dataset
def tokenize_func(examples):
    return tokenizer(examples["text"], truncation=True, max_length=MAX_SEQ_LEN)

dataset = load_dataset("imdb")
tokenized_data = dataset.map(tokenize_func, batched=True)

# 🔥 提速关键：只用少量数据训练，速度爆炸快
train_data = tokenized_data["train"].shuffle(seed=42).select(range(4000))
test_data = tokenized_data["test"].shuffle(seed=42).select(range(500))

# 评估指标
def compute_metrics(eval_pred):
    logits, labels = eval_pred
    predictions = np.argmax(logits, axis=-1)
    return {"accuracy": (predictions == labels).mean().item()}

# ===================== 训练参数【2060极致提速配置】=====================
from transformers import TrainingArguments, Trainer, DataCollatorWithPadding
training_args = TrainingArguments(
    output_dir=OUTPUT_DIR,
    per_device_train_batch_size=8,
    per_device_eval_batch_size=8,
    learning_rate=2e-5,       # BERT标准最优学习率
    num_train_epochs=NUM_EPOCHS,
    logging_steps=20,
    evaluation_strategy="epoch",
    save_strategy="no",        # 不存权重 提速
    weight_decay=0.01,
    warmup_ratio=0.05,
    fp16=True,                # 🔥 混合精度 提速40%+
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
print("\n🚀 快速全参微调开始...")
trainer.train()

# 测试集结果
print("\n========== 测试集最终结果 ==========")
eval_results = trainer.evaluate()
print(f"✅ 测试集准确率: {eval_results['eval_accuracy']:.4f}")
print(f"✅ 测试集损失: {eval_results['eval_loss']:.4f}")

# 推理
print("\n========== 自定义文本测试 ==========")
test_texts = [
    "This movie is fantastic and totally worth watching",
    "It’s boring and a complete waste of time",
    "The plot is exciting and the acting is perfect",
    "The story is dull and the characters are flat",
    "Great visuals and a warm, touching story",
    "Full of plot holes and a terrible ending",
]

model.eval()
for text in test_texts:
    inputs = tokenizer(text, return_tensors="pt", truncation=True).to(device)
    with torch.no_grad():
        pred = torch.argmax(model(**inputs).logits, dim=1).item()
    print(f"文本: {text}")
    print(f"情感: {'正面' if pred==1 else '负面'}\n")






"""
========== 测试集最终结果 ==========
{'eval_loss': 0.6339907050132751, 'eval_accuracy': 0.858, 'eval_runtime': 1.8823, 'eval_samples_per_second': 265.634, 'eval_steps_per_second': 33.47, 'epoch': 3.0}
✅ 测试集准确率: 0.8580
✅ 测试集损失: 0.6340
"""


"""
========== 测试集最终结果 ==========
{'eval_loss': 0.67840576171875, 'eval_accuracy': 0.838, 'eval_runtime': 1.7541, 'eval_samples_per_second': 285.043, 'eval_steps_per_second': 35.915, 'epoch': 3.0}
✅ 测试集准确率: 0.8380
✅ 测试集损失: 0.6784
"""


"""
========== 测试集最终结果 ==========
{'eval_loss': 0.3388783037662506, 'eval_accuracy': 0.862, 'eval_runtime': 1.7057, 'eval_samples_per_second': 293.139, 'eval_steps_per_second': 36.935, 'epoch': 1.0}
✅ 测试集准确率: 0.8620
✅ 测试集损失: 0.3389
"""