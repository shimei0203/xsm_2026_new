# 导入题解类，文件名不允许纯数字哦。Importing solution classes does not allow file names to be purely numerical.
# 也不允许用数字开头哦。It is also not allowed to start with a number.

from threesum_15 import Solution


from tqdm import tqdm  # 进度条库，Python 内置/常用  Progress bar library, built-in/commonly used in Python

def main():
    sol = Solution()

    # 定义所有测试用例（方便统一管理 + 进度条遍历）
    test_cases = [
        {"nums": [-1, 0, 1, 2, -1, -4], "desc": "常规重复负数组合"},
        {"nums": [0, 1, 1], "desc": "无有效三元组"},
        {"nums": [0, 0, 0], "desc": "全零三元组"},
        # 你可以无限加用例
        # 👇 新增边界用例（非常重要）
        {"nums": [], "desc": "空数组"},
        {"nums": [0], "desc": "数组长度不足3"},
        {"nums": [1, 2], "desc": "数组长度不足3"},
        {"nums": [1, 2, 3], "desc": "全正数，无结果"},
        {"nums": [-1, -2, -3], "desc": "全负数，无结果"},
        {"nums": [0, 0, 1], "desc": "两个0+正数，无结果"},
        {"nums": [-2, 0, 1, 1, 2], "desc": "双指针经典边界：两组解"},
        {"nums": [1, -1, -1, 0], "desc": "重复元素+相邻正负"},
        {"nums": [-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6], "desc": "大量重复元素（最难场景）"},
        {"nums": [0, -1, 1], "desc": "最简有效三元组"},
    ]


    print("=" * 60)
    print("开始执行 ThreeSum 测试（共 {} 组）".format(len(test_cases)))
    print("=" * 60)

    # 带进度条的测试循环
    for idx, case in enumerate(tqdm(test_cases, desc="测试进度", ncols=70)):
        nums = case["nums"]
        desc = case["desc"]
        
        print(f"\n📌 测试用例 {idx+1}：{desc}")
        print(f"输入数组：{nums}")
        
        result = sol.threeSum(nums)
        print(f"输出结果：{result}")
        
        print("-" * 50)

    print("\n✅ 所有测试用例执行完毕！")

if __name__ == "__main__":
    main()