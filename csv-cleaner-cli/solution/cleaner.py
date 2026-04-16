import csv
import re

def clean_csv(input_file: str, output_file: str = "../clean_data.csv"):
    # 允许的真实邮箱域名（你可以自己增删）#Permitted real email domain names (you can add or delete them yourself)

    ALLOWED_DOMAINS = {
    # 国内最常用（必加）#Most commonly used domestically (mandatory)
    "163.com",
    "126.com",
    "qq.com",
    "vip.qq.com",
    "foxmail.com",
    "sina.com",
    "sina.cn",
    "sohu.com",
    "139.com",  # 移动
    "189.com",  # 电信
    "wo.cn",    # 联通

    # 国际常用#Commonly used internationally
    "gmail.com",
    "outlook.com",
    "hotmail.com",
    "live.com",
    "yahoo.com",
    "yahoo.cn",
    "icloud.com",
    "protonmail.com",
    "aol.com",
    "msn.com",

    # 企业/办公常用#Commonly used in enterprises/offices
    "aliyun.com",
    "dingtalk.com",
    "feishu.cn",
}
#     P_ALLOWED_DOMAINS = {
#     "gmail.com",
#     "qq.com",
#     "163.com",
#     "outlook.com",
#     "hotmail.com",
#     "yahoo.com",
#     "126.com",
#     "icloud.com",
#     "sina.com",
#     "139.com"
# }
    # 真实邮箱正则（支持数字邮箱，支持163/qq/gmail等）#Real email regularization (supports digital email, 163/qq/gmail, etc.)
    email_pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')

    seen_ids = set()
    cleaned_rows = []

    # 逐条读取原始 CSV#Read the original CSV one by one
    with open(input_file, 'r', encoding='utf-8', newline='') as infile:
        reader = csv.DictReader(infile)

        for row_num, row in enumerate(reader, start=2):
            print(f"\n📝 处理第 {row_num} 行数据：{row}")

            # ========== 1. 检查 ID（第一步） ==========
            raw_id = row.get('id', '').strip()
            if not raw_id:
                print(f"🚫 不通过：ID 为空，终止检查")
                continue  # 不通过 → 直接跳过后面所有逻辑

            if not raw_id.isdigit():
                print(f"🚫 不通过：ID 不是数字 ({raw_id})，终止检查")
                continue

            user_id = int(raw_id)
            if user_id in seen_ids:
                print(f"🚫 不通过：ID 重复 ({user_id})，终止检查")
                continue

            # ========== 2. 检查邮箱是否为空（第二步） ==========
            raw_email = row.get('email', '').strip().lower()
            if not raw_email:
                print(f"🚫 不通过：邮箱为空，终止检查")
                continue

            # ========== 3. 检查邮箱格式（第三步） ==========
            if not email_pattern.match(raw_email):
                print(f"🚫 不通过：邮箱格式错误 ({raw_email})，终止检查")
                continue

            # ========== 4. 拆分邮箱域名（第四步） ==========
            try:
                email_name, email_domain = raw_email.split('@', 1)
            except ValueError:
                print(f"🚫 止检查")
                continue

            # ========== 5. 检查域名是否在白名单（第五步） ==========
            if email_domain not in ALLOWED_DOMAINS:
                print(f"🚫 不通过：邮箱域名不合法 ({email_domain})，终止检查")
                continue不通过：邮箱拆分失败，终

            # ===================== 所有校验全部通过 =====================
            seen_ids.add(user_id)
            raw_name = row.get('name', '').strip()  # 姓名完全宽松
            cleaned_rows.append({
                "id": user_id,
                "name": raw_name,
                "email": raw_email
            })
            print(f"✅ 通过：id={user_id} | name={raw_name} | email={raw_email}")
            
    # 第一步：先把所有 email 取出来#Step 1: Retrieve all emails first
    seen_emails = set()
    for row in cleaned_rows:
        email = row.get("email", "").strip()
        if email:
            seen_emails.add(email)

    # 第二步：去重逻辑，email 相同只保留第一条#Step 2: Remove duplicate logic, keep only the first email if it is the same
    cleaned_rows_unique = []
    seen = set()
    for row in cleaned_rows:
        email = row.get("email", "").strip()
        if email not in seen:
            seen.add(email)
            cleaned_rows_unique.append(row)
        else:
            print(f"发现重复邮箱：{email}，已删除后续重复数据，仅保留第一条")

    # 写入文件
    with open(output_file, 'w', encoding='utf-8', newline='') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=["id", "name", "email"])
        writer.writeheader()
        writer.writerows(cleaned_rows_unique)

        print(f"✅ 清洗完成！有效数据：{len(cleaned_rows_unique)} 条")
        return cleaned_rows_unique

# 运行清洗#Run cleaning
if __name__ == "__main__":
    # 把你的脏 CSV 文件名放在这里#Put your dirty CSV file name here
    clean_csv("../environment/dirty_data.csv")  # 请改成你的真实文件名