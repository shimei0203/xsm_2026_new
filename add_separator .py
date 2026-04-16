# 不完美    𓆝𓆟𓆜𓆞    imperfect
import re

# 分隔符号
sep = "   𓆝𓆟𓆜𓆞   "

def process_line(line):
    return re.sub(
        r'([\u4e00-\u9fff]+)\s*((\d+\.|[A-Z]).*)$',
        rf'\1{sep}\2',
        line
    )

# 处理文件
def process_md(input_path, output_path):
    with open(input_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    new_lines = [process_line(line) for line in lines]

    with open(output_path, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)


if __name__ == "__main__":
    # 把这里改成你的 md 文件路径
    input_file = "Interesting_thing.md"
    output_file = "Interesting_thing_format_output.md"
    process_md(input_file, output_file)
    print("处理完成！已保存到", output_file)