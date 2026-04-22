#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 3.61M, 3610K 4.85G ----train_3.5M_CN
# 286M， 519K ------train_0.5M_CN

import os

# # 【关键】国内加速，必须加这一行
os.environ["HF_ENDPOINT"] = "https://hf-mirror.com"

# 自动安装依赖
try:
    from datasets import load_dataset
except ImportError:
    os.system("pip install datasets -U")
    from datasets import load_dataset

# ===================== 核心代码 =====================
if __name__ == "__main__":
    print("正在下载 BelleGroup/train_0.5M_CN 数据集...")
    
    # 下载 + 自动缓存
    dataset = load_dataset(
        "BelleGroup/train_0.5M_CN",
        cache_dir="./cache"  # 下载到当前目录的 cache 文件夹
    )

    # 打印信息
    print("\n下载完成！数据集信息：")
    print(dataset)

    # 保存到本地文件夹（方便以后直接用）
    dataset.save_to_disk("./train_0.5M_CN")
    print("\n✅ 数据集已保存到：./train_0.5M_CN")


