# 数据格式 data-00000-of-00001.arrow

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Belle 数据集处理：arrow → jsonl + 随机采样 + 截取前N条
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Belle 数据集处理：arrow → jsonl + 随机100条 + 前200条，全部存到 temp_data

import os
import json
import random
from datasets import load_from_disk

# ===================== 路径配置 =====================
DATASET_PATH = "/mnt/d/wsl/datasets/train_0.5M_CN/train"  # 你之前保存的数据集路径
TEMP_DIR = "./temp_data"          # 临时文件夹

# 创建临时文件夹
os.makedirs(TEMP_DIR, exist_ok=True)

JSONL_ALL = os.path.join(TEMP_DIR, "belle_all.jsonl")
JSONL_RANDOM_100 = os.path.join(TEMP_DIR, "belle_random_100.jsonl")
JSONL_TOP_200 = os.path.join(TEMP_DIR, "belle_top_200.jsonl")


# ===================== 加载数据集 =====================
print("正在加载数据集...")
ds = load_from_disk(DATASET_PATH)

# 打印数据集信息
print("\n===== 数据集信息 =====")
print(ds)
print(f"总条数：{len(ds)}")

# ===================== 查看第一条数据（检查） =====================
print("\n===== 第一条数据 =====")
print(json.dumps(ds[0], indent=2, ensure_ascii=False))

# ===================== 1. 导出全部数据为 JSONL =====================
print("\n导出全部数据 → JSONL...")
with open(JSONL_ALL, "w", encoding="utf-8") as f:
    for item in ds:
        f.write(json.dumps(item, ensure_ascii=False) + "\n")

# ===================== 2. 随机抽取 100 条 =====================
print("随机抽取 100 条数据...")
#你做实验、训练模型,必须保证每次随机选的数据都一样,不然结果无法复现，别人也无法重复你的工作
random.seed(42) #固定随机顺序

#random.sample(XXX, 100)不重复地随机选 100 个序号不会抽到重复数据
indices = random.sample(range(len(ds)), 100)
sample_100 = ds.select(indices)

with open(JSONL_RANDOM_100, "w", encoding="utf-8") as f:
    for item in sample_100:
        f.write(json.dumps(item, ensure_ascii=False) + "\n")

# ===================== 3. 截取前 200 条 =====================
print("截取前 200 条数据...")
#书，range(200) = 第 1 页～第 200 页，ds.select() = 把这 200 页撕下来做成新书
top_200 = ds.select(range(200))

with open(JSONL_TOP_200, "w", encoding="utf-8") as f:
    for item in top_200:
        f.write(json.dumps(item, ensure_ascii=False) + "\n")

# ===================== 完成 =====================
print("\n✅ 处理完成！所有文件保存在：")
print(f"📂 {TEMP_DIR}")
print(f"📄 全部数据：{JSONL_ALL}")
print(f"📄 随机100条：{JSONL_RANDOM_100}")
print(f"📄 前200条：{JSONL_TOP_200}")