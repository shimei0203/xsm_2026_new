#!/bin/bash

# 进入项目根目录（确保路径正确）#Enter the root directory of the project (ensure the path is correct)

cd "$(dirname "$0")"

# 运行清洗主程序
python3 cleaner.py

# 提示完成
echo -e "\n========================"
echo "✅ 数据清洗任务已执行完成！"
echo "========================"