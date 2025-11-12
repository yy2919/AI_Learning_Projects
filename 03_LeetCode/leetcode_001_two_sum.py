# LeetCode #1: Two Sum
# Author: Yang Yang
# Date: 2025-11-10
# Description: Find indices of two numbers that add up to target.

def twoSum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i

# Example test
if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    print(twoSum(nums, target))  # Expected output: [0, 1]
# test
