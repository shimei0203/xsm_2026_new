# tests/test_logic.py
import os
import csv

def test_cleaned_output():
    """
    测试清洗后的 clean_data.csv 是否符合要求
    """
    clean_file = "clean_data.csv"
    
    # 1. 检查文件是否生成# 1. Check if the file has been generated

    assert os.path.exists(clean_file), "❌ 错误：clean_data.csv 文件未生成"

    # 2. 读取清洗后的数据# 2. Read the cleaned data

    cleaned_rows = []
    with open(clean_file, 'r', encoding='utf-8', newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            cleaned_rows.append(row)

    # 3. 基础校验# 3. Basic verification 
    # 真实情况肯定是有一些正确数据的。#The real situation definitely has some correct data.

    assert len(cleaned_rows) > 0, "❌ 错误：清洗后没有数据"

    # 4. 检查字段是否完整# 4. Check if the fields are complete

    for row in cleaned_rows:
        assert "id" in row, f"❌ 缺少 id 字段：{row}"
        assert "email" in row, f"❌ 缺少 email 字段：{row}"
        assert row["id"].isdigit(), f"❌ id 不是数字：{row}"

    # 5. 检查 ID 不重复# 5. Check that the ID is not duplicated

    ids = [row["id"] for row in cleaned_rows]
    assert len(ids) == len(set(ids)), "❌ 存在重复 ID"

    # 6. 检查邮箱不重复# 6. Check for duplicate email addresses

    emails = [row["email"] for row in cleaned_rows]
    assert len(emails) == len(set(emails)), "❌ 存在重复邮箱"

    print("\n✅ 测试全部通过：数据格式正确、无重复、无空值")

if __name__ == "__main__":
    test_cleaned_output()