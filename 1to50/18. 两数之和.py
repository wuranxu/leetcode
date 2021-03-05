from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) < 4:
            return []
        nums.sort()
        i = 0
        ans = []
        for i in range(len(nums) - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

        while i <= len(nums) - 4:
            j = i + 1
            x = j + 1
            y = len(nums) - 1
            while j <= len(nums) - 3:
                while x < y:
                    if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:
                        break
                    if nums[i] + nums[len(nums) - 1] + nums[len(nums) - 2] + nums[len(nums) - 3] < target:
                        break
                    sm = nums[x] + nums[y] + nums[i] + nums[j]
                    if sm == target:
                        ans.append([nums[i], nums[j], nums[x], nums[y]])
                        x += 1
                        y -= 1
                    elif target > sm:
                        x += 1
                    else:
                        y -= 1
                j += 1
                while j < len(nums) and nums[j] == nums[j - 1]:
                    j += 1
                x = j + 1
                y = len(nums) - 1
            i += 1
            while i < len(nums) and nums[i] == nums[i - 1]:
                i += 1
        return ans


if __name__ == "__main__":
    s = Solution()
    array = [0, 0, 0, 0]
    target = 0
    rs = s.fourSum(array, target)
    print(rs)
