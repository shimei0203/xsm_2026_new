# 15. 三数之和
# 中等
# 相关标签
# premium lock icon
# 提示
# 给你一个整数数组 nums ，判断是否存在三元组 [nums[i], nums[j], nums[k]] 满足 i != j、i != k 且 j != k ，同时还满足 nums[i] + nums[j] + nums[k] == 0 。请你返回所有和为 0 且不重复的三元组。

# 注意：答案中不可以包含重复的三元组。

#LeetCode: There is a question about the sum of three numbers in LeetCode


#!/usr/bin/python3

"""
示例 1：

输入：nums = [-1,0,1,2,-1,-4]
输出：[[-1,-1,2],[-1,0,1]]
解释：
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0 。
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0 。
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0 。
不同的三元组是 [-1,0,1] 和 [-1,-1,2] 。
注意，输出的顺序和三元组的顺序并不重要。
示例 2：

输入：nums = [0,1,1]
输出：[]
解释：唯一可能的三元组和不为 0 。
示例 3：

输入：nums = [0,0,0]
输出：[[0,0,0]]
解释：唯一可能的三元组和为 0 。
"""


from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        # 先对数组排序：核心前提，方便双指针 + 去重  ^-^  Sort the array first: core premise, convenient for double pointers+deduplication
        nums.sort()
        # 存储最终答案 Store the final answer
        ans = []
        
        # 枚举第一个数 a（固定第一个数） ^-^  List the first number a (fixed first number)
        for first in range(n):
            # 去重：如果当前数和上一个数一样，直接跳过，避免重复三元组  ^-^   De duplication: If the current number is the same as the previous number, skip it directly to avoid repeating triplets
            if first > 0 and nums[first] == nums[first - 1]:
                continue 
            
            # 第三个数指针初始指向数组最右端  ^-^  The third number pointer initially points to the rightmost end of the array
            third = n - 1
            # 目标：b + c = -a，这样 a+b+c=0   ^-^  Goal: b+c=- a, so that a+b+c=0
            target = -nums[first]
            
            # 枚举第二个数 b List the second number b
            for second in range(first + 1, n):
                # 去重：当前数和上一个数一样，跳过  ^-^  De duplication: The current number is the same as the previous number, skip it
                if second > first + 1 and nums[second] == nums[second - 1]:
                    continue
                
                # 让 c 尽可能小，使 b + c 不大于 target ^-^ Make c as small as possible, so that b+c is not greater than the target
                while second < third and nums[second] + nums[third] > target:
                    third -= 1
                
                # 如果指针重合，后面不可能找到符合条件的数，直接退出
                if second == third:
                    break
                
                # 找到符合条件的 b + c = target，即 a + b + c = 0
                if nums[second] + nums[third] == target:
                    ans.append([nums[first], nums[second], nums[third]])
        
        return ans