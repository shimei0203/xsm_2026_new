# 导入题解类，文件名不允许纯数字哦。Importing solution classes does not allow file names to be purely numerical.
# 也不允许用数字开头哦。It is also not allowed to start with a number.

from threesum_15 import Solution


from tqdm import tqdm  # 进度条库，Python 内置/常用  Progress bar library, built-in/commonly used in Python

from threesum_15 import Solution
from tqdm import tqdm

def sort_triplet(triplet):
    """统一排序，避免顺序不同导致判错"""
    return sorted(triplet)

def normalize_res(res):
    """结果标准化排序，消除顺序差异"""
    return sorted([sort_triplet(item) for item in res])

def main():
    sol = Solution()

    # 结构化测试用例：【输入数组，标准答案，用例描述】
    test_cases = [
        {
            "nums": [-1, 0, 1, 2, -1, -4],
            "expect": [[-1, -1, 2], [-1, 0, 1]],
            "desc": "常规重复元素组合"
        },
        {
            "nums": [0, 1, 1],
            "expect": [],
            "desc": "无满足条件三元组"
        },
        {
            "nums": [0, 0, 0],
            "expect": [[0, 0, 0]],
            "desc": "全零特殊用例"
        },
        {
            "nums": [],
            "expect": [],
            "desc": "空数组边界"
        },
        {
            "nums": [0],
            "expect": [],
            "desc": "数组长度为1"
        },
        {
            "nums": [1, 2],
            "expect": [],
            "desc": "数组长度为2"
        },
        {
            "nums": [1, 2, 3],
            "expect": [],
            "desc": "全正数无结果"
        },
        {
            "nums": [-5, -3, -1],
            "expect": [],
            "desc": "全负数无结果"
        },
        {
            "nums": [0, 0, 1],
            "expect": [],
            "desc": "双0+正数"
        },
        {
            "nums": [-2, 0, 1, 1, 2],
            "expect": [[-2, 0, 2], [-2, 1, 1]],
            "desc": "多组有效解"
        },
        {
            "nums": [1, -1, -1, 0],
            "expect": [[-1, 0, 1]],
            "desc": "大量重复负数"
        },
        {
            "nums": [-4, -2, -2, 0, 2, 2, 4],
            "expect": [[-4, 0, 4], [-4, 2, 2], [-2, -2, 4], [-2, 0, 2]],
            "desc": "密集重复元素"
        },
        {
            "nums": [0, -1, 1],
            "expect": [[-1, 0, 1]],
            "desc": "最简合法三元组"
        }
    ]

    total = len(test_cases)
    pass_cnt = 0
    fail_cnt = 0

    print("=" * 80)
    print(f"三数之和 自动化测试 | 总用例数: {total}")
    print("=" * 80)

    for idx, case in enumerate(tqdm(test_cases, desc="测试进度", ncols=75)):
        nums = case["nums"]
        expect = case["expect"]
        desc = case["desc"]

        # 执行函数
        actual = sol.threeSum(nums)

        # 标准化：防止内部顺序、数组排序不同导致误判
        actual_norm = normalize_res(actual)
        expect_norm = normalize_res(expect)

        print(f"\n【用例 {idx+1}】{desc}")
        print(f"输入: {nums}")
        print(f"预期输出: {expect}")
        print(f"实际输出: {actual}")

        if actual_norm == expect_norm:
            print("✅ 测试通过")
            pass_cnt += 1
        else:
            print("❌ 测试失败")
            fail_cnt += 1
        print("-" * 80)

    # 汇总统计
    print("\n" + "=" * 80)
    print(f"测试汇总: 总计 {total} 条 | 通过 {pass_cnt} 条 | 失败 {fail_cnt} 条")
    if fail_cnt == 0:
        print("🎉 全部用例通过！")
    else:
        print("⚠️ 存在失败用例，请检查代码逻辑")
    print("=" * 80)

if __name__ == "__main__":
    main()